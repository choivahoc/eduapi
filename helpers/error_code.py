ERROR_403 = {
    'code': 403,
    'status_code': 403,
    'message': "You don't have the permission to do this"
}

ERROR_CODE = {

    # Error code 401

    401: {
        'code': 401,
        'status_code': 401,
        'message': "Invalid Token"
    },
    4011000: {
        'code': 401,
        'status_code': 4011000,
        'message': "Invalid Signature"
    },
    4011001: {
        'code': 401,
        'status_code': 4011001,
        'message': "Invalid Audience"
    },
    4011002: {
        'code': 401,
        'status_code': 4011002,
        'message': "Token Expired"
    },
    4011003: {
        'code': 401,
        'status_code': 4011003,
        'message': "Decode Error"
    },
    4011004: {
        'code': 401,
        'status_code': 4011004,
        'message': "Token Not Found"
    },
    4011005: {
        'code': 401,
        'status_code': 4011005,
        'message': "User from session_token doesn't exist"
    },
    4011006: {
        'code': 401,
        'status_code': 4011006,
        'message': "You don't have the scope needed for this api"
    },
    4011007: {
        'code': 401,
        'status_code': 4011007,
        'message': "This api can only be used with session_token"
    },


    # Error code 500
    500: {
        'code': 500,
        'status_code': 500,
        'message': "Internal Error"
    }
}

