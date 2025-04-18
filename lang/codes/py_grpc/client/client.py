import grpc
from helloworld import helloworld_pb2
from helloworld import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        resp = stub.SayHello(helloworld_pb2.HelloRequest(name="zhangsan"))
    print("Greeter client received: ", resp.message)


if __name__ == "__main__":
    run()
