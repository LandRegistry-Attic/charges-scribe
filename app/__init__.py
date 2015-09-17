from flask.ext.api import FlaskAPI
from flask.ext.script import Manager
from app.deed import sign
from app.service.deed_api import DeedApi
from app import helloworld, db, key


def create_manager(deed_api_client=DeedApi):
    app = FlaskAPI(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(key.blueprint)
    app.register_blueprint(sign.blueprint(deed_api_client()))

    manager = Manager(app)
    db.init(app, manager)

    return manager
