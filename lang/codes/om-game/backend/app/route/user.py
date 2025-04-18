from starlette.routing import Route
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint
from internal.utils.response import Response
from internal.utils.token import TokenHandle
from internal.utils.passwd import PasswdHandle
from internal.dao.user import UserDb


class UserSignEndpoint(HTTPEndpoint):
    async def get(self, request: Request) -> Response:
        token = request.headers.get("token")
        if not token:
            return Response(40000, msg="token is null")
        token_data = TokenHandle(token=token).verify
        user_db = UserDb(name=token_data["username"]).check
        data = {
            "role": user_db.roles,
            "desc": user_db.desc,
            "name": user_db.name,
            "avatar": user_db.avatar
        }
        return Response(20000, data=data)

    async def post(self, request: Request) -> Response:
        """success"""
        # 数据库对比用户信息
        user_info = await request.json()
        user_db   = UserDb(user_info).check
        print(user_db)
        if not PasswdHandle(plain_pwd=user_info["password"], hash_pwd=user_db.password).verify:
            return Response(40000, msg="passwd error")
        # 创建token
        data = {"username": user_info["name"], "roles": user_db.roles}
        token = TokenHandle(data=data).create
        return Response(20000, data=token)


class UserEndpoint(HTTPEndpoint):
    async def get(self, request: Request) -> Response:
        """success"""
        token = request.headers.get("token")
        if not token:
            return Response(40000, msg="token is null")
        token_data = TokenHandle(token=token).verify
        user_list = UserDb().get
        if not user_list:
            return Response(40000, msg="get user list failed")
        return Response(20000, data=user_list)
        
    async def post(self, request: Request) -> Response:
        """success"""
        token = request.headers.get("token")
        if not token:
            return Response(40000, msg="token is null")
        token_data = TokenHandle(token=token).verify
        user_info = await request.json()
        if user_info["pwd_one"] != user_info["pwd_tow"]:
            return Response(40000, msg="passwd is deferent")
        if not UserDb(user=user_info).add:
            return Response(40000, msg="add user failed")
        return Response(20000, msg="add user success")

    async def delete(self, request: Request) -> Response:
        token = request.headers.get("token")
        if not token:
            return Response(40000, msg="token is null")
        user_info = await request.json()
        if not UserDb(user=user_info).delete:
            return Response(40000, msg="delete user failed")
        return Response(20000, msg="delete user success")


user_route = [
    Route("/api/user", UserEndpoint),
    Route("/api/sign", UserSignEndpoint),
]