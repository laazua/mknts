# -*- coding: utf-8 -*-
"""
jwt组成:
Header{
   'alg': 'HS256',
   'typ': 'JWT'
}

Payload{
    # 官方字段(不是必须的)
    'iss': '签发人',
    'exp': '过期时间',
    'sub': '主题',
    ‘aud’: '受众',
    'nbf': '生效时间',
    'iat': '签发时间',
    'jti': '编号'
    # 私有字段
    'sub': '1234567890',
    'name': 'seve',
    'data': {
        'name': 'test',
        'id': '12'
    }
}

python:jwt
signature:
jwt.encode(
    header,
    payload,
    secret_key
)
"""
import jwt
import datetime


token_secret = "123456"

class Token:
    def __init__(self):
        pass

    def encode_token(self, **kwargs):
        try:
            # exp_days = 1
            exp_hours = 12
            exp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=int(exp_hours), seconds=30)
            payload = {
                'exp': exp_time,
                'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'auth:seve',
                'sub': '123456',
                'data': {
                    'user_id': kwargs.get('user_id', ''),
                    'username': kwargs.get('username', ''),
                },
            }
            return jwt.encode(payload, token_secret, algorithm='HS256')
        except Exception as e:
            return e

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, token_secret, algorithms=['HS256'], leeway=datetime.timedelta(seconds=10))
            if 'data' in payload:
                return payload['data']
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return {"status": "-1", "msg": "token过期"}
        except jwt.InvalidTokenError:
            return {"status": "-2", "msg": "token无效"}
