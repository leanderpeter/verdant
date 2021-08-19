from flask_restx import fields, model
from server.dtos.ticker_bo_dtos import ticker_bo

uuid_bo = model.Model.inherit('BusinessObject', ticker_bo, {
    'UUID': fields.String(attribute='__uuid', description='UUID des BOs'),
})
