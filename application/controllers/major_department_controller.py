from application.exceptions import InvalidParameter
from application.security_jwt import validate_token
from helpers.service_helper import ResponseTemplate
from models.mongodb.department import Departments
from models.mongodb.major import Majors


@validate_token
def list_major(current_user, department_id):
    try:
        datas = Majors().find({'department_id': department_id})
        results = list()
        for data in datas:
            data.pop('_id')
            results.append(data)
    except Exception as e:
        raise InvalidParameter(error_code=4001002, params='get major error')
    return ResponseTemplate(200, {'message': 'Get list major successfully', 'data': results}).return_response()


@validate_token
def list_department(current_user):
    try:
        datas = Departments().find({})
        results = list()
        for data in datas:
            data.pop('_id')
            results.append(data)
    except Exception as e:
        raise InvalidParameter(error_code=4001002, params='get major error')
    return ResponseTemplate(200, {'message': 'Get list major successfully', 'data': results}).return_response()


