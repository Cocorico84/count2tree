from flask import Blueprint
from flask_restful import Api

from treeroot.models.database import db

from .main import Trees, Location, Height, Height_by_locations

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    api.add_resource(Trees, '/trees')
    api.add_resource(Location, '/locations')
    api.add_resource(Height, '/height')

    app.register_blueprint(api_bp, url_prefix='/api/v1')
