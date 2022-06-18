import jwt
from jose import jwt as jose_jwt
from flask import current_app, abort, request
import datetime
from application.exceptions import Unauthorized
from functools import wraps
from models import User, Tenant, db
import time


def encode_jwt(payload):
    private_key = current_app.config.get('PRIVATE_KEY')
    encoded = jwt.encode(payload, private_key.encode(), algorithm='RS256')
    return encoded


def verify_token(token, public_key):
    try:
        data = jwt.decode(token, public_key.encode(), algorithms='RS256', options={'verify_aud': False})
        print(data)
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


def validate_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user = get_current_user()

        return f(current_user, *args, **kwargs)

    return decorated


def generate_token(username, user_id, role):
    jwt_message = {'username': username,
                   'user_id': user_id,
                   'user_role': role,
                   'exp': datetime.datetime.utcnow() + datetime.timedelta(
                       seconds=current_app.config.get('TOKEN_EXPIRATION_TIME'))}

    session_token = encode_jwt(jwt_message)
    return session_token


def get_current_user():
    token = None

    if 'Authorization' in request.headers:
        token = request.headers['Authorization']

    if not token:
        raise Unauthorized(error_code=4011000)

    if token.startswith('Bearer '):
        token = token[7:]

    public_key = current_app.config['PUBLIC_KEY']
    verify_token(token, public_key)

    try:
        data = jwt.decode(token, public_key.encode(), algorithms='RS256', options={'verify_aud': False})
        current_user = {
            'role': data['user_role'],
            'name': data['username'],
            'user_id': data['user_id']
        }
    except Exception as e:
        raise Unauthorized()

    return current_user
