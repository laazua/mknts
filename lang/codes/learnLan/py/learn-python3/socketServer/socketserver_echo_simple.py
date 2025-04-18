# -*-coding:utf-8-*-
import socket
import socketserver
import threading


class EchoRequestHandler(socketserver.BaseRequestHandler):
    # 业务逻辑处理函数
    def handle(self):
        # echo the data back to the client
        data = self.request.recv(1024)
        self.request.send(data)

        return


if __name__ == '__main__':

    # let kernel assign a port
    address = ('127.0.0.1', 0)
    server = socketserver.TCPServer(address, EchoRequestHandler)
    # what port was assigned?
    ip, port = server.server_address

    # start the server in a thread
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send the data
    message = 'hello, world'.encode()
    print('sending : {!r}'.format(message))
    len_sent = s.send(message)

    # receive a response
    response = s.recv(len_sent)
    print('Received: {!r}'.format(response))

    # clean up
    server.shutdown()
    s.close()
    server.socket.close()
