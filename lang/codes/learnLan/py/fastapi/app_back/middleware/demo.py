# -*- coding:utf-8 -*-
"""
middleware,在接收请求后和返响应前做一些操作
"""

import time

from fastapi import Request

from app import router


@router.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

