import typing
from datetime import timedelta
from datetime import datetime
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app import AppConfig


pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")


def create_token(data: dict) -> str:
    expires_delta = timedelta(hours=AppConfig.getfloat("app", "tokenTimeout"))
    if expires_delta:
        expire_time = datetime.utcnow() + expires_delta
    else:
        expire_time = datetime.utcnow() + timedelta(hours=6)
    data = data.copy()
    data.update({'exp': expire_time})
    return jwt.encode(data, AppConfig.get("app", "tokenKey"), algorithm="HS256")


def verify_token(token) -> dict:
    credentials_expception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={ "authorization": "Bearer" }
    )
    try:
        payload  = jwt.decode(
            token, AppConfig.get("app", "tokenKey"), algorithms=["HS256"])
        username = payload.get("name")
        roles = payload.get("roles")
        if username is None:
            raise credentials_expception
        token_data = { 'name': username }
        return token_data
    except JWTError:
        raise credentials_expception


def hashed_pwd(pwd: str) -> str:
    return pwd_ctx.hash(pwd)


def verify_pwd(plain_pwd: str, hash_pwd: str) -> bool:
    return pwd_ctx.verify(plain_pwd, hash_pwd)


def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> typing.Union[typing.Dict, typing.Any]:
    return verify_token(token)
