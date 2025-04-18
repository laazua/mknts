import time
from twisted.internet import protocol


class ZombieServer(protocol.Protocol):
    def dataReceived(self, data):
        # 收到客户端发送的数据后，将其打印出来并发送回去
        print("Received:", data)
        time.sleep(5)
        self.transport.write(b"hello client")

    def connectionLost(self, reason) -> None:
        print(reason.value)


class ZombieFactory(protocol.Factory):
    def buildProtocol(self, addr):
        print(f"Client Address: {addr}")
        return ZombieServer()
