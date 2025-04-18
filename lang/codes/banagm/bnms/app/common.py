# -*- coding: utf-8 -*-
# 公共工具集

import json
import struct
import socket
import rsa
from rsa import PublicKey, PrivateKey
from rsa import common
from concurrent.futures import ProcessPoolExecutor 
from app.config import cnf

from jose import JWSError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import cnf
from app.schemas import TokenData


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/api/login")


class PwHash:
    """password加密&&password验证"""
    @classmethod
    def encode_password(cls, password: str):
        return pwd_cxt.hash(password)

    @classmethod
    def verify_password(cls, encode_password: str, plain_password: str):
        return pwd_cxt.verify(plain_password, encode_password)


class Token:
    """创建token&&token认证"""
    @classmethod
    def create_token(cls, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=cnf.expire_minutes)
        to_encode.update({'exp': expire})
        encode_jwt = jwt.encode(to_encode, cnf.key_word, algorithm=cnf.algorithms)
        return encode_jwt

    @classmethod
    def verify_token(cls, token, credentials_exception):
        try:
            payload = jwt.decode(token, cnf.key_word, algorithms=[cnf.algorithms])
            username: str = payload.get('username')
            rolename: str = payload.get('rolename')
            if not username and not rolename:
                raise credentials_exception
            token_data = TokenData(username=username, rolename=rolename)
            return token_data
        except JWSError:
            raise credentials_exception


def get_current_user(token: str = Depends(oauth2_scheme)):
    """获取当前user token信息"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={'authorization': 'Bearer'}
    )

    return Token.verify_token(token, credentials_exception)


PUB_FILE = cnf.app_path + "/app" + "/pem/public_key.pem"
PRI_FILE = cnf.app_path + "/app" + "/pem/private_key.pem"


def get_max_len(rsa_key, encrypt=True):
    block_size = common.byte_size(rsa_key.n)
    recv_size = 12
    if not encrypt:
        recv_size = 0
    max_len = block_size - recv_size
    return  max_len


def encryt_data(data):
    data = bytes(data, encoding="utf-8")
    out_data = b""
    with open(PUB_FILE, 'rb') as fd:
        pub_data = fd.read()
        pub_key = PublicKey.load_pkcs1(pub_data)
        max_len = get_max_len(pub_key)
        while data:
            in_data = data[:max_len]
            data = data[max_len:]
            out_data += rsa.encrypt(in_data, pub_key)
    return out_data


def decryt_data(data):
    out_data = b""
    with open(PRI_FILE, 'rb') as fd:
        pri_data = fd.read()
        pri_key = PrivateKey.load_pkcs1(pri_data)
        max_len = get_max_len(pri_key, False)
        while data:
            in_data = data[:max_len]
            data = data[max_len:]
            out_data += rsa.decrypt(in_data, pri_key)
    return str(out_data, "utf-8")


def handle_socket(ip, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
    sock.settimeout(30*1000)
    sock.connect((ip, cnf.mg_port))
    send_data = pack_data(data) 
    sock.send(bytes(send_data))
    recv_data = sock.recv(4096)
    sock.close()
    return decryt_data(recv_data)


def pack_data(data):
    # 自定义数据包协议
    version = 1.0
    body = encryt_data(json.dumps(data))
    place_holder = 64
    header = [version, body.__len__(), place_holder]
    try:
        # "!3I" 表示按原字节数,1个浮点型,2个无符号整数
        header_pack = struct.pack("!1f2I", *header)  
        send_data = header_pack + body
        return send_data
    except struct.error as e:
        raise e


async def send_data(serv_list):
    recv_data = []
    print(serv_list)
    with ProcessPoolExecutor(max_workers=5) as executor:
        for i in range(len(serv_list)):
            try:
                ret = executor.submit(handle_socket, serv_list[i]['serverIp'], serv_list[i])
                data = json.loads(ret.result())
                data['ip'] = serv_list[i]['serverIp']
            except Exception:
                data = None
            recv_data.append(data)
    return recv_data