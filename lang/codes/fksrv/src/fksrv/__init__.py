import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

from fksrv.views import auth
from fksrv.views import test


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = b"dev"

    # app.config["LOG_LEVEL"] = "DEBUG"
    app.config["LOG_FORMAT"] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # 设置日志处理程序
    if not os.path.exists("logs"):
        os.mkdir("logs")
    app.logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("logs/app.log", maxBytes=10000, backupCount=1)
    # handler.setLevel(app.config["LOG_LEVEL"])
    handler.setFormatter(logging.Formatter(app.config["LOG_FORMAT"]))
    # 添加处理程序到 app.logger
    app.logger.addHandler(handler)

    # 将中间件应用到 Flask 应用上
    # app.wsgi_app = SimpleMiddleware(app.wsgi_app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(test.bp)

    # 路由:  / == /auth/login
    app.add_url_rule("/", endpoint="auth.login")

    return app
