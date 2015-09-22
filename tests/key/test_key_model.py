import unittest
from app.key import service as key_service
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB
from tests.key.helpers import KeyHelper


class TestKeyModel (unittest.TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_get_all(self):
        gen_key = KeyHelper._create_key()
        key_service.save(gen_key)

        retrieved_gen_key = key_service.get(gen_key.id)

        self.assertIn(retrieved_gen_key, key_service.all())

        key_service.delete(gen_key.id)

        self.assertNotIn(retrieved_gen_key, key_service.all())

    @with_context
    def test_get_and_delete(self):
        gen_key = KeyHelper._create_key()

        retrieved_gen_key = key_service.get(gen_key.id)
        self.assertIsNone(retrieved_gen_key)

        key_service.save(gen_key)

        reretrieved_gen_key = key_service.get(gen_key.id)
        self.assertEqual(reretrieved_gen_key, gen_key)

        key_service.delete(gen_key.id)

        retrieved_no_gen_key = key_service.get(gen_key.id)

        self.assertIsNone(retrieved_no_gen_key)
