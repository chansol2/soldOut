import re


def urlNInfos(box):
    try:
        print("here4")
        item_url = box.select_one("a.link__item")
        if item_url:
            item_url = item_url["href"]
        else:
            return

        org_rate = box.select_one(".list__score span.for-a11y")

        if org_rate:
            org_rate = org_rate.text
            if org_rate != "건" or org_rate != "상품평":
                temp = re.findall(r"(\d+)%", org_rate)
                if temp:
                    rate_val = int(temp[0]) / 20
                else:
                    with open("error.txt", "w") as f:
                        f.write(org_rate)
                    rate_val = 0.0
            else:
                rate_val = 0.0
        else:
            rate_val = 0.0

        rate_cnt = box.select_one(".list-item.list-item__feedback-count .text")
        if rate_cnt:
            rate_cnt = rate_cnt.text
            temp = re.findall(r"(\d+)", rate_cnt)
            if temp:
                rate_cnt = int(temp[0].replace(",", "").replace(" ", ""))
        else:
            rate_cnt = 0

        delivery_method = box.select_one("span.text__tag")

        if delivery_method:
            delivery_method = delivery_method.text
        else:
            delivery_method: "N/A"

    except Exception as e:
        print(e)
        return

    else:
        print("just returned")
        return {
            "item_url": item_url,
            "rate_val": rate_val,
            "rate_cnt": rate_cnt,
            "delivery_method": delivery_method,
        }
