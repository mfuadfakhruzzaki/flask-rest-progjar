# app/resources/user.py
from flask import Blueprint, logging, request, jsonify
from flask_restful import Api, Resource
from ..services.user_service import UserService
from ..schemas.user import UserSchema
from flask_jwt_extended import (
    create_access_token, jwt_required,
    get_jwt_identity, unset_jwt_cookies
)
from datetime import timedelta
from .. import db

user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)
user_schema = UserSchema()

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            logging.error("No input data provided")
            return {'message': 'No input data provided'}, 400

        errors = user_schema.validate(data)
        if errors:
            logging.error(f"Validation errors: {errors}")
            return {'errors': errors}, 400

        username = data.get('username')
        password = data.get('password')
        user, error = UserService.register(username, password)
        if error:
            logging.error(f"Registration error: {error}")
            return {'message': error}, 400

        logging.info(f"User registered successfully: {user.username}")
        return user_schema.dump(user), 201
    def post(self):
        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400

        errors = user_schema.validate(data)
        if errors:
            return {'errors': errors}, 400

        username = data.get('username')
        password = data.get('password')
        user, error = UserService.register(username, password)
        if error:
            return {'message': error}, 400

        return user_schema.dump(user), 201

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'message': 'Username and password are required'}, 400

        user = UserService.authenticate(username, password)
        if not user:
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        return {'access_token': access_token}, 200

class LogoutResource(Resource):
    @jwt_required()
    def post(self):
        response = jsonify({'message': 'Logged out successfully'})
        unset_jwt_cookies(response)
        return response, 200

class ResetPasswordResource(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        user = UserService.get_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.get_json()
        new_password = data.get('new_password')
        if not new_password or len(new_password) < 6:
            return {'message': 'New password is required and should be at least 6 characters'}, 400

        user.set_password(new_password)
        db.session.commit()
        return {'message': 'Password updated successfully'}, 200

class DeleteUserResource(Resource):
    @jwt_required()
    def delete(self):
        user_id = get_jwt_identity()
        user = UserService.get_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        UserService.delete_user(user)
        return {'message': 'User deleted successfully'}, 200

class UpdateUserResource(Resource):
    @jwt_required()
    def put(self):
        user_id = get_jwt_identity()
        user = UserService.get_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400

        user = UserService.update_user(user, data)
        return user_schema.dump(user), 200

# Register resources
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
api.add_resource(ResetPasswordResource, '/reset_password')
api.add_resource(DeleteUserResource, '/delete_user')
api.add_resource(UpdateUserResource, '/update_user')
