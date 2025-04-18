from datetime import datetime, timedelta
from jose import jwt, JWTError
from internal.utils import config

class TokenHandle:
    def __init__(self, data: dict = None, token: str = None) -> None:
        self.data  = data
        self.token = token

    @property
    def create(self) -> str:
        expires_delta = timedelta(minutes=config.APP_EXP_TIME)
        if expires_delta:
            expire_time = datetime.utcnow() + expires_delta
        else:
            expire_time = datetime.utcnow() + timedelta(minutes=60)
        data = self.data.copy()
        data.update({"exp": expire_time})
        return jwt.encode(data, config.APP_KEY, algorithm=config.APP_ALG)

    @property
    def verify(self) -> dict:
        try:
            payload  = jwt.decode(self.token, config.APP_KEY, algorithms=[config.APP_ALG])
            username = payload.get("username")
            roles    = payload.get("roles")
            if not username:
                raise "Unauthorized"
            return {"username": username, "roles": roles}
        except JWTError:
            raise "Unauthorized 401"
