from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from config import settings


def create_token(data: dict) -> str:
    expires_delta = timedelta(minutes=settings.app_expire_time)
    if expires_delta:
        expire_time = datetime.utcnow() + expires_delta
    else:
        expire_time = datetime.utcnow() + timedelta(minutes=60)
    data = data.copy()
    data.update({'exp': expire_time})
    return jwt.encode(data, settings.app_key, algorithm=settings.app_algorithm)


def verify_token(token) -> dict:
    credentials_expception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"authorization": "Bearer"}
    )
    try:
        payload  = jwt.decode(token, settings.app_key, algorithms=[settings.app_algorithm])
        username = payload.get("username")
        roles = payload.get("roles")
        if username is None:
            raise credentials_expception
        token_data = {'username': username, 'roles': roles}
        return token_data
    except JWTError:
        raise credentials_expception
