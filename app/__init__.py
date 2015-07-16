from flask.ext.api import FlaskAPI
from flask.ext.script import Manager
from app import helloworld, db, key


def create_manager():
    app = FlaskAPI(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(key.blueprint)

    manager = Manager(app)
    db.init(app, manager)

    return manager
