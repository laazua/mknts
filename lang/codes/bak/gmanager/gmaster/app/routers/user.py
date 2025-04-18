from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from internal.db import mongo
from internal.schemas.user import CreateUser, UpdateUser
from internal.core.utils import get_current_user, verify_pwd, create_token
from internal.core.result import Response
from internal.core.mlog import logger


router = APIRouter(prefix="/api", tags=["用户API"])


@router.post("/login", description="用户登录")
async def sign(post: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"{post.username}进行了登录操作")
    user = mongo.user_db_chk(post.username)
    if not verify_pwd(post.password, user.password):
        return Response(40000, msg="密码错误")
    data = {"name": user.name, "roles": user.roles}
    token = create_token(data)
    return Response(2000, msg="登录成功", token=token)


@router.post("/user", description="添加用户")
async def add(post: CreateUser):
    if not mongo.user_db_add(post):
        return Response(40000, msg="用户入库是失败")
    logger.info(f"添加用户 {post.name} 成功")
    return Response(20000, msg="用户入库成功")


@router.delete("/user", description="删除用户")
async def remove(name: str):
    if not mongo.user_db_del(name):
        return Response(40000, msg="删除用户失败")
    logger.info(f"删除用户{name} 成功")
    return Response(20000, msg="删除用户成功")


@router.put("/user", description="修改用户")
async def fix(post: UpdateUser):
    if not mongo.user_db_chk(post.name):
        return Response(40000, "用户不存在")
    if not mongo.user_db_put(post):
        return Response(40000, msg="修改用户失败")
    logger.info(f"修改用户 {post.name} 成功")
    return Response(20000, msg="修改用户成功")


@router.get("/user", description="查询用户")
async def query(token_data: str = Depends(get_current_user)):
    user = mongo.user_db_chk(token_data["name"])
    if not user:
        return Response(40000, msg="获取用户信息失败")
    data = {"name": user.name, "roles": user.roles}
    return Response(20000, data=data)
    

@router.get("/users", description="用户列表")
async def select():
    user = mongo.user_db_get()
    if not user:
        return Response(40000, msg="获取用户列表失败")
    return Response(20000, data=user)

