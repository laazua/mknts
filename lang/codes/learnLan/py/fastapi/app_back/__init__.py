# -*- coding:utf-8 -*-

import sys

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

router = APIRouter()
# router类似flask中蓝图.将所有的视图(admin)绑定到一个router上.
sys.path.insert(0, './handlers')
try:
    from app.handlers import admin
    from app.handlers import openserver
    from app.handlers import demo
except Exception as error:
    raise


def get_app():
    """
    :return: fastapi实例
    """
    app = FastAPI(debug=True, title="opms", description="运维管理平台后端")

    origins = ['*']

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    app.add_middleware(
        GZipMiddleware,
        minimum_size=500
    )

    app.include_router(router, prefix='/api')

    return app
