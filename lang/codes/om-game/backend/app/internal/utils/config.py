from starlette.config import Config


config = Config("../../../config.txt")


APP_KEY     = config("APP_KEY", default="test_app")
APP_DEBUG   = config("APP_DEBUG", default=True)
APP_ADDRESS = config("APP_ADDRESS", default="0.0.0.0")
APP_PORT    = config("APP_PORT", default=8666)
APP_RELOAD  = config("APP_RELOAD", default=True)
APP_EXP_TIME = config("APP_EXP_TIME", default=60)
APP_ALG      = config("APP_ALG", default="HS256")


DB_ADDRESS = config("DB_ADDRESS", default="mongodb://127.0.0.1:27017/mgsev")