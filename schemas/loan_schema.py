from marshmallow import Schema, fields, validate


class LoanSchema(Schema):

    applicant_id = fields.Integer(required=True)

    applicant_income = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )

    coapplicant_income = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )

    loan_amount = fields.Float(
        required=True,
        validate=validate.Range(min=1)
    )

    loan_term = fields.Integer(
        required=True,
        validate=validate.Range(min=1)
    )

    credit_history = fields.Integer(
        required=True,
        validate=validate.OneOf([0, 1])
    )