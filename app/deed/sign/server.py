from time import time
from flask import request, jsonify, abort
from flask.ext.api import status


def register_routes(blueprint, deed_api):
    @blueprint.route('/deed/<deed_id>/<borrower_id>/signature',
                     methods=['POST'])
    def sign_deed(deed_id, borrower_id):
        def create_signature(borrower_name):
            return borrower_name + "_" + str(time())

        borrower_name = request.get_json()['borrower_name']

        signature = create_signature(borrower_name)
        result = deed_api.sign(deed_id, borrower_id, signature)

        if result.status_code != 200:
            abort(result.status_code)
        else:
            return jsonify(signature=signature), status.HTTP_200_OK
