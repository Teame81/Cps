import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__)) # __file__ is the name of this file = dbModel.py -- os.path.dirname = c:\dev\flask\cps

######################## INITIATE DATABASE ########################
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aik123@localhost:5432/cps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

Migrate(app, db)

######################## DATA BASE MODELS ########################

#-------------PREMISES START-------------#
class A_premises(db.Model):
    # Manual override table name / if not used it will use class name.
    __tablename__ = 'premises'
    id = db.Column(db.Integer,primary_key=True)
    # premises id.
    premises_id = db.Column(db.String(50))
    # This could company name or more.
    short_description = db.Column(db.String(120))
    # One premises can have several devices.
        # ex: column_name = db.relationship('Class to make relationship to', backref = 'this table name')
    devices = db.relationship('Device', backref = 'A_premises', lazy = 'dynamic')
        
   # Initate data into the premises table
    def __init__ (self, premises_id, short_description, devices):
        self.premises_id = premises_id
        self.short_description = short_description
        self.devices = devices


    def __repr__(self):
        if self.devices:
            print(f"---Start---")
            for device in self.devices:
                print(f"{device} is present in {self.premises_id}")
            return f"---End---"
        else:
            return f"Premises have no device(s) yet."
#-------------PREMISES END-------------#


#-------------DEVICES START-------------#
class Device(db.Model):
    __tablename__ = 'devices'
    device_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, db.ForeignKey('premises.id'))
    visitors = db.relationship('Click' , backref = 'devices', lazy = 'dynamic')
    def __init__(self,device_id, position):
        self.device_id = device_id
        self.position = position
        
    def __repr__(self):
        pass
#-------------DEVICES END-------------#

#-------------CLICKS START-------------#
class Click(db.Model):
    __tablename__ = 'clicks'
    id = db.Column(db.Integer, primary_key=True)
    pass_through = db.Column(db.Integer, db.ForeignKey('devices.device_id'))
    
    def __init__(self, pass_through):
        self.pass_through = pass_through
    
    def __repr__(self):
        pass

#-------------CLICKS START-------------#