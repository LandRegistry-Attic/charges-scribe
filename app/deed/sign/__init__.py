from flask import Blueprint
from . import server


def blueprint(deed_api_client):
    blueprint = Blueprint('deed.sign', __name__)
    server.register_routes(blueprint, deed_api_client)
    return blueprint
