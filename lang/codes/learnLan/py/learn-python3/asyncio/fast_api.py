# -*- coding:utf-8 -*-
'''
pip install fastapi[all]
内部使用了uvloop模块

REST API  aio-libs/aiohttp
pip install aiohttp
'''

import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "./modules")))


from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return "hello world"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('fast_api:app', host='127.0.0.1', port=8080, reload='reload')
