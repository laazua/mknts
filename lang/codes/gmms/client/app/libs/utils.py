import datetime
import concurrent
from jose import jwt
from jose import JWSError
from fastapi import Depends
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from app.libs.config import AppCon
from app.libs.resource import CREDENTIALS_EXCEPTION
from app.libs.rpyc_client import RpcClient


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/api/login")


def encode_password(password):
    return pwd_cxt.hash(password)


def verify_password(plain_password, encode_password):
    return pwd_cxt.verify(plain_password, encode_password)


def create_token(data):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=AppCon.expire_minutes)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, AppCon.key_word, algorithm="HS256")
    return encode_jwt


def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, AppCon.key_word, algorithms=["HS256"])
        username = payload.get('username')
        if not username:
            raise credentials_exception
        token_data = {"username": username}
        return token_data
    except JWSError:
        raise credentials_exception


def get_current_user(data: str = Depends(oauth2_scheme)):
    """获取当前user token信息"""
    return verify_token(data, CREDENTIALS_EXCEPTION)


def format_time(time):
    return '-'.join([ "0"+x if int(x) < 10 else x for x in time.split("-") ])
    # times = []
    # for i in time.split("-"):
    #     if int(i) <= 9:
    #         i = "0" + i
    #         times.append("-")
    #     times.append(i)
    # return ''.join(times)

def get_conn(ip):
    rpc = RpcClient(ip, 2004)
    conn = rpc.root
    return conn


def concurrent_rpc_svn(ips):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(ips)) as executor:
        future_conn = {executor.submit(get_conn, ip[0]): ip for ip in ips}
        return [(future.result(timeout=600), future_conn[future][0]) for future in concurrent.futures.as_completed(future_conn)]