# -*- coding:utf-8 -*-
"""
demo
"""

from typing import List

from fastapi import Form, File, UploadFile, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request

from app import router
from app.request.request_parameter import Item


@router.post("/demo", response_model=Item, response_model_exclude_unset=True)    # 响应模型,过滤私有数据
async def create_item(item: Item):
    return item


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    """
    使用Form接收表单字段
    :param username:
    :param password:
    :return:
    """
    return {
        "username": username,
        "password": password
    }


@router.post("/files")
async def files(request: Request, file_list: List[bytes] = File(...)):
    return {
        "request": request,
        "file size": [len(file) for file in file_list]
    }


@router.post("/uploadfile")
async def upload_file(file: List[UploadFile] = File(...)):
    return {
        "filename": file.filename
    }


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
