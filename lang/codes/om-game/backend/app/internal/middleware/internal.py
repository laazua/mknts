from starlette.middleware import Middleware

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware


middleware = [
    Middleware(CORSMiddleware, allow_origins=["*"]),
    Middleware(GZipMiddleware, minimum_size=1000)
]