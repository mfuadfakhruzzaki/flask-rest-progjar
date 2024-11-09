# app/models/user.py
from ..extensions import db
from passlib.hash import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # Tambahkan field lain jika diperlukan, seperti email, dll.

    def set_password(self, password):
        self.password = bcrypt.hash(password)

    def check_password(self, password):
        return bcrypt.verify(password, self.password)
