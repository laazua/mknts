import os
import grpc
import typing
import contextlib
from app import cfg
from .zone import zone_pb2
from .zone import zone_pb2_grpc
from app.internal.core import logger


def _load_credential_file(file_path: str) -> bytes:
    """加载认证文件"""
    real_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(real_path, "rb") as fd:
        return fd.read()


_root_certificate = _load_credential_file("../../../cert/ca.crt")
_client_certificate_crt = _load_credential_file("../../../cert/client.crt")
_client_certificate_key = _load_credential_file("../../../cert/client.key")


class AuthGateway(grpc.AuthMetadataPlugin):
    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback
    ) -> None:
        signature = context.method_name[::-1]
        callback((("x-signature", signature), ), None)


@contextlib.contextmanager
def create_channel(addr: str) -> grpc.Channel:
    call_credential = grpc.metadata_call_credentials(
        AuthGateway(), name="auth gateway")
    channel_credential = grpc.ssl_channel_credentials(
        root_certificates=_root_certificate,
        private_key=_client_certificate_key,
        certificate_chain=_client_certificate_crt)
    composite_credential = grpc.composite_channel_credentials(
        channel_credential, call_credential)

    channel = grpc.secure_channel(addr, composite_credential)
    yield channel


def zone_service(zone: typing.Dict[str, typing.Any]) -> zone_pb2.ZoneResp:
    """远程区服服务调用"""
    address = f"{zone['zip']}:{cfg.get('zservant', 'port')}"
    with create_channel(address) as channel:
        stub = zone_pb2_grpc.ZoneStub(channel)
        request = zone_pb2.ZoneReq(
            zid=zone["zid"],
            zname=zone["zname"],
            zip=zone["zip"],
            target=zone["target"],
            zsvnversion=zone["zsvnversion"]
        )
        try:
            return stub.zone_option(request)
        except grpc.RpcError as e:
            logger.error("区服远程调用出错", e)
            return None
