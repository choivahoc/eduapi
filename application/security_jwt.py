import jwt
from jose import jwt as jose_jwt
from flask import current_app, abort, request
import datetime
from application.exceptions import Unauthorized
from functools import wraps
from models import User, Tenant, db
import time


def verify_token(token, public_key):
    try:
        jwt.decode(token, public_key.encode(), algorithms='RS256')
    except jwt.exceptions.InvalidSignatureError as e:
        raise Unauthorized(error_code=4011000)
    except jwt.exceptions.InvalidAudienceError as e:
        raise Unauthorized(error_code=4011001)
    except jwt.exceptions.ExpiredSignatureError as e:
        raise Unauthorized(error_code=4011002)
    except jwt.exceptions.DecodeError as e:
        raise Unauthorized(error_code=4011003)
    except Exception as e:
        current_app.logger.error(e)
        raise Unauthorized()


def validate_id_token(token):
    try:
        key = current_app.config['IS_KEY']
        jose_jwt.decode(token, key, algorithms='RS256', options={"verify_at_hash": False, 'verify_aud': False})
    except Exception as e:
        current_app.logger.error(e)
        abort(400, {"message": "The id_token received from IS does not match the signature provided in the config"})


def validate_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user = get_current_user()

        if current_user['access_from'] != current_app.config['CLIENT_MASTER_NAME']:
            abort(400, {'message': "You can only access this api in MASTER app client"})

        return f(current_user, *args, **kwargs)

    return decorated


def get_current_user(refresh_mode=False):
    token = None

    if 'Authorization' in request.headers:
        token = request.headers['Authorization']

    if not token:
        raise Unauthorized(error_code=4011000)

    if token.startswith('Bearer '):
        token = token[7:]

    public_key = current_app.config['GATEKEEPER_PUBLIC_KEY']
    verify_token(token, public_key)

    try:
        data = jwt.decode(token, options={"verify_signature": False})
        current_user = {
            'm_role': data['user_role'],
            'name': data['user_name'],
            'tenant': data['user_tenant'],
            'access_from': data['client_id']
        }
    except Exception as e:
        raise Unauthorized()

    return current_user
