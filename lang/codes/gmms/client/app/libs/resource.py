"""
响应及数据库查询字符串定义
"""
from fastapi.exceptions import HTTPException


# api response error
LOGIN_PASS_ERROR = HTTPException(
    status_code=400, 
    detail="PASSWORD ERROR!")
LOGIN_USER_ERROR = HTTPException(
    status_code=400, 
    detail="USER NOT EXISTS!")
REGESTER_USER_ERROR = HTTPException(
    status_code=400, 
    detail="USER IS EXISTS!")
REGESTER_USER_FAILD = HTTPException(
    status_code=400, 
    detail="REGESTER USER ERROR!")
REGESTER_PASS_ERROR = HTTPException(
    status_code=400, 
    detail="PASSWORD NOT SAME!")
CREATE_ZONES_ERROR = HTTPException(
    status_code=400, 
    detail="CREATE ZONES TB ERROR!")
DELETE_USER_ERROR = HTTPException(
    status_code=400,
    detail="DELETE USER ERROR!")
CREDENTIALS_EXCEPTION = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={'authorization': 'bearer'})
SELECT_ZONES_ERROR = HTTPException(
    status_code=400,
    detail="SELECT ZONES TB ERROR!")
SELECT_SERVEIP_ERROR = HTTPException(
    status_code=400,
    detail="SELECT SERVEVR IP ERROR!")


# sql
GET_USER_BY_NAME = """
SELECT 
    username,
    password
FROM users
WHERE username = '{}'
"""

INSERT_USER_TO_DB = """
INSERT INTO users 
    (username, password, update_at, create_at)
VALUES
    (:username, :password, :update_at, :create_at)
"""

CREATE_USER_TB = """
CREATE TABLE IF NOT EXISTS `users` (
    id INTEGER AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    create_at VARCHAR(255) NOT NULL,
    update_at VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
)
"""

CREATE_ZONES_TB = """
CREATE TABLE IF NOT EXISTS `{}` ( 
    id INTEGER AUTO_INCREMENT,
    server_name VARCHAR(255) NOT NULL,
    server_id INT NOT NULL UNIQUE,
    server_ip VARCHAR(255) NOT NULL,
    create_at VARCHAR(255) NOT NULL,
    update_at VARCHAR(255) NOT NULL,
    is_combined TINYINT DEFAULT 0,
    PRIMARY KEY(id)
)
"""

CREATE_LOG_TB = """
CREATE TABLE IF NOT EXISTS `logs` (
    id INTEGER AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    opt VARCHAR(255) NOT NULL,
    create_at VARCHAR(255) NOT NULL,
    day_time VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
)
"""

INSERT_USER_LOG = """
INSERT INTO logs 
    (username, opt, create_at, day_time)
VALUES
    (:username, :opt, :create_at, :day_time)
"""


SELECT_ALL_USERS = """
SELECT username
FROM users;
"""

DELETE_ONE_USER = """
DELETE FROM users
WHERE username = '{}'
"""

SELECT_USER_LOG = """
SELECT username, opt, create_at
FROM logs
WHERE username='{}'
AND day_time='{}'
"""

SELECT_ZONES_TB = """
SHOW TABLES LIKE '%_zones'
"""

SELECT_SERVE_IP = """
SELECT DISTINCT server_ip  
FROM `{}`
"""

INSERT_ZONE_INFO = """
INSERT INTO `{}` 
    (server_name, server_id, server_ip, create_at, update_at, is_combined)
VALUES
    (:server_name, :server_id, :server_ip, :create_at, :update_at, :is_combined)
"""

GET_ZONE_LIST = """
SELECT server_name, server_id, server_ip
FROM `{}`
WHERE is_combined = 0 
ORDER BY server_id; 
"""