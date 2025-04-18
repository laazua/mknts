# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.libs import utils, database, schemas, resource


router = APIRouter(prefix="/user/api", tags=["User Api"])


@router.post("/login", response_model=schemas.LoginResponse, name="user:login")
async def login(user_login: OAuth2PasswordRequestForm = Depends()):
    # 查询数据库是否存在用户
    user = await database.get_user_by_name(username=user_login.username)
    if not user:
        raise resource.LOGIN_USER_ERROR
    # 验证密码是否正确
    if not utils.verify_password(user_login.password, user.password):
        raise resource.LOGIN_PASS_ERROR
    # 颁发token
    token = utils.create_token({"username": user_login.username})
    # 响应登录成功
    return schemas.LoginResponse(
        token=token,
        message="登录成功!",
        code=200
    )


@router.post("/register", response_model=schemas.RegesteResponse, name="user:register")
async def register(user_register: schemas.RegistrationForm, current_user: schemas.CurrentUser = Depends(utils.get_current_user)):
    
    if user_register.password != user_register.password2:
        raise resource.REGESTER_PASS_ERROR
    # 查询数据库是否存在该用户
    user = await database.get_user_by_name(username=user_register.username)
    if user:
        raise resource.REGESTER_USER_ERROR
    try:
        # 将用户信息插入数据库
        await database.insert_user_to_db(user_register.username, user_register.password)
    except:
        raise resource.REGESTER_USER_FAILD
    # 接口操作记录
    await database.insert_record_to_db(current_user["username"], f"添加用户:{user_register.username}")
    # 响应注册成功
    return schemas.RegesteResponse(
        username=user_register.username,
        message="注册成功",
        code=200
    )
    

@router.get("/userlists", response_model=schemas.ListDictResponse, name="user:list")
async def get_user_list(_: schemas.CurrentUser = Depends(utils.get_current_user)):
    data = await database.select_all_users()
    return schemas.ListDictResponse(
        message="获取用户列表成功!",
        code=200,
        data=data
    )


@router.post("/deluser", response_model=schemas.DeleteUserResponse, name="user:delete")
async def del_user(req: schemas.DeleteUserForm, current_user: schemas.CurrentUser = Depends(utils.get_current_user)):
    if req.username:
        try:
            await database.delete_user(req.username)
        except:
             raise resource.DELETE_USER_ERROR
    # 接口操作记录
    await database.insert_record_to_db(current_user["username"], f"删除用户:{req.username}")
    return schemas.DeleteUserResponse(
        message=f"{req.username}删除成功!",
        code=200
    )


@router.post("/userlog", response_model=schemas.ListDictResponse, name="user:getuserlog")
async def get_user_log(req: schemas.UserLogForm, current_user: schemas.CurrentUser = Depends(utils.get_current_user)):
    datetime = utils.format_time(req.datetime)
    record = await database.select_user_record(req.username, datetime)
    data = [{"username":item[0], "record": item[1], "time": item[2]} for item in record]
    return schemas.ListDictResponse(
        message="获取用户日志成功",
        code=200,
        data=data
    )


@router.get("/userinfo")
async def get_user_info(_: schemas.CurrentUser = Depends(utils.get_current_user)):
    return {
        "message": "success",
        "code": 200
    }
