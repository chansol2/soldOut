from app import db


class TestModel(db.Model):
    __table__ = db.Model.metadata.tables["products"]

    def __repr__(self):
        return self.DISTRICT
