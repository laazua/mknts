import typing
import pydantic


class Zone(pydantic.BaseModel):
    name: str
    number: str
    ip: str
    target: str
    svnversion: typing.Optional[str]
    create_time: typing.Optional[str]
    is_close: typing.Optional[bool] = False


class OptZone(pydantic.BaseModel):
    """区服操作模型"""
    zone: typing.List[Zone]


class SignUser(pydantic.BaseModel):
    """用户登录模型"""
    username: str
    password: str


class AddUser(pydantic.BaseModel):
    """增加用户模型"""
    name: str
    pass_one: str
    pass_tow: str
    description: str
    roles: typing.List[str] = None
    avatar: str = None
