from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

dictPremises = []

#-------------Populate START-------------#
class Populate(Resource):
      def get(self, premises):
            for A_premises in dictPremises:
                  if A_premises['premises_id'] == premises:
                        return A_premises

            return {'premises_id':None}

      def post(self, premises):
            A_Premises = {'premises_id' : premises}
            dictPremises.append(A_Premises)
            return dictPremises

      def delete(self, premises):
            for i,A_premises in enumerate(dictPremises):
              if A_premises['premises_id'] == premises:
                del_post = dictPremises.pop(i)
                print (f"{del_post} is deleted")
                return {'note':'delete success'}
            return {'note':'Cant delete no post with that name'}  


                     
#-------------Populate END-------------#

#-------------All Premises START-------------#
class ShowAllPremises(Resource):
      def get(self):
            return {'premises':dictPremises}


#-------------All Premises STOP-------------#
api.add_resource(Populate, '/populate/<string:premises>')   
api.add_resource(ShowAllPremises, '/All')

# @app.route('/')
# def cps():
#     return HelloWorld()

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)