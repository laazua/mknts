import os
from datetime import datetime
from typing import List
from mongoengine import connect, disconnect
from internal.models.user import User
from internal.models.zone import Zone
from internal.schemas.user import CreateUser
from internal.schemas.zone import OptionZone
from internal.core.utils import hashed_pwd
from internal.core.mlog import logger


async def init_mongo():
    """数据库初始化"""
    return connect(
        os.getenv('db_name', 'test'), 
        host=f"{os.getenv('db_host', '127.0.0.1')}",
        port=int(os.getenv('db_port', 27017)),
        # username=f"{os.getenv('db_user')}",
        # password=f"{os.getenv('db_pass')}"
        )


async def close_mongo():
    return disconnect(
        alias=f"{os.getenv('db_name', 'test')}"
    )


##################### mongodb用户操作 #####################
def user_db_add(user: CreateUser) -> bool:
    """用户信息入库"""
    try:
        _user = User(
            name = user.name,
            password = hashed_pwd(user.password),
            desc = user.desc,
            avatar = user.avatar,
            roles = user.roles,
            create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            update_time = user.update_time
        )
        _user.save()
        logger.info(f"{user.name}信息入库成功!")
        return True
    except Exception as e:
        # print("用户数据入库出错: ", e)
        logger.error(f"{user.name}信息入库出错: {e}")
        return False


def user_db_del(name: str) -> bool:
    """删除用户信息"""
    try:
        user = User.objects.get(name=name)
        user.delete()
        user.save()
        logger.info("f{name}用户信息删除成功")
        return True
    except Exception as e:
        # print("删除用户信息出错: ", e)
        logger.error(f"{name}用户信息删除出错: {e}")
        return False


def user_db_put(user: User) -> bool:
    """更改用户信息"""
    try:
        if len(user.name) != 0:
            User.objects(name=user.name).update_one(set__name=user.name)
        if len(user.password) != 0:
            User.objects(name=user.name).update_one(set__password=hashed_pwd(user.password))
        if len(user.desc) != 0:
            User.objects(name=user.name).update_one(set__desc=user.desc)
        if len(user.avatar) != 0:
            User.objects(name=user.name).update_one(set__avatar=user.avatar)
        if len(user.roles) != 0:
            User.objects(name=user.name).update_one(set__roles=user.roles)
        User.objects(name=user.name).update_one(set__update_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        logger.info(f"{user.name}用户信息修改成功")
        return True
    except Exception as e:
        # print("修改用户信息出错: ", e)
        logger.error(f"{user.name}用户信息修改出错: {e}")
        return False


def user_db_get() -> List[User]:
    """获取所有用户信息"""
    try:
        return [{
            "name": user.name, 
            "desc": user.desc, 
            "roles": user.roles, 
            "create_time": user.create_time } for user in User.objects ]
    except Exception as e:
        # print("获取用户列表出错: ", e)
        logger.error(f"获取用户列表信息出错: {e}")
        return None


def user_db_chk(name: str) -> User:
    if len(name) == 0:
        return None
    return User.objects.get(name=name)


##################### mongodb区服操作 #####################
def zone_db_add(zone: OptionZone) -> bool:
    """区服信息入库"""
    print(zone)
    try:
        _zone = [ 
            Zone(
                zid=z.zid, 
                name=z.name, 
                public_ip=z.public_ip, 
                priviate_ip=z.priviate_ip,
                create_time=z.create_time,
                is_close=z.is_close) for z in zone
        ]
        _ = [ z.save() for z in _zone]
        logger.info(f"区服信息入库成功")
        return True
    except Exception as e:
        # print("区服信息入库出错: ", e)
        logger.error(f"区服信息入库出错: {e}")
        return False


def zone_db_get() -> List[Zone]:
    """获取区服信息"""
    try:
        return [{
                "zid": z.zid, 
                "name": z.name, 
                "public_ip": z.public_ip, 
                "priviate_ip": z.priviate_ip, 
                "create_time": z.create_time,
                "is_closed": z.is_close } for z in Zone.objects 
            ]
    except Exception as e:
        print("获取区服列表出错: ", e)
        return None