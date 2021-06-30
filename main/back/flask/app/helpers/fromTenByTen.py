from bs4 import BeautifulSoup
import requests
import time


def fromTenByTen(prd):
    isChanged = False
    changed = {"prd_id": prd["prd_id"], "seller_nm": "10x10"}

    org_url = prd["org_url"]

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    }

    try:
        res = requests.get(org_url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"{res.status_code} error")
    except Exception as e:
        if res.status_code == 401:
            time.sleep(120)
            print(f"redo {org_url}")
            return fromTenByTen(prd)
        elif res.status_code == 404:
            changed["org_url"] = "404"
            return changed
        else:
            print(e)

    else:
        source = res.text
        soup = BeautifulSoup(source, "lxml")

        new_prd_nm = soup.select_one(".pdtBasicV15 .pdtName")

        if new_prd_nm:
            new_prd_nm = new_prd_nm.text

            if new_prd_nm.replace(" ", "") != prd["prd_nm"].replace(" ", ""):
                isChanged = True
                # old = prd["prd_nm"]
                # print(f"new: {new_prd_nm}, old: {old}")
                changed["prd_nm"] = new_prd_nm
        else:
            isChanged = True
            print("product no longer available")
            changed["org_url"] = "404"
            return changed

        temp = soup.select(".btnArea a.btn-stock")

        if temp:
            isChanged = True
            print(f"Not in stock: {org_url} 품절")
            changed["has_stock"] = False
            return changed

        new_sales_price = soup.select_one("strong.cRd0V15")

        if new_sales_price:
            new_sales_price = new_sales_price.text.strip().split("원")[0]

            if new_sales_price != prd["sales_price"]:
                isChanged = True
                # old = prd["sales_price"]
                # print(f"new: {new_sales_price}, old: {old}")
                changed["sales_price"] = new_sales_price
        else:
            org_price = soup.select_one(".cBk0V15")
            if org_price:
                new_sales_price = org_price.text[0:-1]
            else:
                isChanged = True
                print("product no longer available")
                changed["org_url"] = "404"
                return changed

        if isChanged:
            return changed
