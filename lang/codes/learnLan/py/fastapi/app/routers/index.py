# -*- coding: utf-8 -*-

from fastapi import (
    APIRouter, Request)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(
    tags=["index"]
)

# templates目录要放在顶层目录下
templates = Jinja2Templates(directory='templates')


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
