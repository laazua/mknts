# @Time:        2022-08-04
# @Author:      Sseve
# @File:        config.py
# @Description: app's config

from pydantic import BaseConfig


class Settings(BaseConfig):
    # app config
    app_title:       str  = "manage zone"
    app_desc:        str  = "web app to manage game zone" # app描述
    app_version:     str  = "0.1.0" # app当前开发版本
    app_debug:       bool = True # 是否开启debug模式
    app_reload:      bool = True # 代码改变是否重新加载
    app_factory:     bool = True
    app_concurrency: int  = 20
    app_max_req:     int  = 1000
    app_port:        int  = 8888 # app监听端口
    app_address:     str  = "0.0.0.0" # app监听地址
    app_key:         str  = "d3f4490ee900710ae48a1247474a40e3920c3ff588d063e0b9f36848d0035ba1"  # terminal中,使用openssl rand -hex 32生成
    app_algorithm:   str  = "HS256" # token加密算法
    app_expire_time: int  = 30 # app token过期时间,单位分钟
    app_white_ips:   list = ["127.0.0.1", "172.16.9.126"]

    # db config 
    db_user:         str  = "username" 
    db_password:     str  = "password"
    db_address:      str  = "mongodb://127.0.0.1:27017/mgsev"

    # svn config
    svn_user:        str  = "username"
    svn_password:    str  = "password"
    svn_address:     str  = "http://127.0.0.1:8080/test/xxx"
    svn_data:        str  = "/data/game/svn_data/"

    # other config
    local_bin:       str  = "/data/codes/mgsev/bin/gameserv" # 本地端binfile路径
    remot_bin:       str  = "/data/game/gameserv" # 远端binfile路径
    gm_path:         str  = "/data/game/" # 区服路径
    gm_shell:        str  = "game_opt.sh" # 区服操作脚本


settings = Settings()
__all__ = ['settings']
