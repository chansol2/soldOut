import concurrent.futures
import time
from random import randrange
from flask_mail import Message

from app import db
from app import app
from app import mail
from app.helpers.fromCoupang import fromCoupang
from app.helpers.fromGMarket import fromGMarket
from app.helpers.fromOHouse import fromOHouse
from app.helpers.fromOneRoom import fromOneRoom
from app.helpers.fromSSG import fromSSG
from app.helpers.fromTenByTen import fromTenByTen
from app.models.products import ProductModel
from flask_restful import Resource


class Cron(Resource):
    def get(self):

        try:

            ssg = ProductModel.query.filter_by(seller_id=15).all()

            rest = ProductModel.query.filter(ProductModel.seller_id != 15).all()

            all_prds = ssg + rest

            prds = [(prd.seller_id, prd) for prd in all_prds]

            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = []

                for seller_id, prd in prds:
                    if seller_id == 15:
                        t = randrange(3, 6)
                        time.sleep(t)
                        results.append(executor.submit(fromSSG, prd, "cron"))
                    elif seller_id == 11:
                        results.append(executor.submit(fromCoupang, prd, "cron"))
                    elif seller_id == 12:
                        results.append(executor.submit(fromGMarket, prd, "cron"))
                    elif seller_id == 13:
                        results.append(executor.submit(fromOHouse, prd, "cron"))
                    elif seller_id == 14:
                        results.append(executor.submit(fromOneRoom, prd, "cron"))
                    elif seller_id == 16:
                        results.append(executor.submit(fromTenByTen, prd, "cron"))
                    else:
                        app.logger.info(f"wrong seller: {prd}")

                needs_update = []
                for f in concurrent.futures.as_completed(results):
                    if f.result():
                        needs_update.append(f.result())

            for item in needs_update:
                prd = item["prd"]
                try:
                    db.session.add(prd)
                except Exception as e:
                    app.logger.info(e)

            db.session.commit()
            app.logger.info("it's been committed successfully")
        except Exception as e:
            app.logger.info("500")
            app.logger.info(e)
            raise e
            msg = Message(
                "admin",
                sender="fordifferencekr@gmail.com",
                recipients=["fordifferencekr@gmail.com"],
            )

            msg.body = str(e)
            mail.connect()
            mail.send(msg)
            return {"message": str(e)}, 500
        else:
            app.logger.info("it's successful:200")
            msg = Message(
                "admin",
                sender="fordifferencekr@gmail.com",
                recipients=["fordifferencekr@gmail.com"],
            )

            msg.body = "cronjob has been done successfully"
            mail.connect()
            mail.send(msg)
            return {"message": "it's successful"}, 200
