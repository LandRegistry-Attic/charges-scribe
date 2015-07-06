class DeedApiInterface(object):
    def __init__(self, implementation):
        self.implementation = implementation

    def can_sign(self, deed_id, borrower_id):
        return self.implementation.can_sign(deed_id, borrower_id)
