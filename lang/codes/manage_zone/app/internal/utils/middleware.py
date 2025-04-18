# @Time:        2022-08-09
# @Author:      Sseve
# @File:        middleware.py
# @Description: some middlewares

import typing
from starlette.types import ASGIApp
from fastapi import Request, Response
from starlette.middleware.base import \
     BaseHTTPMiddleware, RequestResponseEndpoint, DispatchFunction


class AllowIps(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, ips: typing.Optional[list] = ..., 
                 dispatch: typing.Optional[DispatchFunction] = None) -> None:
        super().__init__(app, dispatch)
        self.ips = ips
    
    # rewrite dispathch method
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.client.host not in self.ips:
            return Response("your ip not allowed")
        return await call_next(request)
