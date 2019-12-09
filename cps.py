# NOTES to me:
# Check into https://flask-restful.readthedocs.io/en/latest/api.html

from flask import Flask, session, render_template
from settings import db, app, api, migrate
from flask_jwt import JWT, jwt_required
from flask_migrate import Migrate
from flask_restful import Resource
from dbModel import A_premises, Device, Click
from datetime import datetime

#Migrate(app, db)

#########################START PREMISES SECTION#########################

#-------------Premises Post START-------------#
class Premises(Resource):
      def post(self, premises_id, short_description = 'None provided'):
            print("First")
            ThisPremises = A_premises(premises_id, short_description, None)
            print(ThisPremises.json())
            if ThisPremises:
                  db.session.add(ThisPremises)
                  db.session.commit()
                  return ThisPremises.json(), 201
            else:
                  return {'Error':'Wrong input'},404

#-------------Premises Post END-------------#

#-------------Premises Delete / Get  START-------------#
class DeletePostPremises(Resource):
      def delete(self, premises_id):
            DeleteThisPremises = A_premises.query.filter_by(premises_id=premises_id).first()
            db.session.delete(DeleteThisPremises)
            db.session.commit()
            return {'Note' : f'{DeleteThisPremises.json()} Delete success'}

      def get(self, premises_id):
            ThisPremises = A_premises.query.filter_by(premises_id=premises_id).first()
            if ThisPremises:
                  return ThisPremises.json()
            else:
                  return {'Premises':None},404
#-------------Premises Delete / Get END-------------#

#-------------All Premises START-------------#
class ShowAllPremises(Resource):
#      @jwt_required()
      def get(self):
            AllPremises = A_premises.query.all()
            return [A_premises.json() for A_premises in AllPremises]

#-------------All Premises STOP-------------#

#########################END PREMISES SECTION#########################

#########################START CLICKS SECTION#########################

class PostClick(Resource):
      def post(self, pass_through):
            theTimeStamp = datetime.now()
            theClick = Click(pass_through, theTimeStamp)
            db.session.add(theClick)
            db.session.commit()
            return (f"{theClick.json()} : '{theTimeStamp}'"), 201

#########################END CLICKS SECTION#########################

#########################START DEVICES SECTION#########################

class ADevice(Resource):
      def post(self, position):
            NewDevice = Device(position)
            db.session.add(NewDevice)
            db.session.commit()
            return NewDevice.json(),201

#########################END DEVICES SECTION#########################

#-------------ROUTING-------------#
api.add_resource(Premises, '/premises/premises_id="<string:premises_id>"&short_desc="<string:short_description>"')   
api.add_resource(DeletePostPremises, '/premises/Dp/premises_id="<string:premises_id>"')
api.add_resource(ShowAllPremises, '/premises/All')
api.add_resource(PostClick, '/click/id="<int:pass_through>"')
api.add_resource(ADevice, '/device/position="<int:position>"')

@app.route('/')
def home():
      timestamp = datetime.now()
      premises = A_premises.query.all()
      devices = Device.query.all()
      clicks = Click.query.all()
      return render_template('index.html',Jtimestamp = timestamp,
                              Jpremises = premises,
                              Jdevices = devices,
                              Jclicks = clicks
      )
@app.route('/<wrong_page>')
def catch(wrong_page):
      return f"No pages called {wrong_page} exists",404

# Start a test server
if __name__ == '__main__':
  app.run()
  #inside app.run function during devlopment :
  #host='127.0.0.1', port=5000, debug=True