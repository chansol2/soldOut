from app import db

from app.models.coupang import CoupangModel
from app.models.gMarket import GMarketModel
from app.models.oHouse import OHouseModel
from app.models.oneRoom import OneRoomModel
from app.models.ssg import SSGModel
from app.models.tenByTen import TenByTenModel


def getProducts():
    # initialize all product tables mapped by seller_id
    coupang = CoupangModel.query.all()
    gMarket = GMarketModel.query.all()
    oHouse = OHouseModel.query.all()
    oneRoom = OneRoomModel.query.all()
    ssg = SSGModel.query.all()
    tenByTen = TenByTenModel.query.all()

    # concat all result arrays into one results array

    results = ssg + coupang + gMarket + oHouse + oneRoom + tenByTen
    return results
