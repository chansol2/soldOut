from flask_restful import Resource
import concurrent.futures
import time
from random import randrange

from app.helpers.row2dict import row2dict
from app.helpers.getProducts import getProducts
from app.helpers.fromGMarket import fromGMarket
from app.helpers.fromCoupang import fromCoupang
from app.helpers.fromOHouse import fromOHouse
from app.helpers.fromOneRoom import fromOneRoom

from app.helpers.fromSSG import fromSSG
from app.helpers.fromTenByTen import fromTenByTen

from app import db


class Update(Resource):
    def get(self):
        ##possible use of multithreading
        results = getProducts()
        prds = [(row2dict(r)["seller_nm"], row2dict(r)) for r in results]

        # try:

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = []

            for seller_nm, prd in prds:
                if seller_nm == "SSG":
                    t = randrange(3, 6)
                    time.sleep(t)
                    results.append(executor.submit(fromSSG, prd))
                elif seller_nm == "지마켓":
                    results.append(executor.submit(fromGMarket, prd))
                elif seller_nm == "쿠팡":
                    results.append(executor.submit(fromCoupang, prd))
                elif seller_nm == "오늘의집":
                    results.append(executor.submit(fromOHouse, prd))
                elif seller_nm == "원룸만들기":
                    results.append(executor.submit(fromOneRoom, prd))
                elif seller_nm == "10x10":
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
