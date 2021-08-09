import re
from random import choice
from aiohttp import ClientSession
import asyncio


async def responseExtractor(url, sem):

    uas = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    ]

    ua = choice(uas)

    headers = {
        "Connection": "Upgrade",
        "Upgrade": "http/1.1",
        "User-Agent": ua,
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
    }
    try:
        print("here")
        async with sem:
            async with ClientSession() as session:
                async with session.get(
                    url, headers=headers, raise_for_status=True
                ) as res:
                    return await res.text()

    except asyncio.exceptions.TimeoutError:
        pass

    except Exception as e:
        print(e)
