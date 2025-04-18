import os

class Config:
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # svn配置
    SVNDIR = os.path.join(path, "svndata")
    SVNUSER = "test"
    SVNPASS = "test123"
    SVNURL = "http://127.0.0.1:8080/svndata/ob"
    # 程序配置
    BINSRC = os.path.join(path, "binfile")
    RPCPORT = 2004
    
    GM_PATH = "/data/game/"
    GM_SCRIPT = "game_opt.sh"


sev_con = Config()