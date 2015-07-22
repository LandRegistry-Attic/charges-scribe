from time import strftime
from flask import request, jsonify, abort


def register_routes(blueprint, deed_api):
    @blueprint.route('/deed/<deed_id>/<borrower_id>/signature',
                     methods=['POST'])
    def sign_deed(deed_id, borrower_id):
        borrower_name = request.form['borrower_name']

        def create_signature():
            return borrower_name + "_" + strftime("%d/%m/%Y_%H:%M:%S")

        signature = create_signature()
        result = deed_api.sign(deed_id, borrower_id, signature)

        if result.status_code != 200:
            abort(result.status_code)
        else:
            return jsonify(signature=signature)
