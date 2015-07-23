import requests

from app import config

DEED_API_BASE_HOST = config.DEED_API_BASE_HOST


def sign(deed_id, borrower_id, signature):
    json_body = {"signature": signature}
    url = DEED_API_BASE_HOST + "/deed/" + deed_id + "/" + borrower_id + "/" \
        + "signature/"
    return requests.post(url, data=json_body)
