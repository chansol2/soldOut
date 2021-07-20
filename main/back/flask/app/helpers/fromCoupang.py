import requests
from app import db
from app import app
from bs4 import BeautifulSoup


def fromCoupang(prd, kind):

    org_url = prd.org_url

    isChanged = False

    changed = {"prd": prd}

    headers = {
        "Host": "www.coupang.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
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

    new_prd_nm = soup.select_one(".prod-buy-header__title")

    if kind == "update" and not new_prd_nm:
        app.logger.info(f"product no longer available: {org_url}")
        changed["has_stock"] = "404"
        return changed

    elif kind == "update" and new_prd_nm:
        return

    else:

        if new_prd_nm:
            new_prd_nm = new_prd_nm.text

            if new_prd_nm.replace(" ", "") != prd.prd_nm.replace(" ", ""):
                prd.prd_nm = new_prd_nm
                isChanged = True
                app.logger.info(f"{prd.id}: named changed")

        if soup.select_one(".oos-label") and prd.has_stock == 1:
            prd.has_stock = 0
            isChanged = True
            app.logger.info(f"{prd.id}: out of stock")
        elif not soup.select_one(".oos-label") and prd.has_stock == 0:
            prd.has_stock = 1
            isChanged = True
            app.logger.info(f"{prd.id}: in stock")

        new_sales_price = soup.select_one(".prod-major-price > .total-price > strong")

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
                prd.sales_price = new_sales_price
                isChanged = True
                app.logger.info(f"{prd.id}: price changed - {new_sales_price}")

        if isChanged:
            changed["prd"] = prd
            return changed
