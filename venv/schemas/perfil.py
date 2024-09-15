from marshmallow import Schema, fields

class PerfilSchema(Schema):
    id = fields.Int(dump_only=True)
    DNI = fields.Str(required=True)
    informacion = fields.Str(required=True)
    status = fields.Str(required=True)
    fecha_registro = fields.DateTime()
