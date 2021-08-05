from app.helpers.gMarket.findLastPage import findLastPage
from app.helpers.gMarket.itemExtractor import itemExtractor
import concurrent.futures
import time
from random import uniform


def bedNHead():
    org_url = "https://browse.gmarket.co.kr/list?category=200000702&k=20&p="

    # find the last page_num
    lastPageNum = findLastPage(org_url)

    # gather all items in the category
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = []

            for i in range(1, lastPageNum + 1):
                # t = uniform(0.1, 1.1)
                # time.sleep(t)
                results.append(executor.submit(itemExtractor, org_url + str(i)))

            ready_to_parse = []
            i = 0
            for f in concurrent.futures.as_completed(results):
                if f.result():
                    i += 100
                    print(i)
                    ready_to_parse.extend(f.result())
                else:
                    print(f.result())
                    print("here1")

            print(len(ready_to_parse))
    except Exception as e:
        raise e

    # time to parse

    # with concurrent.futures.ThreadPoolExecutor() as executor:
