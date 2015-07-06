from flask import Flask
from flask.ext.script import Manager
from app import helloworld
from app.deed import sign
from app.service.deed_api import make_deed_client


def create_manager(deed_api_client=make_deed_client):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(sign.blueprint(deed_api_client()))

    return manager
