from app.helloworld.model import Hello


def register_routes(blueprint):
    @blueprint.route('/helloworld', methods=['GET'])
    def get_title():

        result = Hello.get()

        return result.to_json()
