from marshmallow import Schema, fields

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    perfil_id = fields.Int(required=True)
    nombre = fields.Str(required=True)
    correo_electronico = fields.Email(required=True)
    contrasena = fields.Str(required=True)
    fecha_registro = fields.DateTime()
