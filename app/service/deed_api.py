import requests
from app import config

DEED_API_BASE_HOST = config.DEED_API_BASE_HOST


class DeedApi(object):
    def sign(self, deed_id, borrower_id, signature):
        payload = {"signature": signature}

        url = "{base}/deed/{deed_id}/{borrower_id}/signature/".format(
            base=DEED_API_BASE_HOST,
            deed_id=deed_id,
            borrower_id=borrower_id
        )
        return requests.post(url, json=payload)
