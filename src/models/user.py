from . import db
from .abc import BaseModel

import datetime


class User(db.Model, BaseModel):
    __tablename__ = 'user'

    username = db.Column(db.String, primary_key=True,unique=True, nullable=False)
    avatar_url = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username: str, avatar_url: str = '', date_created: str = ''):
        self.username = username
        self.avatar_url = avatar_url
        self.date_created = datetime.date
