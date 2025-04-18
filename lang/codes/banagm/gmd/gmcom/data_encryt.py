# -*- coding: utf-8 -*-
"""
套接字数据加密
openssl genrsa -out private_key.pem 512
pyrsa-priv2pub -i private_key.pem -o public_key.pem
"""
from rsa import common,encrypt,decrypt,PublicKey,PrivateKey
from gmcom.config import gmdcon


class DataEncrypt:
    def __init__(self, pubFile=gmdcon.pub_file, priFile=gmdcon.pri_file):
        self.pub_file = pubFile
        self.pri_file = priFile

    def get_max_len(self, rsa_key, encrypt=True):
        block_size = common.byte_size(rsa_key.n)
        recv_size = 12
        if not encrypt:
            recv_size = 0
        max_len = block_size - recv_size
        return  max_len

    def encryt_data(self, data):
        data = bytes(data, encoding='utf-8')
        out_data = b''
        with open(self.pub_file, 'rb') as fd:
            pub_data = fd.read()
            pub_key = PublicKey.load_pkcs1(pub_data)
            max_len = self.get_max_len(pub_key)
            while data:
                in_data = data[:max_len]
                data = data[max_len:]
                out_data += encrypt(in_data, pub_key)
        return out_data

    def decryt_data(self, data):
        out_data = b""
        with open(self.pri_file, 'rb') as fd:
            pri_data = fd.read()
            pri_key = PrivateKey.load_pkcs1(pri_data)
            max_len = self.get_max_len(pri_key, False)
            while data:
                in_data = data[:max_len]
                data = data[max_len:]
                out_data += decrypt(in_data, pri_key)
        return str(out_data, "utf-8")


gmdcry = DataEncrypt()
__all__ = [gmdcry]