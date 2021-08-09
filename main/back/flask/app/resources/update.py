from app.helpers.gMarket.main import gMarketMain

from flask_restful import Resource


class Update(Resource):
    def get(self):
        try:
            categories = ["bedNHead"]
            # crawl each category from websites
            # loop through each category
            for category in categories:
                gMarketMain(category)
                # possibly other websites

            return 200

        except Exception as e:
            print(e)
