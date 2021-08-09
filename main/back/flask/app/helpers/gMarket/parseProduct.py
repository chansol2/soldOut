from bs4 import BeautifulSoup

from app.helpers.gMarket.responseExtractor import responseExtractor


async def parseProduct(item, sem):
    try:
        url = item["item_url"]

        if url:

            res = await responseExtractor(url, sem)
            if res:
                print("here2")
                # extract all infos on the product detail page
                soup = BeautifulSoup(res, "lxml")

                ## name

                prd_nm = soup.select_one(".itemtit")

                if prd_nm:
                    prd_nm = prd_nm.text
                else:
                    # raise ValueError("prd_nm does not exist")
                    return

                ## has_stock and sales_price

                inStock = soup.select_one("strong.price_real")

                if inStock:
                    if "품절" in inStock.text:
                        has_stock = 0
                        sales_price = 0
                    else:
                        sales_price = int(
                            inStock.text.replace(",", "")
                            .replace("원", "")
                            .replace(" ", "")
                        )
                        has_stock = 1

                else:
                    # raise ValueError("sth wrong")
                    return

                ## original price
                org_price = soup.select_one(".price_original")
                if org_price:
                    org_price = int(
                        org_price.text.replace(",", "")
                        .replace("원", "")
                        .replace(" ", "")
                    )
                    print(org_price)
                else:
                    org_price = 0

                ##img_url

                img_url = soup.select_one(".box__viewer-container img")

                if img_url:
                    img_url = img_url["src"]
                    print(img_url)
                else:
                    return

                ## org_id, color, material, KC_Auth

                table = soup.select(".box__product-notice-list tbody tr")

                color = ""

                material = ""

                KC_Auth = ""

                for item in table:

                    if item.select_one("th"):
                        if item.select_one("th").text == "상품번호":
                            if item.select_one("td"):
                                org_id = item.select_one("td").text
                            else:
                                raise ValueError("org_id does not exist")
                        elif item.select_one("th").text == "색상":
                            if item.select_one("td"):
                                color = item.select_one("td").text
                        elif item.select_one("th").text == "주요소재":
                            if item.select_one("td"):
                                material = item.select_one("td").text
                        elif "KC" in item.select_one("th").text:
                            if item.select_one("td"):
                                KC_Auth = item.select_one("td").text
                        else:
                            pass

                if item.delivery_method:
                    delivery_method = item["delivery_method"]
                else:
                    delivery_method = "N/A"

                if item.rate_val:
                    rate_val = item["rate_val"]
                else:
                    rate_val = 0.0

                if item.rate_cnt:
                    rate_cnt = item["rate_cnt"]
                else:
                    rate_cnt = 0

                return {
                    "prd_nm": prd_nm,
                    "delivery_method": delivery_method,
                    "sales_price": sales_price,
                    "org_price": org_price,
                    "img_url": img_url,
                    "org_url": url,
                    "org_id": org_id,
                    "rate_val": rate_val,
                    "rate_cnt": rate_cnt,
                    "has_stock": has_stock,
                    "color": color,
                    "material": material,
                    "KC_Auth": KC_Auth,
                }

            else:
                return

    except Exception as e:
        print(e)
