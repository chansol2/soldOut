from app import db
import datetime


class OneRoomModel(db.Model):

    __tablename__ = "prd_14"

    id = db.Column(db.BigInteger, primary_key=True)
    cate_id = db.Column(db.BigInteger, db.ForeignKey("cate_info.cate_id"))
    prd_nm = db.Column(db.String(150))
    org_url = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
    rate_cnt = db.Column(db.String(150))
    rate_val = db.Column(db.String(150))
    sales_price = db.Column(db.String(150))
    has_stock = db.Column(db.Boolean)
    org_id = db.Column(db.BigInteger)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller_info.seller_id"))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    cate = db.relationship("CategoryModel")
    seller = db.relationship("SellerModel")

    def __init__(
        self,
        cate_id,
        prd_nm,
        org_url,
        img_url,
        rate_cnt,
        rate_val,
        sales_price,
        has_stock,
        org_id,
        seller_id,
    ):
        self.cate_id = cate_id
        self.prd_nm = prd_nm
        self.org_url = org_url
        self.img_url = img_url
        self.rate_cnt = rate_cnt
        self.rate_val = rate_val
        self.sales_price = sales_price
        self.has_stock = has_stock
        self.org_id = org_id
        self.seller_id = seller_id

    def json(self):
        return {
            "cate_id": self.cate_id,
            "prd_nm": self.prd_nm,
            "org_url": self.org_url,
            "img_url": self.img_url,
            "rate_cnt": self.rate_cnt,
            "rate_val": self.rate_val,
            "sales_price": self.sales_price,
            "has_stock": self.has_stock,
            "org_id": self.org_id,
            "seller_id": self.seller_id,
        }
