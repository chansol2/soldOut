import re


def urlNRate(item):
    try:
        item_url = item.select_one("a.link__item")["href"]
        org_rate = item.select_one(".list__score span.for-a11y")

        if org_rate:
            org_rate = org_rate.text
            if org_rate != "건":
                rate = int(re.findall(r"(\d+)%", org_rate)[0])
            else:
                rate = 0
        else:
            rate = 0
    except Exception as e:
        raise e

    return (item_url, rate)
