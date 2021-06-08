import logging

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from sqlalchemy_utils import create_database, database_exists

from .api.resources.healthcheck import HealthcheckResource
from .config import Config
from .helpers import version


def register_resources(api: Api) -> Api:
    """Register all API resources"""
    api.add_resource(HealthcheckResource, "/healthcheck")
    return api


def register_docs(docs: FlaskApiSpec) -> FlaskApiSpec:
    """Register endpoints to docs"""
    docs.register(HealthcheckResource)
    return docs


def initialize_logging(app: Flask) -> Flask:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    return app


def create_app(config_class=Config) -> Flask:
    """Flask application factory"""
    app = Flask(__name__)

    app.config.from_object(config_class)

    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title="{{ cookiecutter.project_name }}",
                version=version(),
                openapi_version="2.0.0",
                plugins=[MarshmallowPlugin()],
            ),
            "APISPEC_SWAGGER_URL": "/openapi/",
            "APISPEC_SWAGGER_UI_URL": "/",
        }
    )

    app = initialize_logging(app)

    api = Api(app)
    api = register_resources(api)

    docs = FlaskApiSpec(app)
    docs = register_docs(docs)

    from .extensions import db
    db.init_app(app)

    from .extensions import ma

    ma.init_app(app)

    with app.app_context():
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        db.create_all()

    return app
