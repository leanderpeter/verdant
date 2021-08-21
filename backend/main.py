from server.bo.interaction import Interaction
from server.dtos.uuid_bo_dtos import uuid_bo
from server.dtos.ticker_bo_dtos import ticker_bo
from server.dtos.business_object_dtos import bo


from server.recommender.lightfm_recommender import Recommender
from server.interactions_administration import InteractionAdministration
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from flask import request
import json
import os
print("Lets go...")


# Die App basiert auf Flask
# Die Flask Erweiterung Flask CORS wird für Cross-Origin Resource Sharing verwendet
# Des Weiteren wird das auf Flask aufbauende Flask-RestX verwendet

"""Flask wird hiermit instanziert"""
app = Flask(__name__)

CORS(app, support_credentials=True, resources={
     r'/verdantApp/*': {"origins": "*"}})

api = Api(app, version='0.1', title='Verdant API',
          description='Web App for stock picking')

"""Namespaces"""
verdantApp = api.namespace('verdantApp', description='Functions of verdantApp')


""""Please, someone needs to fix the inheritance in server.dtos. that stuff is
pure garbage"""
verdantApp.add_model("BusinessObject", bo)

interaction = api.inherit('Interaction', bo,  {
    'uuid': fields.String(attribute='_uuid', description="UUID of object"),
    'ticker': fields.String(attribute='_ticker', description="Ticker of holding"),
    'interaction_name': fields.String(attribute='_interaction_name', description="Name der Holding"),

})


'''this needs to be fixed! ticker/average_rating etc needs to be changed to JS CamelCase.
average_rating -> AverageRating
++++
BusinessObjects
++++
'''
stock_metadata = api.inherit('StockMetadata', bo, {
    'ticker': fields.String(attribute='_ticker', description="Ticker Symbol of object"),
    'average_rating': fields.String(attribute='_average_rating', description="Average Rating of object"),
    'marcet_cap': fields.String(attribute='_marcet_cap', description="Marcet Cap  of object"),
    'average_volume': fields.String(attribute='_average_volume', description="Average Volume of object"),
    'country_code': fields.String(attribute='_country_code', description="Country Code of object"),
    'industry': fields.String(attribute='_industry', description="Industry of object"),
    'sector': fields.String(attribute='_sector', description="Sector of object"),
    'employees': fields.String(attribute='_employees', description="Employees of object"),
    'overall_risk': fields.String(attribute='_overall_risk', description="Overall risk of object"),
})


@verdantApp.route('/recommender')
@verdantApp.response(500, 'Something went wrong')
class RecommendationOperationen(Resource):
    @verdantApp.marshal_list_with(interaction)
    def put(self):
        if api.payload != None:
            request_list = list(api.payload)
            adm = InteractionAdministration()
            response = adm.predict(request_list)
            return response
        else:
            return 404


@verdantApp.route('/stocks/metadata')
@verdantApp.response(500, 'Something went wrong')
class MetadataOperationen(Resource):
    @verdantApp.marshal_list_with(stock_metadata)
    def get(self):
        adm = InteractionAdministration()
        response = adm.get_all_metadata()
        return response


if __name__ == '__main__':
    app.run(debug=True)
