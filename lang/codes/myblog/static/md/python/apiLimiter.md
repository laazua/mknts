## ***web api限流***

* *slowapi*
```
from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/home")
@limiter.limit("5/minute")
async def homepage(request: Request):
    return PlainTextResponse("test")

@app.get("/mars")
@limiter.limit("5/minute")
async def homepage(request: Request, response: Response):
    return {"key": "value"}
```

* *fastapi-limiter*
```
import aioredis
import uvicorn
from fastapi import Depends, FastAPI

from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

app = FastAPI()


@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool("redis://localhost")
    FastAPILimiter.init(redis)


@app.get("/", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def index():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True)
```

* *asgi-ratelimit*
```
app.add_middleware(
    RateLimitMiddleware,
    authenticate=AUTH_FUNCTION,
    backend=RedisBackend(),
    config={
        r"^/user": [Rule(second=5, block_time=60)],
    },
)
```

* *参考*
```
slowapi: https://github.com/laurents/slowapi
fastapi-limiter: https://github.com/long2ice/fastapi-limiter
asgi-ratelimit: https://github.com/abersheeran/asgi-ratelimit
```

