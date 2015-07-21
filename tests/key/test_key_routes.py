from tests.helpers import (
    with_client, setUpApp, with_context, setUpDB, tearDownDB
)
from tests.key.helpers import KeyHelper
import unittest
from flask.ext.api import status
import json


class TestKey (unittest.TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_get_key_api(self, client):
        gen_key = KeyHelper._create_key()
        gen_key.save()

        response = client.get('/key')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        decoded_json = json.loads(response.data.decode())

        self.assertEqual(len(decoded_json), 1)
        self.assertEqual(decoded_json[0], gen_key.to_json())
