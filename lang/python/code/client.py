import socket
import struct


def send_message(sock, message):
    # 计算消息长度，并转换为网络字节顺序
    msg_len = len(message)
    header = struct.pack("!I", msg_len)

    # 发送消息头
    sock.sendall(header)

    # 发送消息体
    sock.sendall(message.encode("utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # 创建一个TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 连接服务器
        sock.connect((HOST, PORT))

        # 发送测试消息
        send_message(
            sock,
            "hello world xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz",
        )

        # 接收服务器响应
        response_header = sock.recv(4)
        response_len = struct.unpack("!I", response_header)[0]
        response = sock.recv(response_len).decode("utf-8")
        print("Recive server reponse: ", response)
