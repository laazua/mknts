from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        # 当与服务器建立连接时，发送一条消息
        self.transport.write(rb"Hello, server!")

    def dataReceived(self, data):
        # 收到服务器的回复后，将其打印出来
        print("Server said:", data)
        # 收到响应后断开连接
        self.transport.loseConnection()


class EchoClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        print(f"Server Address: {addr}")
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print(connector)
        print(reason.value)
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print(connector)
        print(reason)
        print("Connection lost.")
        reactor.stop()


# 创建一个 TCP 客户端，连接到指定的服务器和端口
reactor.connectTCP("localhost", 8000, EchoClientFactory())
# 启动事件循环
reactor.run()
