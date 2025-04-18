### socket模块

- 回显服务器服务端
```python
import socket


address = ("localhost", 9988)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print(f"listen on {address}")
    sock.bind(address)
    sock.listen(5)
    while True:
        conn, client_address = sock.accept()
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"recv data: {data.decode()}")
                _ = conn.send(data)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
            print(f"close connect: {client_address}")        
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
import socket
import threading

# 服务器配置
HOST = '127.0.0.1'  # 服务器地址
PORT = 9988        # 端口号

# 客户端连接列表
clients = []

# 发送消息到所有客户端
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# 处理客户端连接
def handle_client(client_socket):
    while True:
        try:
            # 接收客户端的消息
            message = client_socket.recv(1024)
            if message:
                print(f"收到消息: {message.decode()}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break
    
    # 断开连接时，从客户端列表中移除该连接
    clients.remove(client_socket)
    client_socket.close()

# 启动服务器
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"服务器已启动，等待连接...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"客户端连接：{client_address}")
        clients.append(client_socket)
        
        # 创建线程来处理每个客户端
        threading.Thread(target=handle_client, args=(client_socket,)).start()

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