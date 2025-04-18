import os
import grpc
import typing
from concurrent import futures
from app.config import cfg
from app.internal import core
from app.internal.grpc.zone import zone_pb2, zone_pb2_grpc


def _load_credential_file(file_path: str) -> bytes:
    """加载认证文件"""
    real_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(real_path, "rb") as fd:
        return fd.read()


_root_certificate = _load_credential_file("../../../cert/ca.crt")
_server_certificate_crt = _load_credential_file("../../../cert/server.crt")
_server_certificate_key = _load_credential_file("../../../cert/server.key")


class SignatureInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self):
        def abort(_, context: grpc.aio.ServicerContext) -> None:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid signature")
        self._abort_handler = grpc.unary_unary_rpc_method_handler(abort)

    def intercept_service(
        self,
        continuation: typing.Callable[
            [grpc.HandlerCallDetails], typing.Awaitable[grpc.RpcMethodHandler]
        ],
        handler_call_details: grpc.HandlerCallDetails
    ) -> grpc.RpcMethodHandler:
        method_name = handler_call_details.method.split("/")[-1]
        expected_metadata = ("x-signature", method_name[::-1])
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        return self._abort_handler


class ZoneService(zone_pb2_grpc.ZoneServicer):
    def zone_option(
        self,
        request: zone_pb2.ZoneReq,
        context
    ) -> zone_pb2.ZoneResp:
        match request.target:
            case "add":
                resp = core.add_zone(request)
            case "uptbin":
                resp = core.upt_bin(request)
            case "uptcon":
                resp = core.upt_conf(request)
            case "start":
                resp = core.zone_opt(request)
            case "stop":
                resp = core.zone_opt(request)
            case "check":
                resp = core.zone_opt(request)
            case _:
                resp = f"{request.target}是未知的命令"
        return zone_pb2.ZoneResp(
            zname=request.zname, zid=request.zid, zip=request.zip, result=resp
        )


def start_server() -> typing.Tuple[grpc.server, int]:
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=cfg.getint("app", "worker")),
        interceptors=(SignatureInterceptor(),)
        )
    zone_pb2_grpc.add_ZoneServicer_to_server(ZoneService(), server)
    server_credentials = grpc.ssl_server_credentials(
        ((_server_certificate_key, _server_certificate_crt),),
        _root_certificate, True
    )
    addr = f"{cfg.get('app', 'host')}:{cfg.get('app', 'port')}"
    port = server.add_secure_port(addr, server_credentials)
    try:
        server.start()
        return server, port
    except grpc.RpcError:
        server.stop(0)
