# app/services/user_service.py
from ..models.user import User
from ..extensions import db

class UserService:
    @staticmethod
    def register(username, password):
        if User.query.filter_by(username=username).first():
            return None, "User already exists"

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user, None

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def get_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user, data):
        if 'username' in data:
            user.username = data['username']
        if 'password' in data:
            user.set_password(data['password'])
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
