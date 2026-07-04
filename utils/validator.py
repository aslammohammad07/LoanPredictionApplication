from marshmallow import ValidationError


def validate_request(schema, data):

    try:

        return schema.load(data), None

    except ValidationError as err:

        return None, err.messages