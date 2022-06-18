from flask import jsonify, request

from application.exceptions import InvalidParameter
from application.security_jwt import validate_token
from helpers.service_helper import ResponseTemplate
from helpers.utils import hashsum_password_local
from models.mongodb.user import Users


def get_users():
    args = request.args.to_dict()
    search_option = dict()
    if args and args.get('user_type'):
        search_option.update({
            'role_user.' + args['user_type']: True
        })
    if args and args.get('user_id'):
        search_option.update({
            'user_id': args['user_id']
        })
    if args and args.get('school_id'):
        search_option.update({
            'school': {'$elemMatch': {'school_id': args['school_id']}}
        })
    if args and args.get('department_name'):
        search_option.update({
            'school': {'$elemMatch': {'department': {'department_name': args.get('department_name')}}}
        })
    print(search_option)
    datas = Users().list_user(search_option)
    results = list()
    for data in datas:
        data.pop('_id')
        results.append(data)
    return ResponseTemplate(200, {'message': 'Get list user successfully', 'data': results,
                                  'count': datas.count()}).return_response()


def add_user():
    return jsonify({'message': 'add user success'})


def edit_user():
    return jsonify({'message': 'edit user success'})


def delete_user():
    return jsonify({'message': 'delete user success'})


def create_account():
    args = request.json
    search_option = dict()
    username = args.get('username')
    password = args.get('password')
    user_id = args.get('user_id')
    user = Users().find_one({'user_id': user_id})
    check_user = Users().find({'user_id': {'$ne': user_id}, 'username': username})
    print('check_user')
    print(check_user.count())
    print({'user_id': {'$ne': user_id}, 'username': username})
    if check_user.count():
        raise InvalidParameter(error_code=4001000, params='username')

    if user:
        hash_password = hashsum_password_local(password, username)
        print(hash_password)
        user['password'] = hash_password
        user['username'] = username
        Users().update_user(user, user_id)
    else:
        raise InvalidParameter(error_code=4001000, params='user_id')
    return ResponseTemplate(200, {'message': 'Create account successfully'}).return_response()


@validate_token
def self_user_info(current_user):
    user_id = current_user['user_id']
    data = Users().get_user(user_id)
    data.pop('_id')
    return ResponseTemplate(200, {'message': 'Get user successfully', 'data': data}).return_response()
