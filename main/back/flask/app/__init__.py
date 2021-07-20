from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# from sqlalchemy.ext.automap import automap_base
from flask_jwt import JWT
from flask_cors import CORS

from app.security import authenticate, identity


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://admin:Nineso20!$@3.37.93.239/products_test"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "jose"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "fordifferencekr@gmail.com"
app.config["MAIL_PASSWORD"] = "nineso123"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)

api = Api(app)
jwt = JWT(app, authenticate, identity)
CORS(app, resources={r"/*": {"origins": "*"}})


db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

from app.resources.index import Index
from app.resources.update import Update
from app.resources.cron import Cron

api.add_resource(Index, "/index")
api.add_resource(Update, "/update")
api.add_resource(Cron, "/cron")
