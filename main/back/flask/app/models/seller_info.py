from app import db
import datetime


class SellerModel(db.Model):

    __tablename__ = "seller_info"

    seller_id = db.Column(db.Integer, primary_key=True)
    seller_nm = db.Column(db.String(150))
    seller_url = db.Column(db.String(500))

    products = db.relationship("ProductsModel")

    def __init__(self, seller_id, seller_nm, seller_url):
        self.seller_id = seller_id
        self.seller_nm = seller_nm
        self.seller_url = seller_url
