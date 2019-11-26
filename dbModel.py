import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__)) # __file__ is the name of this file = dbModel.py -- os.path.dirname = c:\dev\flask\cps

######################## INITIATE DATABASE ########################
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite.sql')
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
    premises_id = db.Column(db.Text)
    # This could company name or more.
    short_description = db.Column(db.Text)
    # One premises can have several devices.
        # ex: column_name = db.relationship('Class to make relationship to', backref = 'this table name')
    devices = db.relationship('Device', backref = 'premises', lazy = 'dynamic')
        
    # Initate data into the premises table
    def __init__ (self, premises_id, short_description):
        self.premises_id = premises_id
        self.short_description = short_description

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
    position = db.Column(db.Integer, db.ForeignKey('premises.premises_id'))
    visitors = db.relationship('Click' , backref = 'devices', lazy = 'dynamic')
    def __init__(self,device_id, premises_id):
        self.device_id = device_id
        self.premises_id = premises_id

    def __repr__(self):
        pass
#-------------DEVICES END-------------#

#-------------CLICKS START-------------#
class Click(db.Model):
    __tablename__ = 'clicks'
    id = db.Column(db.Integer, primary_key=True)
    pass_through = db.Column(db.Integer, db.ForeignKey('devices.visitors'))
    
    def __init__(self, pass_through):
        self.pass_through = pass_through
    
    def __repr__(self):
        pass

#-------------CLICKS START-------------#