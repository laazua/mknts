from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from config import settings


_pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
_oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/login")


def hashed_pwd(pwd: str) -> str:
    return _pwd_ctx.hash(pwd)


def verify_pwd(pwd: str, hash_pwd: str) -> bool:
    return _pwd_ctx.verify(pwd, hash_pwd)


def create_token(data: dict) -> str:
    expires_delta = timedelta(hours=settings.TOKEN_TIME)
    if expires_delta:
        expire_time = datetime.utcnow() + expires_delta
    else:
        expire_time = datetime.utcnow() + timedelta(hours=2)
    data = data.copy()
    data.update({"exp": expire_time})
    return jwt.encode(data, settings.TOKEN_KEY, algorithm="HS256")


def verify_token(token: str) -> dict:
    credentials_expception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"authorization": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.TOKEN_KEY, algorithms=["HS256"])
        username = payload.get("name")
        roles = payload.get("roles")
        if username is None:
            raise credentials_expception
        token_data = {"name": username, "roles": roles}
        return token_data
    except JWTError:
        raise credentials_expception


async def get_current_user(token: str = Depends(_oauth2_schema)) -> dict:
    return verify_token(token)