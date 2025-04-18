# -*-coding:utf-8-*-
import os
import socketserver
import socket
import threading


class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    # 业务逻辑重写该函数
    def handle(self):
        # echo the data back to the client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d: %s' % (cur_pid, data)
        self.request.send(response)

        return


class ForkingEchoServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    # let the kernel assign a port
    address = ('localhost', 0)
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    # what port was assigned?
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    # do not hang on exit
    t.setDaemon(True)
    t.start()
    print('server loop running in process:', os.getpid())

    # connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send the data
    message = 'hello world'.encode()
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    # receive a response
    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    # clean up
    server.shutdown()
    s.close()
    server.socket.close()
