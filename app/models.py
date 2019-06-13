from typing import Tuple

from app import db, ma
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<User {}>'.format(self.username)


class PersonSchema(ma.Schema):
    class Meta:
        fields: Tuple[str, ...] = ('id', 'username', 'email', 'created')


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(240))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Activity {}>'.format(self.body)


class ActivitySchema(ma.Schema):
    class Meta:
        fields: Tuple[str, ...] = ('id', 'activity', 'created', 'user_id')
