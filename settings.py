import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secretkeys import DBinfo
from flask_restful import Resource, Api


# Making the essentals objects
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)

# DC Setup, connection
DBuser = DBinfo["Username"]
DBpassword = DBinfo["Password"]
DBname = DBinfo["Database"]
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DBuser}:{DBpassword}@localhost:5432/{DBname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

db.create_all()