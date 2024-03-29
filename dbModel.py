from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from settings import db, app, migrate

######################## INITIATE DATABASE ########################
#app = Flask(__name__)

#Migrate(app, db)

######################## DATA BASE MODELS ########################

#-------------PREMISES START-------------#
class A_premises(db.Model):
    # Manual override table name / if not used it will use class name.
    __tablename__ = 'premises'
    id = db.Column(db.Integer,primary_key=True)
    # premises id.
    premises_id = db.Column(db.String(50), unique = True)
    # This could company name or more.
    short_description = db.Column(db.String(120))

    # One premises can have several devices.
        # ex: column_name = db.relationship('Class to make relationship to', backref = 'this table name')
    devices = db.relationship('Device', backref = 'premises', lazy = 'dynamic')
        
   # Initate data into the premises table
    def __init__ (self, premises_id, short_description, devices):
        self.premises_id = premises_id
        self.short_description = short_description
        if devices is not None:
            self.devices = devices

    def json(self):
        return {'id': self.id, 'Premises': self.premises_id, 'Description' : self.short_description}

    # def __repr__(self):
    #     if self.devices:
    #         print(f"---Start---")
    #         for device in self.devices:
    #             print(f"{device} is present in {self.premises_id}")
    #         return f"---End---"
    #     else:
    #         return f"Premises have no device(s) yet."
#-------------PREMISES END-------------#


#-------------DEVICES START-------------#
class Device(db.Model):
    __tablename__ = 'devices'
    # All devices should have a unique id
    id = db.Column(db.Integer, primary_key=True)
    # In which premisis is this device located?
    position = db.Column(db.Integer, db.ForeignKey('premises.id'))
    # Number of people that has passed this device
    visitors = db.relationship('Click' , backref = 'devices', lazy = 'dynamic')
    
    def __init__(self, position):
        self.position = position

    def json(self):
        return {'Device_id' : self.id,
                 'Position' : self.position}

    def __repr__(self):
        pass
#-------------DEVICES END-------------#

#-------------CLICKS START-------------#
    # This is the table for click with time stamps that connects to a device.
class Click(db.Model):
    __tablename__ = 'clicks'
    id = db.Column(db.Integer, primary_key=True)
    # this is a post for when a person passes thru
    pass_through = db.Column(db.Integer, db.ForeignKey('devices.id'))
    time_stamp = db.Column(db.DateTime)
    def __init__(self, pass_through, time_stamp):
        self.pass_through = pass_through
        self.time_stamp = time_stamp
    
    def __repr__(self):
        pass
    def json(self):
        return {'Device_id' : self.pass_through,
                'Time stamp' : self.time_stamp}
#-------------CLICKS START-------------#