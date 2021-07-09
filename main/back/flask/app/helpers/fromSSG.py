from bs4 import BeautifulSoup
import requests
import time
from random import randrange, choice
from requests.auth import HTTPBasicAuth


uas = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
]


def fromSSG(prd):
    isChanged = False
    changed = {"prd_id": prd.org_id, "seller_nm": "SSG"}

    org_url = prd.org_url

    ua = choice(uas)

    headers = {
        "User-Agent": ua,
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
    }
    try:
        res = requests.get(org_url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"{res.status_code} error")
    except Exception as e:
        if res.status_code == 401:
            print(f"redo {org_url}")
            time.sleep(120)
            return fromSSG(prd)
        elif res.status_code == 404:
            changed["org_url"] = "404"
            return changed
        else:
            print(e)

    else:
        source = res.text
        soup = BeautifulSoup(source, "lxml")

        new_prd_nm = soup.select_one(".cdtl_info_tit")

        if new_prd_nm:
            new_prd_nm = new_prd_nm.text

            if new_prd_nm.replace(" ", "") != prd.prd_nm.replace(" ", ""):
                isChanged = True
                # old = prd["prd_nm"]
                # print(f"new: {new_prd_nm}, old: {old}")
                changed["prd_nm"] = new_prd_nm
        else:
            isChanged = True
            print(f"product no longer available: {org_url}")
            changed["org_url"] = "404"
            return changed

        isTempSoldOut = soup.select(".cdtl_disabled")
        isSoldOut = soup.select(".cdtl_btn_soldout")

        if isTempSoldOut or isSoldOut:
            isChanged = True
            print(f"Not in stock: {org_url} 품절")
            changed["has_stock"] = False
            return changed

        new_sales_price = soup.select_one(".ssg_price")

        if new_sales_price:
            new_sales_price = new_sales_price.text

            if new_sales_price != prd.sales_price:
                isChanged = True
                # old = prd["sales_price"]
                # print(f"new: {new_sales_price}, old: {old}")
                changed["sales_price"] = new_sales_price
        else:
            isChanged = True
            print("product no longer available")
            changed["org_url"] = "404"
            return changed

        if isChanged:
            return changed
