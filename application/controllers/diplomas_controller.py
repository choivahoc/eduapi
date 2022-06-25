from plistlib import Data

from flask import request

from application.exceptions import InvalidParameter
from application.security_jwt import validate_token
from helpers.service_helper import ResponseTemplate
from models.mongodb.diplomas import Diplomas
from models.mongodb.user import Users


@validate_token
def get_diplomas(current_user):
    args = request.args.to_dict()
    search_option = dict()
    if args and args.get('diplomas_id'):
        search_option.update({
            'diplomas_id': args['diplomas_id']
        })
    if args and args.get('user_id'):
        search_option.update({
            'user_id': args['user_id']
        })
    print(search_option)
    datas = Diplomas().list_diplomas(search_option)
    results = list()
    for data in datas:
        data.pop('_id')
        results.append(data)
    return ResponseTemplate(200, {'message': 'Get list diplomas successfully', 'data': results,
                                  'count': datas.count()}).return_response()


def create_diplomas():
    args = request.json
    diplomas = args.get('diplomas_data')
    user_id = args.get('user_id')
    user = Users().find_one({'user_id': user_id})

    if user:
        Diplomas().insert_document(diplomas)
        user['diplomas'] = {
            'diplomas_id': diplomas['diplomas_id'],
            'diplomas_name': diplomas['diplomas_name'],
        }
        Users().update_user(user, user_id)
    else:
        raise InvalidParameter(error_code=4001000, params='user_id')
    return ResponseTemplate(200, {'message': 'Create diplomas successfully'}).return_response()


@validate_token
def edit_diplomas(current_user, user_id, diplomas_data):
    search_option = {"user_id": user_id}
    Diplomas().upsert(search_option, diplomas_data)
    return ResponseTemplate(200, {'message': 'Edit diplomas successfully'}).return_response()


@validate_token
def upsert_diplomas_point(current_user):
    args = request.json
    user_id = args.get('user_id')
    transcript_academic_id = args.get('transcript_academic_id')
    point = args.get('point')
    user = Users().find_one({'user_id': user_id})
    print(user)
    if user:
        diplomas = Diplomas().find_one({'user_id': user_id})
        transcript = diplomas.get('transcript')
        transcript_new = list()
        for item in transcript:
            if item.get('transcript_academic').get('transcript_academic_id') == transcript_academic_id:
                item['point'] = point
            transcript_new.append(item)
        diplomas['transcript'] = transcript_new
        Diplomas().upsert({'user_id': user_id}, diplomas)
    else:
        raise InvalidParameter(error_code=4001000, params='user_id')
    return ResponseTemplate(200, {'message': 'Edit point successfully'}).return_response()
