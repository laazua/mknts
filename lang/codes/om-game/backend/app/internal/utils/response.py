from typing import Any
from starlette.responses import JSONResponse


class Response(JSONResponse):
    def __init__(self, code: int, /, msg: str = None, data: Any = None) -> None:
        self.content = {"code": code, "msg": msg, "data": data}
        super(Response, self).__init__(self.content)
