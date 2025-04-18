import socket
import struct
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import json

# 从文件加载服务器公钥
with open("pem/public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# 准备 JSON 数据
json_data1 = json.dumps(
    {"name": "zhangsan", "addr": "成都", "age": 15, "school": "成都七中"}
).encode("utf-8")

json_data2 = json.dumps(
    {"name": "lisi", "addr": "成都", "age": 12, "school": "成都七中"}
).encode("utf-8")

# 加密 JSON 数据
encrypted_data1 = public_key.encrypt(
    json_data1,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

encrypted_data2 = public_key.encrypt(
    json_data2,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)


# 创建 socket 并连接服务器
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8000))

# 发送数据长度和加密数据
data_length1 = struct.pack("!I", len(encrypted_data1))
data_length2 = struct.pack("!I", len(encrypted_data2))

try:
    import threading

    thread1 = threading.Thread(
        target=sock.sendall, args=(data_length1 + encrypted_data1,)
    )
    thread2 = threading.Thread(
        target=sock.sendall, args=(data_length2 + encrypted_data2,)
    )
    thread1.start()
    thread2.start()

    # 等待所有线程结束
    thread1.join()
    thread2.join()

except Exception:
    sock.close()
