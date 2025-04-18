# -*- coding: utf-8 -*-

import jwt
import datetime
import hashlib
from app.config.setting import base



token_secret = '132456789abc'


def encode_token(**kwargs):

    exp_hours = kwargs.get('exp_hours', 24)
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=int(exp_hours), seconds=10),
        'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=10),
        'iat': datetime.datetime.utcnow(),
        'iss': 'auth: seve',
        'sub': 'my token',
        'id': '2135464354657',
        'data': {
            'user_id': kwargs.get('user_id', ''),
            'username': kwargs.get('username', ''),
            'is_superuser': kwargs.get('is_super', False)
        }
    }

    return jwt.encode(
        payload,
        token_secret,
        algorithm='HS256'
    )


def decode_token(token):
    payload = jwt.decode(token, token_secret, algorithms=['HS256'], leeway=datetime.timedelta(seconds=10))
    if 'data' in payload and 'user_id' in payload['data']:
        return payload['data']
    else:
        raise jwt.InvalidTokenError


def hash_password(password):
    m = hashlib.md5()
    m.update(password.encode("utf-8"))
    return m.hexdigest()


def white_list(request):
    ip_list = base.ip_list
    if request.client.host not in ip_list:
        return True
    else:
        return False