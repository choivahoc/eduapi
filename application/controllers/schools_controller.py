from flask import jsonify, request

from helpers.service_helper import ResponseTemplate
from models.mongodb.schools import Schools


def get_schools():
    args = request.args.to_dict()
    search_option = dict()
    if args and args.get('school_id'):
        search_option.update({
            'school_id': args['school_id']
        })
    print(search_option)
    datas = Schools().list_school(search_option)
    results = list()
    for data in datas:
        data.pop('_id')
        results.append(data)
    return ResponseTemplate(200, {'message': 'Get list school successfully', 'data': results,
                                  'count': datas.count()}).return_response()


def add_school():
    return jsonify({'message': 'add school success'})


def edit_school():
    return jsonify({'message': 'edit school success'})


def delete_school():
    return jsonify({'message': 'delete school success'})
