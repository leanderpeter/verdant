from flask_restx import fields, model

bo = model.Model('BusinessObject', {
    'id': fields.Integer(attribute='__id', description='ID des BOs'),
})
