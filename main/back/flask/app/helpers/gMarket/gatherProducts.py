import asyncio

from app.helpers.gMarket.parseProduct import parseProduct


async def gatherProducts(pages):

    items = []
    for page in pages:
        if page:
            items.extend(page)

    tasks = []
    sem = asyncio.Semaphore(10000)

    for item in items:
        if item:
            tasks.append(asyncio.create_task(parseProduct(item, sem)))
    return await asyncio.gather(*tasks)
