import requests
from app import db
from bs4 import BeautifulSoup


def fromOHouse(prd, kind):

    org_url = prd.org_url

    isChanged = False

    changed = {"prd": prd}

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
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

    new_prd_nm = soup.select_one(".production-selling-header__title__name")

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

        new_sales_price = soup.select(
            ".production-selling-header__price__price .number"
        )

        if new_sales_price:
            notInStock = soup.select_one(
                ".production-selling-option-form__footer__sold-out"
            )
            if notInStock and prd.has_stock == 1:
                prd.has_stock = 0
                isChanged = True
                app.logger.info(f"{prd.id}: out of stock")
            elif not notInStock and prd.has_stock == 0:
                prd.has_stock = 1
                isChanged = True
                app.logger.info(f"{prd.id}: in stock")
            elif notInStock and prd.has_stock == 0:
                pass
            else:
                try:
                    new_sales_price = int(
                        new_sales_price[0]
                        .text.replace(",", "")
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
