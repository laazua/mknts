from datetime import datetime, timedelta
from typing import Any

import jwt
from passlib.context import CryptContext

from taoist.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(subject: str | Any, expires_delta: timedelta):
    """
    创建token
    """
    expire = datetime.now() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.app_secret, algorithm=settings.app_algorithm
    )
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str):
    """
    密码认证
    """
    return pwd_context.verify(plain_password, hashed_password)


def hashed_password(password: str):
    """
    密码哈希
    """
    return pwd_context.hash(password)
