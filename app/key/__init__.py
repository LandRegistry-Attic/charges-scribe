from flask import Blueprint
from . import server


blueprint = Blueprint('key', __name__)
server.register_routes(blueprint)
