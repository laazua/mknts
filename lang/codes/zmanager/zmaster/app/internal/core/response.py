from typing import Any
from fastapi.responses import JSONResponse


class AppResponse(JSONResponse):
    def __init__(
        self,
        code: int,
        /,
        msg: str = None,
        data: Any = None,
        token: str = None
    ) -> None:
        self.content = {
            "code": code,
            "message": msg,
            "data": data,
            "token": token
        }
        super(AppResponse, self).__init__(self.content)
