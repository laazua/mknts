import grpc
import concurrent.futures as futures
from helloworld import helloworld_pb2 
from helloworld import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"hello {request.name}")


def service():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    print("server start on :5000")
    server.wait_for_termination()


if __name__ == "__main__":
    service()