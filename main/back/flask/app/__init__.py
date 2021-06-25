from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_jwt import JWT
from flask_cors import CORS

from app.security import authenticate, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soldOut.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
jwt = JWT(app, authenticate, identity)
CORS(app)

app.secret_key = 'jose'

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)


from app.resources.update import Update

api.add_resource(Update, '/update')
