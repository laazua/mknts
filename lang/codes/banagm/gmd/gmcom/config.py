# -*- coding: utf-8 -*-
"""gmd配置"""
import os

class Config:
    gmd_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    pid_file = os.path.join(gmd_path, 'app.pid')
    gmd_addr = ('0.0.0.0', 2004)
    gmd_cmd = ['start', 'stop', 'check', 'update']

    ## 加密套接字数据的公钥和私钥文件
    pub_file = gmd_path + '/pem/public_key.pem'
    pri_file = gmd_path + '/pem/private_key.pem'
    ## 数据传送相关配置
    data_size = 12
    allow_ips = ['127.0.0.1', '101.132.245.153']
    
    game_dir = '/data/game/'
    game_alias = 'syf'
    game_script = 'game_opt.sh'

    ## 运维服相关信息
    yw_user = 'gamecpp'
    yw_pass = 'gamevcppnd2jd2ffla'
    yw_host = '101.132.245.153'
    bin_path = '/home/gamecpp/codes/banagm/bnms/backsource/{gameserv-beta,md5.txt}'
  
    ## svn仓库认证信息
    svn_url = 'http://159.75.220.163:8080/svn/syfdata/ob'
    svn_user = 'wupan'
    svn_pass = 'wupanwupan'
    svn_dir = gmd_path + '/svndata'

    ## 监控数值信息
    web_hook = 'https://oapi.dingtalk.com/robot/send?access_token=db7054b9a5c5a8fb1fe441f36044cf13d0cbc707ee963b0ab85526e06c5c9a70'
    disk_mou = '/data'
    disk_val = 80.0
    load_val = 50.0
    cpu_val = 80.0
    mem_val = 100.0

gmdcon = Config()
__all__ = [gmdcon]