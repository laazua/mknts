from fastapi import Depends


from app.shared import db


class AuthRepository:
    """认证仓库类"""
    def __init__(self, db=Depends(db.get)):
        self.db = db  # typing: ignore

    async def auth(self):
        pass


def get() -> AuthRepository:
    return AuthRepository()
