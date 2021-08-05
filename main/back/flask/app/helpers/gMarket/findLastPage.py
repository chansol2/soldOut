from bs4 import BeautifulSoup
import requests


def findLastPage(org_url):

    # find total num of items

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    res = requests.get(org_url + str(1), headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    total_item_num = soup.select_one(".text__item-count")

    if total_item_num:
        total_item_num = int(total_item_num.text.replace(",", "").replace(" ", ""))
    else:
        raise Exception("sth wrong")

    approx_page = total_item_num // 90

    res = requests.get(org_url + str(approx_page), headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    last_page_num = soup.select(".link__page")

    last_page_num = soup.select(".link__page")[-2]["data-montelena-pageno"]

    return int(last_page_num)
