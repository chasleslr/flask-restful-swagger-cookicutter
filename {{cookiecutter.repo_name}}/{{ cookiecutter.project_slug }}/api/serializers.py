from marshmallow import Schema, fields
from webargs.flaskparser import abort, parser


class HealthcheckResponseSchema(Schema):
    status = fields.String()


@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    status_code = error_status_code or 422
    abort(status_code, errors=err.messages)
