from app.helpers.gMarket.findLastPage import findLastPage
from app.helpers.gMarket.gatherItems import gatherItems
from app.helpers.gMarket.gatherProducts import gatherProducts
from app.helpers.gMarket.preprocessDF import preprocessDF

import asyncio
import ast
import time


def bedNHead():

    t0 = time.time()

    org_url = "https://browse.gmarket.co.kr/list?category=200000702&k=20&p="

    # find the last page_num
    # lastPageNum = findLastPage(org_url)

    # gather all items in the category e.g. [[(url,rate),...]...]

    # pages = asyncio.run(gatherItems(org_url, lastPageNum))

    # with open("temp.txt", "w") as f:
    #     f.write(str(pages))

    with open("temp.txt", "r") as f:
        for line in f:
            pages = ast.literal_eval(line)

    # time to parse, returns a list of product objects

    products = asyncio.run(gatherProducts(pages))

    t1 = time.time()

    print(f"elasped time: {t1-t0}")

    with open("temp3.txt", "w") as f1:
        f1.write(str(products))

    products = [x for x in products if x]

    # make a df and preprocess it

    # preprocessDF(products)
