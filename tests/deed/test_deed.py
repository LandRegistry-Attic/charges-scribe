from tests.helpers import with_client, setUpApp, with_context
from tests.mock.deed_api import MockDeedApi
import unittest
import json


class TestDeed(unittest.TestCase):
    def setUp(self):
        setUpApp(self, deed_api_client=MockDeedApi)

    @with_context
    @with_client
    def test_sign_deed(self, client):
        borrower_name = "DS"
        response = client.post(
            '/deed/1/1/signature/',
            data=json.dumps({"borrower_name": borrower_name}),
            headers={'content-type': 'application/json'}
        )

        assert response.status_code == 200
        assert borrower_name in response.data.decode()
