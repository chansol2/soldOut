from bs4 import BeautifulSoup
import requests


def fromGMarket(prd):
    isChanged = False
    changed = {
        "prd_id" : prd['prd_id'],
        "seller_nm": "지마켓"
    }

    org_url = prd['org_url']

    try:
        res = requests.get(org_url)
        if res.status_code==404:
            print("404 page not found")
            changed['org_url'] = "404"
            return changed
        else:
            source = res.text

    except:
        print(res.status_code)
        return

    soup = BeautifulSoup(source, 'lxml')


    new_prd_nm = soup.select_one(".itemtit").text

    if new_prd_nm.replace(" ", "") != prd['prd_nm'].replace(" ", ""):
        isChanged = True
        # old = prd['prd_nm']
        # print(f'new: {new_prd_nm}, old: {old}')
        changed['prd_nm'] = new_prd_nm
    
    inStock = soup.select_one("strong.price_real").text
    

    if inStock == "일시품절":
        isChanged = True
        # print(f'{inStock}: {org_url}')
        changed['has_stock'] = False
        return changed

    new_sales_price = inStock[0:-1]

    if new_sales_price != prd['sales_price']:
        isChanged = True
        # old = prd['sales_price']
        # print(f'new: {new_sales_price}, old: {old}')
        changed['sales_price'] = new_sales_price

    if isChanged:
        return changed