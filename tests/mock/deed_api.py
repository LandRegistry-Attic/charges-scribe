from flask import jsonify
from flask.ext.api import status


class MockDeedApi(object):
    def sign(self, deed_id, borrower_id, signature):
        return jsonify(status_code=status.HTTP_200_OK)
