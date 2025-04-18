# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.routers import (
    user, index)
from app.config import setting


def get_app():
    app = FastAPI(debug=True, title=setting.app_name, description=setting.app_desc)

    app.include_router(user.router)
    app.include_router(index.router)

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers={"*"}
    )
    app.add_middleware(
        GZipMiddleware,
        minimum_size=500
    )

    return app
