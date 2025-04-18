import sys
import threading
import socketserver


class MyTcpHandler(socketserver.BaseRequestHandler):
    """Tcp Handler"""
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(self.data)

        self.sendall(self.data)


class MyUdpHandler(socketserver.BaseRequestHandler):
    """Udp Handler"""
    def handle(self):
        pass


class MyUnixStreamHandler(socketserver.BaseRequestHandler):
    """UnixStream"""
    def handle(self):
        pass


class MyUnixDatagramHandler(socketserver.BaseRequestHandler):
    """UnixDatagram"""
    def handle(self):
        pass


class MyThreadTcpHandler(socketserver.BaseRequestHandler):
    """Thread Tcp Handler"""
    def handle(self):
        pass


class MyThreadUdpHandler(socketserver.BaseRequestHandler):
    """thread Udp Handler"""
    def handle(self):
        pass


class MyThreadUnixStreamHandler(socketserver.BaseRequestHandler):
    """Thread Unixstream Handler"""
    def handle(self):
        pass


class MyThreadUnixDatagramHandler(socketserver.BaseRequestHandler):
    """Thread Unixdatagram Handler"""
    def handle(self):
        pass


#########################异步类的另一种实现###########################
class MyThreadTcpRequestHandler(socketserver.BaseRequestHandler):
    """Handler"""
    def handle(self):
        pass


class MyThreadTcpServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Server"""
    pass


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8000
    if len(sys.argv) != 2:
        print(sys.argv[0], "tcp|unixs|udp|unixd|ttcp|tunixs|tudp|tunidxd")
        sys.exit(0)

    ### TCP
    if sys.argv[1] == "tcp":
        with socketserver.TCPServer((HOST, PORT), MyTcpHandler) as server:
            print("TCP Server start...")
            server.serve_forever()

    ### UnixStream
    if sys.argv[1] == "unixs":
        with socketserver.UnixStreamServer("", MyUnixStreamHandler) as server:
            print("UnixStream Server start...")
            server.serve_forever()
    ### UDP
    if sys.argv[1] == "udp":
        with socketserver.UDPServer((HOST, PORT), MyUdpHandler) as server:
            print("UDP Server start...")
            server.serve_forever()

    ### UnixDatagram
    if sys.argv[1] == "unixd":
        with socketserver.UnixDatagramServer("", MyUnixDatagramHandler) as server:
            print("UnixDatagram Server start...")
            server.serve_forever()


    ###### ThreadingMinxIn 实现异步 ######

    ### 异步TCP
    if sys.argv[1] == "ttcp":
        with socketserver.ThreadingTCPServer((HOST, PORT), MyThreadTcpHandler) as server:
            print("thread tcp server start...")
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            try:
                while True:
                    pass
            except KeyboardInterrupt:
                server.shutdown()

    ### 异步 unixstream
    if sys.argv[1] == "tunixs":
        with socketserver.ThreadingUnixStreamServer("", MyThreadUnixStreamHandler) as server:
            pass

    ### 异步UDP
    if sys.argv[1] == "tudp":
        with socketserver.ThreadingUDPServer((HOST, PORT), MyThreadUdpHandler) as server:
            pass

    ### 异步 unixdatagram
    if sys.argv[1] == "tunixd":
        with socketserver.ThreadingUnixDatagramServer("", MyThreadUnixDatagramHandler) as server:
            pass


    ###### ForkingMinxIn 实现 异步 ######

    ### 异步 TCP
    # with socketserver.ForkingTCPServer() as server:
    #     pass

    ### 异步 unixstream
    # with socketserver.ForkingUnixStreamServer() as server:
    #     pass

    ### 异步 UDP
    # with socketserver.ForkingUDPServer() as server:
    #     pass

    ### 异步 unxidatagram
    # with socketserver.ForkingUnixDatagramServer() as server:
    #     pass


    #########################异步类的另一种调用###########################
    with MyThreadTcpServer((HOST, PORT), MyThreadTcpRequestHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            server.shutdown()

    # 其他udp, unixstream, unixdatagram服务的实现类似