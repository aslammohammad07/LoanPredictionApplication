from marshmallow import Schema, fields, validate


class ApplicantSchema(Schema):

    gender = fields.String(
        required=True,
        validate=validate.OneOf(["Male", "Female"])
    )

    married = fields.String(
        required=True,
        validate=validate.OneOf(["Yes", "No"])
    )

    dependents = fields.String(required=True)

    education = fields.String(
        required=True,
        validate=validate.OneOf(["Graduate", "Not Graduate"])
    )

    self_employed = fields.String(
        required=True,
        validate=validate.OneOf(["Yes", "No"])
    )

    property_area = fields.String(
        required=True,
        validate=validate.OneOf([
            "Urban",
            "Semiurban",
            "Rural"
        ])
    )