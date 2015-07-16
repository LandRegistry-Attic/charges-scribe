from app.key import keystore


def register_routes(blueprint):

    @blueprint.route('/key', methods=['GET'])
    def get_keys():
        return [key.to_json() for key in keystore.all_keys()]
