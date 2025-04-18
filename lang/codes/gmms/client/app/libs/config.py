
class AppCon:
    expire_minutes = 60
    key_word = "abcdefghijklmnopqrstuvwxyz1234567890"

    db_url = "mysql+pymysql://test:test123@127.0.0.1:3306/bnms?min_size=5&max_size=20"

    app_debug = True
    app_desc = "运维管理系统"


AppCon = AppCon()