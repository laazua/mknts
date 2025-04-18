# -*- coding: utf-8 -*-
"""
program enter
"""

import uvicorn

from app import get_app
from app.config import setting


app = get_app()


if __name__ == "__main__":
    uvicorn.run("server:app", host=setting.host, port=setting.port, reload=True)
