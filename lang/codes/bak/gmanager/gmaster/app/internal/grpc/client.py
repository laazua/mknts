import os
import grpc
import contextlib
from internal.grpc import credentials
from internal.schemas import zone
from internal.core.mlog import logger


class AuthGateway(grpc.AuthMetadataPlugin):
    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback
    ) -> None:
        signature = context.method_name[::-1]
        callback((("x-signature", signature), ), None)


@contextlib.contextmanager
def create_client_channel(addr: str) -> grpc.Channel:
    call_credential = grpc.metadata_call_credentials(AuthGateway(), name="auth gateway")
    channel_credential = grpc.ssl_channel_credentials(
        root_certificates=credentials.ROOT_CERTIFICATE,
        private_key=credentials.CLIENT_CERTIFICATE_KEY, 
        certificate_chain=credentials.CLIENT_CERTIFICATE_CRT)
    composite_credential = grpc.composite_channel_credentials(channel_credential, call_credential)

    yield grpc.secure_channel(addr, composite_credential)


####################################### 区服远程调用 #######################################
# zone_pb2, zone_pb2_grpc = grpc.protos_and_services("zone.proto")
from internal.grpc.zone import zone_pb2
from internal.grpc.zone import zone_pb2_grpc


def _zone_service(channel: grpc.Channel, zone) -> zone_pb2.ZoneReply:
    """业务逻辑"""
    stub = zone_pb2_grpc.ZoneStub(channel)
    request = zone_pb2.ZoneRequest(target=zone["target"], name=zone["name"], zid=zone["zid"], ip=zone["domain"])
    try:
        return stub.zone_option(request)
    except grpc.RpcError as e:
        logger.exception("区服远程调用出错: ", e)
        return None


def call_zone_service(zone) -> zone_pb2.ZoneReply:
    addr = f"{zone['domain']}:{os.getenv('grpc_port', 8887)}"
    with create_client_channel(addr) as channel:
        response = _zone_service(channel, zone)
    return {'name': response.name, 'zid': response.zid, 'ip': response.ip, 'result': response.result}


####################################### 主机远程调用 #######################################
# host_pb2, host_pb2_grpc = grpc.protos_and_services("host.proto")


# async def _host_service(channel: grpc.aio.Channel, host) -> host_pb2.HostReply:
#     stub = host_pb2_grpc.HostStub(channel)
#     request = host_pb2.HostRequest(ip=host.ip)
#     try:
#         return await stub.host_option(request)
#     except grpc.RpcError as e:
#         print("主机远程调用出错: ", e)
#         logger.exception("主机远程调用出错: ", e)
#         return None


# async def call_host_service(host) -> host_pb2.HostReply:
#     channel = _create_client_channel(host.ip + ":" + str(os.getenv("grpc_port")))
#     response = await _host_service(host)
#     await channel.close()
    
#     return response