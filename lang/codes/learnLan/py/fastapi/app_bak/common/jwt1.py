# -*- coding: utf-8 -*-
"""
jwt组成: Header + Payload + Signature(xxxxx.yyyyy.zzzzz)
Header:
{
    "alg": "HS256",
    "typ": "JWT"
}

Payload:
{
    # 预定义声明(不是必须的,但是推荐使用)
    iss:
    exp:
    sub:
    aud:
    # 公共声明

    # 私有声明
}

Signature:
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)

############
python jwt库:pyjwt, python-jose, jwcrypto, authlib
python处理哈希密码的库: passlib
"""

from passlib import CryptContext


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(pasword):
    return PWD_CONTEXT.hash(pasword)


def verify_password(plain_password, hashed_password):
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def encode_token(data):
    pass


def decode_token(token):
    pass
