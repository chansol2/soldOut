from app.helpers.gMarket.responseExtractor import responseExtractor
from app.helpers.gMarket.urlNInfos import urlNInfos
from bs4 import BeautifulSoup


async def itemsExtractor(url, sem):
    try:

        res = await responseExtractor(url, sem)
        if res:
            print("here2")
            # extract all items on the page
            soup = BeautifulSoup(res, "lxml")
            box_infos = soup.select(".box__information")

            if box_infos:
                results = []
                for box in box_infos:
                    results.append(urlNInfos(box))
                return results
            else:
                return
        else:
            return

    except Exception as e:
        print(e)
