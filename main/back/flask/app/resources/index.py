# from app.models.products import ProductsModel
# from app.models.cate_info import CategoryModel
# from app.models.seller_info import SellerModel
# from app.models.coupang import CoupangModel
# from app.models.gMarket import GMarketModel
# from app.models.oHouse import OHouseModel
# from app.models.oneRoom import OneRoomModel
# from app.models.ssg import SSGModel
# from app.models.tenByTen import TenByTenModel
from app.models.products import ProductModel
from flask_restful import Resource
from app import db
from app import app


class Index(Resource):
    def get(self):
        app.logger.info("index:here")
        ssg = ProductModel.query.filter_by(seller_id=15).first().json()
        return ssg, 200
