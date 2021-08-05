from bs4 import BeautifulSoup
import requests
import re
from random import choice

import concurrent.futures


from app.helpers.gMarket.urlNRate import urlNRate


def itemExtractor(url):

    uas = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    ]

    ua = choice(uas)

    headers = {
        "User-Agent": ua,
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        # extract all items on the page
        soup = BeautifulSoup(res.text, "lxml")
        box_infos = soup.select(".box__information")

        if box_infos:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = []
                for box in box_infos:
                    results.append(executor.submit(urlNRate, box))

                return_val = []
                for f in concurrent.futures.as_completed(results):
                    if f.result():
                        return_val.append(f.result())

            return return_val
        else:
            print("here")
            return None

    except requests.exceptions.RequestException as e:
        if res.status_code == 401:
            raise (e)
        elif res.status_code == 404:
            return
        else:
            raise (e)
    except Exception as e:
        raise (e)
