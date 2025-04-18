from starlette.routing import Route
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from internal.utils.response import Response
from internal.utils.token import TokenHandle
from internal.utils.ansible import ZoneHandle


class ZoneEndpoint(HTTPEndpoint):
    async def get(self, request: Request) -> Response:
        pass

    async def post(self, request: Request) -> Response:
        token = request.headers.get("token")
        if not token:
            return Response(40000, msg="token is None")
        zone_info = await request.json()
        ZoneHandle(zone=zone_info).ansible_cmd
        return Response(20000, data=zone_info)

    async def put(self, request: Request) -> Response:
        pass


zone_route = [
    Route("/api/zone", ZoneEndpoint)
]