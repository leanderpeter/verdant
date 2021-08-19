from flask_restx import fields, model
from server.dtos.business_object_dtos import bo

ticker_bo = model.Model.inherit('BusinessObject', bo ,{
    'ticker': fields.Integer(attribute='__ticker', description='Ticker Symbol des BOs'),
})
