from app import db


class ProductModel(db.Model):
    __table__ = db.Model.metadata.tables["products"]

    def json(self):
        return {
            "cate_id": self.cate_id,
            "prd_nm": self.prd_nm,
            "img_url": self.img_url,
            "org_url": self.org_url,
            "rate_cnt": self.rate_cnt,
            "rate_val": self.rate_val,
            "sales_price": self.sales_price,
            "has_stock": self.has_stock,
            "org_id": self.org_id,
            "seller_id": self.seller_id,
            "is_delete": self.is_delete,
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
