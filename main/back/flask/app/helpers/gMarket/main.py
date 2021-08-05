from app.helpers.gMarket.bedNHead import bedNHead


def gMarketMain(category):
    try:
        if category == "bedNHead":
            bedNHead()

    except Exception as e:
        raise e
