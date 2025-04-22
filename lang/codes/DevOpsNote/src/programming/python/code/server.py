import socketserver
import struct
import threading


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("客户端 {} 已连接".format(self.client_address))
        while True:
            # 读取4字节的消息头，其中包含消息的长度
            header = self.request.recv(4)
            if not header:
                break
            msg_len = struct.unpack("!I", header)[0]

            # 根据消息长度读取完整消息
            msg = b""
            total_received = 0
            while total_received < msg_len:
                chunk = self.request.recv(min(msg_len - total_received, 4096))
                if not chunk:
                    break
                msg += chunk
                total_received += len(chunk)

            if total_received < msg_len:
                print("接收到的消息长度不足，可能出现了粘包问题")
                continue

            print("Recive client message: ", msg.decode("utf-8"))
            # 可在此处添加处理收到消息的逻辑

            # 响应客户端
            response = "Recive client message: {}".format(msg.decode("utf-8")).encode(
                "utf-8"
            )
            response_header = struct.pack("!I", len(response))
            self.request.sendall(response_header + response)


class ThreadedTCPServer(socketserver.ThreadingTCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # 创建多线程服务器
    server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # 启动服务器，等待客户端连接
    print("服务器已启动，等待客户端连接...")

    # 主线程等待服务器线程退出
    server_thread.join()
