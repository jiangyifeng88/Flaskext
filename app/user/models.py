from app.ext import db
from flask_login import UserMixin


class User(db.model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Integer, default=1)

    def get_id(self):
        return self.uid
