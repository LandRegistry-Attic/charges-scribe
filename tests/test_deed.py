from tests.helpers import with_client, setUpApp, with_context
import unittest


def post_json_body():
    return {"deed_id": "1",
            "borrower_id": "1",
            "borrower_name": "DS"}


class TestDeedCanSign(unittest.TestCase):
    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_sign_deed(self, client):
        response = client.post('/deed/signature')


class TestDeedCannotSign(unittest.TestCase):
    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_sign_deed(self, client):
        response = client.post('/deed/signature')
