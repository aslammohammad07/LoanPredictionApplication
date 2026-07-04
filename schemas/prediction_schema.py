from marshmallow import Schema, fields


class PredictionSchema(Schema):

    loan_id = fields.Integer(required=True)