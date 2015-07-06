from flask import request, jsonify, abort
from flask.ext.api import exceptions, status


def register_routes(blueprint, deed_api):
    @blueprint.route('/deed/signature', methods=['POST'])
    def sign_deed():
        borrower_name = request.get_json()['borrower_name']
        borrower_id = request.get_json()['borrower_id']
        deed_id = request.get_json()['deed_id']
        sign_allowed = deed_api.can_sign(deed_id, borrower_id)['matches']
        if sign_allowed:
            # TODO deed_api.sign_deed
            return jsonify(deed_id=2), status.HTTP_200_OK
        else:
            abort(403)
