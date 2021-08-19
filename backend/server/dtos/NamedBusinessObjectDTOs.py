from flask_restx import fields, model
from server.dtos.BusinessObjectDTOs import bo

nbo = model.Model.inherit('NamedBusinessObject', bo, {
    'name': fields.String(attribute='_name', description='Name des BOs'),
})
