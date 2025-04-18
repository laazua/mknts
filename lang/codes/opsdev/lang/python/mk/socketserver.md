### socketserver模块

- 回显服务器服务端
```python
import socketserver


class MHandler(socketserver.baseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                break

            print(f"recv dat: {data.decode()}")
            self.request.send(data)


if __name__ == "__main__":
    address = ("localhost", 9988)
    print(f"listen on {address}")
    server = socketserver.ThreadingTCPServer(address, MHandler)
    server.serve_forever()
```

- 回显服务器客户端
```python
import time
import socket


address = ("localhost", 9988)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(address)
    sock.send(b"hello world")
    time.sleep(20)
    data = sock.recv(1024)
    print(f"recv data: {data.decode()}")
```

- 聊天服务器服务端
```python
import socketserver

# 服务器配置
HOST = '127.0.0.1'  # 服务器地址
PORT = 9988        # 端口号

class ChatHandler(socketserver.BaseRequestHandler):
    clients = []

    def handle(self):
        # 将当前连接的客户端添加到客户端列表
        ChatHandler.clients.append(self.request)
        print(f"新客户端连接: {self.client_address}")

        try:
            while True:
                # 接收客户端消息
                message = self.request.recv(1024).strip()
                if message:
                    print(f"收到消息: {message.decode()}")
                    self.broadcast(message)
                else:
                    break
        finally:
            # 客户端断开时，移除该客户端并关闭连接
            ChatHandler.clients.remove(self.request)
            self.request.close()
            print(f"客户端断开连接: {self.client_address}")

    def broadcast(self, message):
        """广播消息到所有连接的客户端"""
        for client in ChatHandler.clients:
            if client != self.request:
                try:
                    client.sendall(message)
                except:
                    # 如果发送失败，移除该客户端
                    ChatHandler.clients.remove(client)

# 启动服务器
def start_server():
    server = socketserver.ThreadingTCPServer((HOST, PORT), ChatHandler)
    print(f"服务器已启动，等待连接...")
    server.serve_forever()

# 启动服务器
if __name__ == "__main__":
    start_server()
```

- 聊天服务器客户端
```python
import socket
import threading

# 服务器配置
HOST = '127.0.0.1'  # 服务器地址
PORT = 9988        # 端口号

# 连接到服务器
def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    print(f"收到消息: {message.decode()}")
                else:
                    break
            except:
                break

    # 启动接收消息的线程
    threading.Thread(target=receive_messages).start()

    while True:
        message = input("请输入消息: ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())

    client_socket.close()

# 启动客户端
if __name__ == "__main__":
    connect_to_server()
```