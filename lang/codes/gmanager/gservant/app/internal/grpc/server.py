import grpc
from concurrent import futures
from typing import Awaitable, Callable, Tuple
from config import cfg
from internal.core.zone import \
    add_zone, upt_conf, upt_bin, zone_opt
from internal.grpc import credentials


class SignatureInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self):
        def abort(_, context: grpc.aio.ServicerContext) -> None:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid signature")
        self._abort_handler = grpc.unary_unary_rpc_method_handler(abort)
    
    def intercept_service(
        self, 
        continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]],
        handler_call_details: grpc.HandlerCallDetails
    ) -> grpc.RpcMethodHandler:
        method_name = handler_call_details.method.split("/")[-1]
        expected_metadata = ("x-signature", method_name[::-1])
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        return self._abort_handler


####################################### 区服远程服务 #######################################
# zone_pb2, zone_pb2_grpc = grpc.protos_and_services("zone.proto")
from internal.grpc.zone import zone_pb2
from internal.grpc.zone import zone_pb2_grpc


class ZoneService(zone_pb2_grpc.ZoneServicer):
    """实现proto文件中定义的rpc调用"""
    def zone_option(
        self, 
        request: zone_pb2.ZoneRequest, 
        context
    ) -> zone_pb2.ZoneReply:
        """区服业务逻辑"""
        if request.target == "add":
            resp = add_zone(request)
        if request.target == "uptbin":
            resp = upt_bin(request)
        if request.target == "uptcon":
            resp = upt_conf(request)
        if request.target == "start":
            resp = zone_opt(request)
        if request.target == "stop":
            resp = zone_opt("stop")
        if request.target == "check":
            resp = zone_opt("check")
        return zone_pb2.ZoneReply(name=request.name, zid=request.zid, ip=request.ip, result=resp)


####################################### 主机远程服务 #######################################
# host_pb2, host_pb2_grpc = grpc.protos_and_services("host.proto")


# class HostService(host_pb2_grpc.HostServicer):
#     async def host_option(
#         self,
#         request: host_pb2.HostRequest,
#         unused_context
#     ) -> host_pb2.HostReply:
#         """主机业务逻辑"""
#         pass


###########################################################################################
def run_server(port: str) -> Tuple[grpc.server, int]:
    """启动远程服务"""
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4),
        interceptors=(SignatureInterceptor(),)        
        )
    # 添加远程服务
    zone_pb2_grpc.add_ZoneServicer_to_server(ZoneService(), server)
    # host_pb2_grpc.add_HostServicer_to_server(HostService(), server)
    
    server_credentials = grpc.ssl_server_credentials(((
        credentials.SERVER_CERTIFICATE_KEY,
        credentials.SERVER_CERTIFICATE_CRT
    ),), credentials.ROOT_CERTIFICATE, True)
    port = server.add_secure_port(cfg.get('app', 'addr') + ":" + port, server_credentials)
    server.start()
    try:
        return server, port
    except grpc.RpcError as e:
        server.stop(0)
