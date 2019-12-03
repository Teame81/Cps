from flask import Flask, session
from flask_restful import Resource, Api
from secretkeys import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from secretkeys import DBinfo
from dbModel import A_premises, Device, Click

# Making the essentals objects
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)
jwt = JWT(app, authenticate,identity)

# DC Setup, connection
DBuser = DBinfo["Username"]
DBpassword = DBinfo["Password"]
DBname = DBinfo["Database"]
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DBuser}:{DBpassword}@localhost:5432/{DBname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#Migrate(app, db)

#-------------Premises START-------------#
class Premises(Resource):
      def get(self, premises_id, short_description = ' '):
            ThisPremises = A_premises.query.filter_by(premises_id=premises_id).first()
            if ThisPremises:
                  return ThisPremises.json()
            else:
                  return {'Premises':None},404

      def post(self, premises_id, short_description):
            ThisPremises = A_premises(premises_id, short_description, None)
            db.session.add(ThisPremises)
            db.session.commit()
            return A_premises.json()

      def delete(self, premises_id, short_description):
            ThisPremises = A_premises.query.filter_by(premises_id=premises_id).first()
            db.session.delete(ThisPremises)
            db.session.commit()
            return {'Note' : 'Delete success'}

                     
#-------------Premises END-------------#

#-------------All Premises START-------------#
class ShowAllPremises(Resource):
#      @jwt_required()
      def get(self):
            AllPremises = Premises.query.all()
            return [A_premises.json() for A_premises in AllPremises]

#-------------All Premises STOP-------------#

#-------------ROUTING-------------#
api.add_resource(Premises, '/premises/premises_id="<string:premises_id>"&short_desc="<string:short_description>"')   
api.add_resource(ShowAllPremises, '/premises/All')

# @app.route('/')
# def cps():
#     return HelloWorld()

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)