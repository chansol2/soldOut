import concurrent.futures

from app.helpers.gMarket.main import gMarketMain

from flask_restful import Resource


class Update(Resource):
    def get(self):
        try:
            categories = ["bedNHead"]
            # crawl each category from websites
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = []
                # loop through each category
                for category in categories:
                    results.append(executor.submit(gMarketMain, category))
                    # possibly other websites

            return 200
        except Exception as e:
            print(e)
