import concurrent.futures
import time
from random import randrange

from app.helpers.fromCoupang import fromCoupang
from app.helpers.fromGMarket import fromGMarket
from app.helpers.fromOHouse import fromOHouse
from app.helpers.fromOneRoom import fromOneRoom
from app.helpers.fromSSG import fromSSG
from app.helpers.fromTenByTen import fromTenByTen

from app.models.products import ProductsModel

from flask_restful import Resource


class Update(Resource):
    def get(self):
        ##possible use of multithreading
        # all_prds = ProductsModel.query.all()
        ssg = ProductsModel.query.filter_by(seller_id=15).all()

        rest = ProductsModel.query.filter(ProductsModel.seller_id != 15).all()

        all_prds = ssg + rest

        prds = [(prd.seller_id, prd) for prd in all_prds]

        # try:

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = []

            for seller_id, prd in prds:
                if seller_id == 15:
                    t = randrange(3, 6)
                    time.sleep(t)
                    results.append(executor.submit(fromSSG, prd))
                elif seller_id == 12:
                    results.append(executor.submit(fromGMarket, prd))
                elif seller_id == 11:
                    results.append(executor.submit(fromCoupang, prd))
                elif seller_id == 13:
                    results.append(executor.submit(fromOHouse, prd))
                elif seller_id == 14:
                    results.append(executor.submit(fromOneRoom, prd))
                elif seller_id == 16:
                    results.append(executor.submit(fromTenByTen, prd))
                else:
                    print(f"wrong seller: {prd}")

            needs_update = []
            i = 0
            for f in concurrent.futures.as_completed(results):
                if f.result():
                    needs_update.append({"id": i, "data": f.result()})
                    i += 1

            # i = 0
            # for prd in ssg:
            #     needs_update.append({"id": i, "data": fromSSG(prd)})
            #     i += 1

            return needs_update, 200


# except:
#     return 500
