class DeedApiInterface(object):
    def __init__(self, implementation):
        self.implementation = implementation

    def sign(self, deed_id, borrower_id, signature):
        return self.implementation.sign(deed_id, borrower_id, signature)
