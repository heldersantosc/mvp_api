from marshmallow import Schema, fields


class ExpenseSchema(Schema):
    id = fields.Integer()
    description = fields.String()
    value = fields.Float()
    date_time = fields.DateTime()
