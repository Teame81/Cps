import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from secretkeys import DBinfo
from flask_restful import Resource, Api


# Making the essentals objects
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)

# DC Setup, connection
DBuser = "teame81"
DBpassword = "aik123aik"
DBname = "cps"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{DBuser}:{DBpassword}@teame81.mysql.pythonanywhere-services.com/{DBname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

#db.create_all()