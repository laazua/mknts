from passlib.context import CryptContext


_pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed_pwd(pwd: str) -> str:
    return _pwd_ctx.hash(pwd)


def verify_pwd(plain_pwd: str, hash_pwd: str) -> bool:
    return _pwd_ctx.verify(plain_pwd, hash_pwd)