import os
import grpc
import contextlib
from auth_helloworld import helloworld_pb2
from auth_helloworld import helloworld_pb2_grpc


def _load_credential_file(filepath):
    real_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(real_path, 'rb') as fd:
        return fd.read()


_root_certificate = _load_credential_file("./cert/ca.crt")
_clt_certificate_crt = _load_credential_file("./cert/client.crt")
_clt_certificate_key = _load_credential_file("./cert/client.key")


class AuthGateway(grpc.AuthMetadataPlugin):
    def __call__(self, context, callback):
        signature = context.method_name[::-1]
        callback((('x-signature', signature), ), None)


@contextlib.contextmanager
def create_client_channel():
    call_credential = grpc.metadata_call_credentials(AuthGateway(), name='auth gateway')
    channel_credential = grpc.ssl_channel_credentials(
        _root_certificate, _clt_certificate_key,_clt_certificate_crt)
    composite_credentials = grpc.composite_channel_credentials(channel_credential, call_credential)
    channel = grpc.secure_channel("test.grpc.com:5000", composite_credentials)
    yield channel


def run(channel):
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    request = helloworld_pb2.HelloRequest(name='zhangsan')
    try:
        response = stub.SayHello(request)
    except grpc.RpcError as e:
        return e
    else:
        print(response.message)
        return response


if __name__ == "__main__":
    with create_client_channel() as channel:
        run(channel)