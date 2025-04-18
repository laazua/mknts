# -*- coding: utf-8 -*-
"""
token编码解码, password加密
"""
import datetime
import jwt
import hashlib

from app.config import setting


class Token:
    def __init__(self):
        pass

    @staticmethod
    def encode(**kwargs):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12, seconds=60),
                'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=20),
                'iat': datetime.datetime.utcnow(),
                'iss': 'auth:omms',
                'sub': '123456',
                'data': {
                    'username': kwargs.get('username'),
                },
            }
            return jwt.encode(payload, setting.secret_key, algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode(token):
        try:
            payload = jwt.decode(token, setting.secret_key, algorithms=['HS256'], leeway=datetime.timedelta(seconds=20))
            if 'data' in payload:
                return payload['data']
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return {"code": "-1", "message": "token过期"}
        except jwt.InvalidTokenError:
            return {"code": "-2", "message": "token无效"}

    @staticmethod
    def hash_password(password):
        m = hashlib.md5()
        m.update(password.encode("utf-8"))
        return m.hexdigest()

