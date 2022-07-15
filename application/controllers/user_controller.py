from flask import jsonify, request

from application.exceptions import InvalidParameter
from application.security_jwt import validate_token
from helpers.service_helper import ResponseTemplate
from helpers.utils import hashsum_password_local
from models.mongodb.diplomas import Diplomas
from models.mongodb.user import Users


@validate_token
def get_users(current_user):
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
            "school.department.department_name": args.get('department_name')
        })
        datas = Users().aggregate_data([{"$match": search_option}])
    else:
        datas = Users().list_user(search_option)
    results = list()
    for data in datas:
        data.pop('_id')
        results.append(data)
    return ResponseTemplate(200, {'message': 'Get list user successfully', 'data': results,
                                  'count': len(results)}).return_response()


@validate_token
def add_user(current_user):
    args = request.json
    user_data = args.get('user_data')
    Users().insert_document(user_data)
    return ResponseTemplate(200, {'message': 'Create user successfully'}).return_response()


@validate_token
def edit_user(current_user, user_id, user_data):
    search_option = {"user_id": user_id}
    Users().upsert(search_option, user_data)
    return ResponseTemplate(200, {'message': 'Edit user successfully'}).return_response()


def delete_user():
    return jsonify({'message': 'Delete user success'})


def create_account():
    args = request.json
    username = args.get('username')
    password = args.get('password')
    user_id = args.get('user_id')
    user = Users().find_one({'user_id': user_id})
    check_user = Users().find({'user_id': {'$ne': user_id}, 'username': username})
    print('check_user')
    print(check_user.count())
    print({'user_id': {'$ne': user_id}, 'username': username})
    if check_user.count():
        raise InvalidParameter(error_code=4001002, params='username already exist')

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
    return ResponseTemplate(200, {'message': 'Get self user successfully', 'data': data}).return_response()


@validate_token
def get_student_info_by_class(current_user):
    args = request.json
    user_id = args.get('user_id') if args.get('user_id') else None
    class_name = args.get('class_name')
    search_user_query = {
            "school.department.major.class.class_name": class_name
        }
    if user_id:
        search_user_query.update({'user_id': user_id})
    print(search_user_query)
    users = Users().aggregate_data([{"$match": search_user_query}])
    users = list(users)
    results = list()
    for user in users:
        diplomas = Diplomas().find_one({'user_id': user.get('user_id')})
        diplomas_user = dict()
        diplomas_user['user_id'] = user.get('user_id')
        diplomas_user['username'] = user.get('username')
        diplomas_user['full_name'] = user.get('full_name')
        diplomas_user['email'] = user.get('email')
        diplomas_user['gender'] = user.get('profile').get('gender')
        diplomas_user['date_of_birth'] = user.get('profile').get('date_of_birth')
        if diplomas:
            diplomas_data = dict()
            diplomas_data['awarded_date'] = diplomas.get('awarded_date')
            diplomas_data['awarded_place'] = diplomas.get('awarded_place')
            diplomas_data['degree_awarder'] = diplomas.get('degree_awarder')
            diplomas_data['id_graduate_certification'] = diplomas.get('id_graduate_certification')
            diplomas_data['transcript'] = diplomas.get('transcript')
        else:
            diplomas_data = {}
        diplomas_user['student_diplomas'] = diplomas_data
        results.append(diplomas_user)
    return ResponseTemplate(200, {'message': 'Get list student successfully', 'data': results}).return_response()
