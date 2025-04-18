from passlib.context import CryptContext


class PasswdHandle:
    def __init__(self, plain_pwd: str = None, hash_pwd: str = None) -> None:
        self.plain_pwd = plain_pwd
        self.hash_pwd  = hash_pwd
        self.pwd_ctx   = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @property
    def hash(self):
        return self.pwd_ctx.hash(self.plain_pwd)
    
    @property
    def verify(self):
        return self.pwd_ctx.verify(self.plain_pwd, self.hash_pwd)
