from flask import Flask, session
from settings import db, app, api
from flask_jwt import JWT, jwt_required
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_restful import Resource
from dbModel import A_premises, Device, Click

#Migrate(app, db)

#-------------Premises Post START-------------#
class Premises(Resource):
      def post(self, premises_id, short_description = 'None provided'):
            try:
                  ThisPremises = A_premises(premises_id, short_description, None)
                  print(ThisPremises.json())
                  if ThisPremises:
                        db.session.add(ThisPremises)
                        db.session.commit()
                        return ThisPremises.json()                     
                  else:
                        return {'Error':'Wrong input'},405            
            except ValueError:
                  print("Post error wrong format")                        
            
#-------------Premises Post END-------------#

#-------------Premises Delete / Get  START-------------#
class DeletePremises(Resource):
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

#-------------ROUTING-------------#
api.add_resource(Premises, '/premises/premises_id="<string:premises_id>"&short_desc="<string:short_description>"')   
api.add_resource(DeletePremises, '/premises/premises_id="<string:premises_id>"')
api.add_resource(ShowAllPremises, '/premises/All')

# @app.route('/')
# def cps():
#     return HelloWorld()

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)