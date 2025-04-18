import os
import grpc
import contextlib
from concurrent import futures
from auth_helloworld import helloworld_pb2
from auth_helloworld import helloworld_pb2_grpc


def _load_credential_file(filepath):
    real_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(real_path, 'rb') as fd:
        return fd.read()


_root_certificate = _load_credential_file("./cert/ca.crt")
_serv_certificate_crt = _load_credential_file("./cert/server.crt")
_serv_certificate_key = _load_credential_file("./cert/server.key")


class SignatureInterceptor(grpc.ServerInterceptor):
    def __init__(self):
        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid signature')
        self._abortion = grpc.unary_unary_rpc_method_handler(abort)
    
    def intercept_service(self, continuation, handler_call_details):
        method_name = handler_call_details.method.split('/')[-1]
        expected_metadata = ('x-signature', method_name[::-1])
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        return self._abortion


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    """重写父类方法"""
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"hello {request.name}")


@contextlib.contextmanager
def service():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4),
        interceptors=(SignatureInterceptor(),))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server_credentials = grpc.ssl_server_credentials(((
        _serv_certificate_key, _serv_certificate_crt
    ),), _root_certificate, True)

    port = server.add_secure_port("test.grpc.com:5000", server_credentials)
    print(f"server run on :{port}")
    server.start()
    try:
        yield server, port
    finally:
        server.stop(0)


if __name__ == "__main__":
    with service() as (server, port):
        server.wait_for_termination()