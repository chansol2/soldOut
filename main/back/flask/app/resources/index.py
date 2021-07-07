from app.models.products import ProductsModel
from app.models.cate_info import CategoryModel
from app.models.seller_info import SellerModel
from app.models.coupang import CoupangModel
from app.models.gMarket import GMarketModel
from app.models.oHouse import OHouseModel
from app.models.oneRoom import OneRoomModel
from app.models.ssg import SSGModel
from app.models.tenByTen import TenByTenModel
from flask_restful import Resource
from app import db


class Index(Resource):
    def get(self):
        # cate = CategoryModel(10101, "일반침대", None, None)
        # seller = SellerModel(11, "coupang", "https://coupang.com/")
        # test = ProductsModel(
        #     cate_id=10101,
        #     prd_nm="동익가구",
        #     org_url="https://google.com",
        #     img_url="https://google.com",
        #     rate_cnt=0,
        #     rate_val=0,
        #     sales_price=1000,
        #     has_stock=True,
        # )
        # db.session.add(cate)
        # db.session.add(seller)
        # db.session.add(test)
        # db.session.commit()

        return 200
