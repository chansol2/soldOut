from app.helpers.gMarket.itemsExtractor import itemsExtractor

import asyncio


async def gatherItems(url, lastPageNum):

    tasks = []
    sem = asyncio.Semaphore(10)
    for i in range(1, lastPageNum + 1):
        tasks.append(asyncio.create_task(itemsExtractor(url + str(i), sem)))

    return await asyncio.gather(*tasks)
