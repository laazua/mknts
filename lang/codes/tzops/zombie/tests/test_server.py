from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        # 收到客户端发送的数据后，将其打印出来并发送回去
        print("Received:", data)
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


# 创建一个 TCP 服务器，并监听在指定的端口上
reactor.listenTCP(1234, EchoFactory())
# 启动事件循环
reactor.run()
