# -*-coding:utf-8-*-
import threading
import socketserver
import socket


class ThreadedEchoRequestHandler(socketserver.BaseRequestHandler):
    # 业务逻辑处理函数
    def handle(self):
        # echo the data back to the client
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = b'%s: %s' % (cur_thread.getName().encode(), data)
        self.request.send(response)

        return


class ThreadedEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    # let the kernel assign a port
    address = ('127.0.0.1', 0)
    server = ThreadedEchoServer(address, ThreadedEchoRequestHandler)
    # what port assigned
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print('Server loop running in thread:', t.getName())

    # connect to the server.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send the data
    message = b'hello world'
    print('sending : {!r}'.format(message))
    len_sent = s.send(message)

    # receive a response
    response = s.recv(1024)
    print('received: {!r}'.format(response))

    # clean up
    server.shutdown()
    s.close()
    server.socket.close()
