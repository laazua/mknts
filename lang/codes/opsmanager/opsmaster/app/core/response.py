import typing
from fastapi.responses import JSONResponse


class AppResponse(JSONResponse):
    def __init__(
        self,
        code: int,
        /,
        message: str = None,
        data: typing.Optional[None] = None,
        token: str = None
    ) -> None:
        self.content = {
            "code": code,
            "message": message,
            "data": data,
            "token": token
        }
        super(AppResponse, self).__init__(self.content)