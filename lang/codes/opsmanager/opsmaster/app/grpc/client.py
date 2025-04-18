import os
import grpc
import typing
import contextlib
from app import AppConfig, AppLogger
from app.grpc.zone import zone_pb2, zone_pb2_grpc


def load_cert_file(filename: str) -> bytes:
    """加载认证文件"""
    realpath = os.path.join(
        os.path.dirname(__file__), filename
    )
    with open(realpath, "rb") as fd:
        return fd.read()


root_cert = load_cert_file("../../certs/ca.crt")
client_crt = load_cert_file("../../certs/client.crt")
client_key = load_cert_file("../../certs/client.key")


class AuthGateway(grpc.AuthMetadataPlugin):
    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback
    ) -> None:
        signature = context.method_name[::-1]
        callback(((AppConfig.get("app", "rpcKey"), signature), ), None)


@contextlib.contextmanager
def create_channel(addr: str) -> grpc.Channel:
    call_credential = grpc.metadata_call_credentials(
        AuthGateway(), name="auth gateway")
    channel_credential = grpc.ssl_channel_credentials(
        root_certificates=root_cert,
        private_key=client_key,
        certificate_chain=client_crt)
    composite_credential = grpc.composite_channel_credentials(
        channel_credential, call_credential)

    yield grpc.secure_channel(addr, composite_credential)


def zone_service(zone: typing.Dict[str, typing.Any]) -> zone_pb2.ZoneResponse:
    """远程区服服务调用"""
    address = f"{zone['ip']}:{AppConfig.get('app', 'rport')}"
    with create_channel(address) as channel:
        stub = zone_pb2_grpc.ZoneStub(channel)
        request = zone_pb2.ZoneRequest(
            name=zone["name"],
            number=zone["number"],
            ip=zone["ip"],
            target=zone["target"],
            svnversion=zone["svnversion"],
        )
        try:
            return stub.option(request)
        except grpc.RpcError as e:
            AppLogger.error("区服远程调用出错", e)
            return None