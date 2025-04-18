import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

from taoist.auth.views import auth_bp
from taoist.jobs.views import jobs_bp
from taoist.config import DevSetting, TestSetting, ProdSetting


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # 加载对象配置
    mode = os.getenv("MODE")
    if mode is None:
        raise  ValueError("Please config: export MODE=[dev|test|prod]")
    if mode == "dev":
        app.config.from_object(DevSetting)
    if mode == "test":
        app.config.from_object(TestSetting)
    if mode == "prod":
        app.config.from_object(ProdSetting)

    # 添加日志处理
    if not os.path.exists(app.config["LOGPATH"]):
        os.makedirs(app.config["LOGPATH"])
    app.logger.setLevel(app.config["LOGLEVEL"])
    logfile = f"{app.config['LOGPATH']}/app.log"
    handler = RotatingFileHandler(logfile, maxBytes=10000, backupCount=1)
    handler.setFormatter(logging.Formatter(app.config["LOGFORMAT"]))
    app.logger.addHandler(handler)

    # 路由注册
    app.register_blueprint(auth_bp)
    app.register_blueprint(jobs_bp)

    # 设置路由:  / == /auth/login
    app.add_url_rule("/", endpoint="auth.login")

    return app 
