from functools import wraps
from app import create_manager
from app.db import db
from app.service.deed_api import interface
from tests.mock import deed_api_mock_impl

database_URI = 'sqlite://'


def with_context(test):
    @wraps(test)
    def _wrapped_test(self):
        with self.app.app_context():
            with self.app.test_request_context():
                test(self)
    return _wrapped_test


def with_client(test):
    @wraps(test)
    def _wrapped_test(self):
        with self.app.test_client() as client:
            test(self, client)
    return _wrapped_test


def make_deed_client():
    return interface.DeedApiInterface(deed_api_mock_impl)


def setUpApp(self, deed_api_mock_client=make_deed_client):
    manager = create_manager(deed_api_client=deed_api_mock_client)
    self.app = manager.app
    self.app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
    self.app.config['TESTING'] = True
    self.manager = manager


def setUpDB(self):
    with self.app.app_context():
        db.create_all()


def tearDownDB(self):
    with self.app.app_context():
        db.session.remove()
        db.drop_all()
