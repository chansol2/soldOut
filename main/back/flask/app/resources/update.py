from flask_restful import Resource
import concurrent.futures

from app.helpers.row2dict import row2dict
from app.helpers.getProducts import getProducts
from app.helpers.fromGMarket import fromGMarket
from app.tables import Prd12

from app import db

class Update(Resource):
    def get(self):
        ##possible use of multithreading
        results = getProducts()
        prds = [(row2dict(r)['seller_nm'], row2dict(r)) for r in results]

        try:

            with concurrent.futures.ProcessPoolExecutor() as executor:
                results = []
                for seller_nm, prd in prds:
                    if seller_nm == "지마켓":
                        results.append(executor.submit(fromGMarket, prd))
                needs_update = []
                i=0
                for f in concurrent.futures.as_completed(results):
                    if f.result():
                        needs_update.append({
                            "id": i,
                            "data": f.result()
                        })
                        i += 1

            return needs_update, 200
        
        except:
            return 500