# socketserver异步使用示例
import socketserver


class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} connected")
        print(data)
        self.request.sendall(data.upper())


if __name__ == '__main__':
    # socketserver.ThreadingTCPServer已经封装了ThreadingMinIn
    with socketserver.ThreadingTCPServer(('0.0.0.0', 8888), TCPHandler) as serve:
        serve.serve_forever()