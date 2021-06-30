from app import db

from app.tables import Prd11, Prd12, Prd13, Prd14, Prd15, Prd16


def getProducts():
    # initialize all product tables mapped by seller_id
    coupang = db.session.query(Prd11).all()
    gMarket = db.session.query(Prd12).all()
    oHouse = db.session.query(Prd13).all()
    oneRoom = db.session.query(Prd14).all()
    ssg = db.session.query(Prd15).all()
    tenByTen = db.session.query(Prd16).all()

    # concat all result arrays into one results array

    results = ssg + coupang + gMarket + oHouse + oneRoom + tenByTen
    return results
