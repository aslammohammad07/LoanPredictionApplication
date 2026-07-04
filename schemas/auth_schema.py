from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):

    name = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100)
    )

    email = fields.Email(required=True)

    password = fields.String(
        required=True,
        validate=validate.Length(min=6)
    )


class LoginSchema(Schema):

    email = fields.Email(required=True)

    password = fields.String(required=True)


class ChangePasswordSchema(Schema):

    old_password = fields.String(required=True)

    new_password = fields.String(
        required=True,
        validate=validate.Length(min=6)
    )