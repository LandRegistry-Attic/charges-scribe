from app.key.model import Key
from flask import request


def register_routes(blueprint):

    @blueprint.route('/key', methods=['GET'])
    def get_keys():
        return [key.to_json() for key in Key.all()]
