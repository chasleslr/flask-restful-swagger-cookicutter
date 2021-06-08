from marshmallow import Schema, fields


class HealthcheckResponseSchema(Schema):
    status = fields.String()
