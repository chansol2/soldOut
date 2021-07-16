from bs4 import BeautifulSoup
import requests
import time


def fromCoupang(prd):
    isChanged = False
    changed = {"prd_id": prd.org_id, "seller_nm": "쿠팡"}

    org_url = prd.org_url

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
        if res.status_code != 200:
            raise Exception(f"{res.status_code} error")
    except Exception as e:
        if res.status_code == 401:
            time.sleep(120)
            print(f"redo {org_url}")
            return fromCoupang(prd)
        elif res.status_code == 404:
            changed["org_url"] = "404"
            return changed
        else:
            print(e)
    else:
        source = res.text
        soup = BeautifulSoup(source, "lxml")

        new_prd_nm = soup.select_one(".prod-buy-header__title")

        if new_prd_nm:
            new_prd_nm = new_prd_nm.text

            if new_prd_nm.replace(" ", "") != prd.prd_nm.replace(" ", ""):
                isChanged = True
                # old = prd['prd_nm']
                # print(f'new: {new_prd_nm}, old: {old}')
                changed["prd_nm"] = new_prd_nm
        else:
            isChanged = True
            print(f"product no longer available: {org_url}")
            changed["org_url"] = "404"
            return changed

        if soup.select_one(".total-price > strong"):
            if soup.select_one(".oos-label"):
                isChanged = True
                print(f"Not in stock: {org_url} 일시품절")
                changed["has_stock"] = False
                return changed
            else:
                new_sales_price = soup.select_one(".total-price > strong")

                if new_sales_price:
                    new_sales_price = new_sales_price.text

                    if new_sales_price != prd.sales_price:
                        isChanged = True
                        # old = prd["sales_price"]
                        # print(f"new: {new_sales_price}, old: {old}")
                        changed["sales_price"] = new_sales_price

        else:
            isChanged = True
            print(f"Not in stock: {org_url} 품절")
            changed["has_stock"] = False
            return changed

        if isChanged:
            return changed
