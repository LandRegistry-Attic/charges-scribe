from .model import Key
from app.db import db


def save(key):
    db.session.add(key)
    db.session.commit()


def all():
    return Key.query.all()


def get(id_):
    return Key.query.filter_by(id=id_).first()


def delete(id_):
    key = Key.query.filter_by(id=id_).first()

    if key is None:
        return key

    db.session.delete(key)
    db.session.commit()

    return key
