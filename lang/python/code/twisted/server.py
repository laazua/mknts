import json
import struct
import sys
from twisted.internet import reactor, protocol
from twisted.python import log
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes


class EchoServer(protocol.Protocol):
    def __init__(self):
        # 从文件加载私钥
        with open("private_key.pem", "rb") as key_file:
            self.private_key = serialization.load_pem_private_key(
                key_file.read(), password=None
            )
        self.buffer = b""
        self.msg_length = None

    def dataReceived(self, data):
        self.buffer += data

        while True:
            if self.msg_length is None:
                if len(self.buffer) >= 4:
                    self.msg_length = struct.unpack("!I", self.buffer[:4])[0]
                    self.buffer = self.buffer[4:]
                else:
                    break

            if self.msg_length is not None:
                if len(self.buffer) >= self.msg_length:
                    encrypted_message = self.buffer[: self.msg_length]
                    self.buffer = self.buffer[self.msg_length :]
                    self.msg_length = None
                    self.handle_message(encrypted_message)
                else:
                    break

    def handle_message(self, encrypted_message):
        try:
            # 解密数据
            decrypted_data = self.private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            # 将解密后的数据从字节转换为字符串
            decrypted_str = decrypted_data.decode("utf-8")
            # 解析 JSON 数据
            json_data = json.loads(decrypted_str)
            print("Received JSON data:", json_data)
        except Exception as e:
            print("Failed to decrypt or parse JSON:", e)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return EchoServer()


# 启动服务器
reactor.listenTCP(8000, EchoFactory())

log.startLogging(sys.stdout)
print("Server started on port 8000")
reactor.run()
