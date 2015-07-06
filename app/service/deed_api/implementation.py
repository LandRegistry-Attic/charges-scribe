import requests

from app import config

DEED_API_BASE_HOST = config.DEED_API_BASE_HOST


def get_deed_json(md_ref):
    return requests.get(DEED_API_BASE_HOST + '/deed/' + str(md_ref)).json()


def can_sign(deed_id, borrower_id):
    url = DEED_API_BASE_HOST + '/deed/' + deed_id + '/' + borrower_id + '/match'
    return requests.get(url).json()
