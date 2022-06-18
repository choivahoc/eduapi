from flask import jsonify, request

from application.exceptions import InvalidParameter
from application.security_jwt import generate_token
from helpers.utils import hashsum_password_local
from helpers.service_helper import ResponseTemplate
from models.mongodb.user import Users


def login():
    args = request.json
    role = args.get('role')
    username = args.get('username')
    password = args.get('password')
    user = Users().find_one({'username': username})
    if user:
        hash_password = hashsum_password_local(password, username)
        print('hash_password')
        print(hash_password)
        if user.get('password') == hash_password and user.get('role_user').get(role) == True:
            token = generate_token(username, user.get('user_id'), role)
            print(token)
            return ResponseTemplate(200, {'message': 'Get list user successfully', 'token': token}).return_response()
        else:
            raise InvalidParameter(error_code=4001000, params='username or password')
    else:
        raise InvalidParameter(error_code=4001000, params='username or password')


def edit_user():
    return jsonify({'message': 'edit user success'})


def delete_user():
    return jsonify({'message': 'delete user success'})
