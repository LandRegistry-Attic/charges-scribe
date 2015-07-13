from app.db import db
from flask import jsonify


class Hello(db.Model):
    __tablename__ = 'hello'

    id = db.Column(db.Integer, primary_key=True)
    Hello = db.Column(db.String())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get():
        return Hello.query.filter_by(id=1).first()

    def to_json(self):
        return jsonify(
            Hello=self.Hello
        )
