from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app import core, schema


router = APIRouter(prefix="/api", tags=["用户接口"])


@router.post("/login", description="用户登录OK")
async def sign(
    post: OAuth2PasswordRequestForm = Depends()
) -> core.AppResponse:
    # 用户信息校验
    user = core.user_db_chk(post.username)
    if user is None:
        return core.AppResponse(40000, message="用户不存在")
    if not core.verify_pwd(post.password, user.password):
        return core.AppResponse(40000, message="密码不正确")
    # 创建token
    data = { "name": post.username }
    token = core.create_token(data)
    return core.AppResponse(20000, message="登录成功", token=token)


@router.post("/user", description="添加用户接口OK")
async def add(
    post: schema.AddUser,
    # token_data = Depends(core.get_current_user)
) -> core.AppResponse:
    if post.pass_one != post.pass_tow:
        return core.AppResponse(40000, message="密码不一致")
    user = core.user_db_chk(post.name)
    if user:
        return core.AppResponse(40000, message="用户已经存在")
    if not core.user_db_add(post):
        return core.AppResponse(40000, message="添加用户失败")
    return core.AppResponse(20000, message="添加用户成功")


@router.delete("/user", description="删除用户接口OK")
async def delete(
    post: schema.AddUser,
    token_data = Depends(core.get_current_user)
) ->core.AppResponse:
    user = core.user_db_chk(post.name)
    if user is None:
        return core.AppResponse(40000, message="用户不存在")
    if not core.user_db_del(post):
        return core.AppResponse(40000, message="删除用户失败")
    return core.AppResponse(20000, message="删除用户成功")


@router.put("/user", description="修改用户接口")
async def revise(
    post: schema.AddUser,
    token_data = Depends(core.get_current_user)
) -> core.AppResponse:

    return core.AppResponse(20000, message="修改用户成功")


@router.get("/user", description="查询用户接口")
async def query(
    token_data = Depends(core.get_current_user)
) -> core.AppResponse:
    user = core.user_db_chk(token_data["name"])
    data = {
        "name": user.name,
        "desc": user.description,
        "role": user.roles,
        "avatar": user.avatar
    }
    return core.AppResponse(20000, message="查询用户成功", data=data)


@router.get("/users", description="用户列表接口")
async def list(
    token_data = Depends(core.get_current_user)
) -> core.AppResponse:

    return core.AppResponse(20000, message="用户列表成功")


@router.post("/logout", description="用户登出接口")
async def exit(
    token_data = Depends(core.get_current_user)
) -> core.AppResponse:
    return core.AppResponse(20000, message="登出成功")