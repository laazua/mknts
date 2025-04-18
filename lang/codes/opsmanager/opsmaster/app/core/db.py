import typing
from app import schema, core
from app import AppLogger


def user_db_add(user: schema.AddUser) -> bool:
    try:
        u = schema.DBUser(
            name=user.name,
            password=core.hashed_pwd(user.pass_one),
            description=user.description,
            roles=user.roles,
            avatar=user.avatar
        )
        u.save()
        return True
    except Exception as e:
        AppLogger.error(f"{user.name} 用户入库失败: {e}")
        return False


def user_db_del(user: schema.AddUser) -> bool:
    try:
        u = schema.DBUser.objects.get(name=user.name)
        u.delete()
        u.save()
        return True
    except Exception as e:
        AppLogger.error(f"{user.name} 用户删除失败: {e}")
        return False


def user_db_chk(name: str) -> typing.Union[schema.DBUser, None]:
    try:
        return schema.DBUser.objects.get(name=name)
    except Exception as e:
        AppLogger.error(f"用户不存在: {e}")
        return None


def user_db_lst() -> typing.Union[typing.List[schema.DBUser], None]:
    try:
        return [{
            "name": u.name,
            "description": u.description,
            "roles": u.roles,
            "avatar": u.avatar,
            "create_time": u.create_time
        } for u in schema.DBUser.objects]
    except Exception as e:
        return None


def zone_db_add(zone: typing.List[schema.Zone]) -> bool:
    """区服信息入库"""
    try:
        zones = [
            schema.DBZone(
                name=z.name,
                number=z.number,
                ip=z.ip,
                create_time=z.create_time,
                is_close = z.is_close
            ) for z in zone
        ]
        _ = [z.save() for z in zones]
        AppLogger.info(f"{zone}区服信息入库成功")
        return True
    except Exception as e:
        AppLogger.error(f"{zone}区服信息入库失败: {e}")
        return False


def zone_db_lst() -> typing.Union[typing.List[schema.DBZone], None]:
    """获取库中区服信息"""
    try:
        return [
            {
                "name": z.name,
                "number": z.number,
                "ip": z.ip,
                "is_close": z.is_close
            } for z in schema.DBZone.objects
        ]
    except Exception as e:
        AppLogger.error(f"获取区服信息失败: {e}")
        return None
