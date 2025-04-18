# -*- coding: utf-8 -*-
"""
fastapi的依赖注入
"""

from typing import Optional
from fastapi import Depends, FastAPI


app = FastAPI()

# 函数作为依赖
async def comm_parameters(q: Optional[str] = None, skip: int = 0, limit: init = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items")
async def read_items(commans:dict = Depends(comm_parameters)):
    return commans


@app.get("/users")
async def read_users(commans: dict = Depends(comm_parameters)):
    return commans


# 类作为依赖
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/bar")
async def read_bar(commans: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commans.q:
        return response.update({"q": commans.q})
    items = fake_items_db[commans.skip: commans.skip + commans.limit]
    response.update({"items": items})
    return response


# 使用Depends()可以进行依赖嵌套