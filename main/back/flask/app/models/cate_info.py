from app import db


class CategoryModel(db.Model):

    __tablename__ = "cate_info"

    cate_id = db.Column(db.BigInteger, primary_key=True)
    cate_nm = db.Column(db.String(150))
    parent_id = db.Column(db.Integer)
    sub_parent_id = db.Column(db.Integer)

    products = db.relationship("ProductsModel")

    def __init__(self, cate_id, cate_nm, parent_id, sub_parent_id):
        self.cate_id = cate_id
        self.cate_nm = cate_nm
        self.parent_id = parent_id
        self.sub_parent_id = sub_parent_id
