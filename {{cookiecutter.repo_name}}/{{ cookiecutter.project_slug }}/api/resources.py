from flask_restful import Resource
from flask_apispec import MethodResource, marshal_with, doc

from ..serializers.healthcheck import HealthcheckResponseSchema


class HealthcheckResource(Resource, MethodResource):
    @doc(
        summary="Check the app's health status",
        tags=["Healthcheck"]
    )
    @marshal_with(
        HealthcheckResponseSchema,
        code=200,
        description="Successful Response. See response object for health status."
    )
    def get(self):
        return {"status": "healthy"}
