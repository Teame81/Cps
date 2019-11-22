import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__)) # __file__ is the name of this file = dbModel.py -- os.path.dirname = c:\dev\flask\cps

######################## INITIATE DATABASE ########################
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

######################## DATA BASE MODELS ########################

class localDb(db.Model):
    __tablename__ = 'local' # Manual override table name / if not used it will use class name
    id = db.Column(db.Integer,primary_key=True)
    local_id = db.Column(db.Text)

    def __init__ (self, local_id):
        self.local_id = local_id

    def __repr__(self):
        return f"Lokal Id: {self.local_id}"
    
