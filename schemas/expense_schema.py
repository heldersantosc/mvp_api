from marshmallow import Schema, fields, validates, ValidationError


class ExpenseSchema(Schema):
    id = fields.Integer()
    description = fields.String(required=True)
    value = fields.Float(required=True)
    date_time = fields.DateTime(required=True)

    @validates("value")
    def validate_value(self, value):
        message = "O Valor não pode ser menor ou igual a zero."
        if value <= 0:
            raise ValidationError(message)
