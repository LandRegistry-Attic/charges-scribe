from flask import jsonify
from flask.ext.api import status


def sign(deed_id, borrower_id, signature):
    return jsonify(status_code=status.HTTP_200_OK)
