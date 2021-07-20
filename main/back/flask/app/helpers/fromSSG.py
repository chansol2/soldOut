from random import choice

import requests
from app import db
from bs4 import BeautifulSoup

uas = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
]


def fromSSG(prd, kind):

    org_url = prd.org_url

    isChanged = False

    changed = {"prd": prd}

    ua = choice(uas)

    headers = {
        "User-Agent": ua,
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    try:
        res = requests.get(org_url, headers=headers)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        if res.status_code == 401:
            raise (e)
        elif res.status_code == 404 and kind == "update":
            app.logger.info(f"product no longer available: {org_url}")
            changed["has_stock"] = "404"
            return changed
        elif res.status_code == 404 and kind == "cron":
            return
        else:
            raise (e)
    except Exception as e:
        raise (e)

    source = res.text
    soup = BeautifulSoup(source, "lxml")

    new_prd_nm = soup.select_one(".cdtl_info_tit")
    new_sales_price = soup.select_one(".ssg_price")

    if kind == "update" and (not new_prd_nm or not new_sales_price):
        app.logger.info(f"product no longer available: {org_url}")
        changed["has_stock"] = "404"
        return changed

    elif kind == "update" and (new_prd_nm or new_sales_price):
        return

    else:

        if new_prd_nm:
            new_prd_nm = new_prd_nm.text

            if new_prd_nm.replace(" ", "") != prd.prd_nm.replace(" ", ""):
                isChanged = True
                prd.prd_nm = new_prd_nm
                app.logger.info(f"{prd.id}: named changed")

        isTempSoldOut = soup.select(".cdtl_disabled")
        isSoldOut = soup.select(".cdtl_btn_soldout")

        if (isTempSoldOut or isSoldOut) and prd.has_stock == 1:
            isChanged = True
            prd.has_stock = 0
            app.logger.info(f"{prd.id}: out of stock")
        elif (not isTempSoldOut and not isSoldOut) and prd.has_stock == 0:
            isChanged = True
            prd.has_stock = 1
            app.logger.info(f"{prd.id}: in stock")

        if new_sales_price:

            try:
                new_sales_price = int(
                    new_sales_price.text.replace(",", "")
                    .replace("원", "")
                    .replace(" ", "")
                )
            except Exception as e:
                raise (e)

            if new_sales_price != prd.sales_price:
                isChanged = True
                prd.sales_price = new_sales_price
                app.logger.info(f"{prd.id}: price changed - {new_sales_price}")

        if isChanged:
            changed["prd"] = prd
            return changed
