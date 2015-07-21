from app.key.model import Key
import unittest
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
        gen_key.save()

        retrieved_gen_key = Key.get(gen_key.id)

        self.assertIn(retrieved_gen_key, Key.all())

        Key.delete(gen_key.id)

        self.assertNotIn(retrieved_gen_key, Key.all())

    @with_context
    def test_get_and_delete(self):
        gen_key = KeyHelper._create_key()

        retrieved_gen_key = Key.get(gen_key.id)
        self.assertIsNone(retrieved_gen_key)

        gen_key.save()

        reretrieved_gen_key = Key.get(gen_key.id)
        self.assertEqual(reretrieved_gen_key, gen_key)

        Key.delete(gen_key.id)

        retrieved_no_gen_key = Key.get(gen_key.id)

        self.assertIsNone(retrieved_no_gen_key)
