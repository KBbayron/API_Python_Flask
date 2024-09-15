from marshmallow import Schema, fields, validate

class PerfilSchema(Schema):
    id = fields.Int(dump_only=True)  # El ID se genera automáticamente, por lo que solo se debe mostrar, no recibir.
    DNI = fields.String(required=True, validate=validate.Length(min=1, max=9))
    informacion = fields.String(required=True, validate=validate.Length(min=1))
    status = fields.Boolean(missing=True)  # `status` es opcional en la solicitud de creación, por lo que se proporciona un valor predeterminado.

    class Meta:
        # Puedes agregar opciones adicionales aquí, si es necesario.
        fields = ("id", "DNI", "informacion", "status")

