import os
import typing
import grpc
from concurrent import futures
from app import AppConfig, core, AppLogger
from app.grpc.zone import zone_pb2, zone_pb2_grpc


def load_cert_file(filename: str) -> bytes:
    """加载认证文件"""
    realpath = os.path.join(
        os.path.dirname(__file__), filename
    )
    with open(realpath, "rb") as fd:
        return fd.read()


root_cert = load_cert_file("../../certs/ca.crt")
server_crt = load_cert_file("../../certs/server.crt")
server_key = load_cert_file("../../certs/server.key")


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
        expected_metadata = (AppConfig.get("app", "rpcKey"), method_name[::-1])
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        return self._abort_handler


class LoggerInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self):
        pass

    def intercept_service(
        self,
        continuation: typing.Callable[
            [grpc.HandlerCallDetails], typing.Awaitable[grpc.RpcMethodHandler]
        ],
        handler_call_details: grpc.HandlerCallDetails
    ) -> None:
        method_name = method_name = handler_call_details.method.split("/")[-1]
        AppLogger.info("调用了方法: ", method_name)


class ZoneService(zone_pb2_grpc.ZoneServicer):
    def option(
        self,
        request: zone_pb2.ZoneRequest,
        context
    ) -> zone_pb2.ZoneResponse:
        if request.target == "addition":
            resp = core.add_zone(request)
        elif request.target == "updatebin":
            resp = core.upt_bin(request)
        elif request.target == "updatecon":
            resp = core.upt_con(request)
        else:
            resp = core.opt_zone(request)
        return zone_pb2.ZoneResponse(
            name=request.name, number=request.number, ip=request.ip, result=resp
        )


def start_server() -> typing.Tuple[grpc.Server, int]:
    server = grpc.server(
        futures.ThreadPoolExecutor(
            max_workers=AppConfig.getint("app", "worker")),
            interceptors=(SignatureInterceptor(), LoggerInterceptor()))
    zone_pb2_grpc.add_ZoneServicer_to_server(ZoneService(), server)
    server_credentials = grpc.ssl_server_credentials(
        ((server_key, server_crt), ), root_cert, True)
    addr = "{0}:{1}".format(
        AppConfig.get('app', 'host'),
        AppConfig.get('app', 'port')
    )
    port = server.add_secure_port(addr, server_credentials)
    try:
        server.start()
        return server, port
    except grpc.RpcError:
        server.stop(0)
