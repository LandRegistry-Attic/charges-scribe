from Crypto.PublicKey import RSA
from random import randint
from app.key.model import Key


class KeyHelper:

    @staticmethod
    def _create_key():

        rsa_key = RSA.generate(2048)

        _key_dict = {"type": "Key",
                     "id": randint(1, 999999),
                     "public_key": str(rsa_key.publickey().exportKey('PEM')),
                     "private_key": str(rsa_key.exportKey('PEM'))}

        key = Key.from_json(_key_dict)

        return key
