### socket

- pip install cryptography

- **服务端代码**
```python
import socket
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

HOST = ""  # 监听所有可用接口
PORT = 50005  # 任意非特权端口
KEY = b"\xc8\xfe\x1f\xf5\x87DI\r\xe7\xbb\x02\x13\xe6B~\xd02\x0b]}R\x13\xc0\x00\x01LP\n\x90\x19\xdbe"  # 生成一个随机的32字节密钥
IV = b"\xbc\x1bZ\x9a\xd5\xfc\x90\x7f\x16J\xb2\x05\xf3\xa9J9"  # 生成一个随机的16字节初始向量（IV）


# 初始化AES加密器
def encrypt(data):
    # 数据填充到16的倍数
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data) + encryptor.finalize()


# 解密函数
def decrypt(data):
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(data) + decryptor.finalize()

    # 去填充
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted_data) + unpadder.finalize()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            # 接收4个字节，表示消息长度
            length_data = conn.recv(4)
            if not length_data:
                break
            # 使用struct解包获取消息长度
            length = struct.unpack("!I", length_data)[0]
            # 根据消息长度接收消息内容
            data = decrypt(conn.recv(length))
            if not data:
                break
            # 处理接收到的数据
            print("Received:", data.decode("utf-8"))
            # 发送回客户端
            conn.sendall(data)
```

- **客户端代码**
```python
import sys
import socket
import struct

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

HOST = "localhost"  # 服务端地址
PORT = 50005  # 服务端端口
# KEY = os.urandom(32)  # 生成一个随机的32字节密钥
# IV = os.urandom(16)  # 生成一个随机的16字节初始向量（IV）
KEY = b"\xc8\xfe\x1f\xf5\x87DI\r\xe7\xbb\x02\x13\xe6B~\xd02\x0b]}R\x13\xc0\x00\x01LP\n\x90\x19\xdbe"
IV = b"\xbc\x1bZ\x9a\xd5\xfc\x90\x7f\x16J\xb2\x05\xf3\xa9J9"


# 初始化AES加密器
def encrypt(data):
    # 数据填充到16的倍数
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data) + encryptor.finalize()


# 解密函数
def decrypt(data):
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(data) + decryptor.finalize()

    # 去填充
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted_data) + unpadder.finalize()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter message: ")
        if not message:
            break
        if message == "exit":
            sys.exit(0)
        # 将消息编码为字节
        data = encrypt(message.encode("utf-8"))
        # 使用struct打包消息长度
        length = struct.pack("!I", len(data))
        # 发送消息长度和消息内容
        s.sendall(length + data)
        # 接收服务端返回的数据
        data = s.recv(1024)
        print("Received from server:", data.decode("utf-8"))
```