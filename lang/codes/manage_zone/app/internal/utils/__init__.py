# @Time:        2022-08-04
# @Author:      Sseve
# @File:        __init__.py
# @Description: some utils

from config import settings
from fabric import Connection
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/api/login")


class TokeHandle:
    def __init__(self, 
            crt_key:     str  = "webapp123", 
            algorithm:   str  = None, 
            expire_time: int  = 60, 
            data:        dict = None, 
            token:       str  = None
            ) -> None:
        self._crt_key     = crt_key
        self._algorithm   = algorithm
        self._expire_time = expire_time
        self._data        = data
        self._token       = token
   
    @property
    def create_token(self) -> str:
        expires_delta = timedelta(minutes=self._expire_time)
        if expires_delta:
            expire_time = datetime.utcnow() + expires_delta
        else:
            expire_time = datetime.utcnow() + timedelta(minutes=60)
        data = self._data.copy()
        data.update({"exp": expire_time})
        return jwt.encode(data, self._crt_key, algorithm=self._algorithm)

    @property
    def verify_token(self) -> dict:
        credentials_expception = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail      = "Could not validate credentials",
            headers     ={"WWW-Authenticate": "Bearer"},
            )
        try:
            payload = jwt.decode(self._token, self._crt_key, algorithms=[self._algorithm])
            username = payload.get("name")
            if username is None:
                raise credentials_expception
            token_data = {"username": username}
        except JWTError:
            raise credentials_expception
        return token_data


class PasswdHandle:
    def __init__(self, plain_pwd=None, hash_pwd=None) -> None:
        self._plain_pwd = plain_pwd
        self._hash_pwd  = hash_pwd
        self._pwd_ctx   = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @property
    def hashed_passwd(self) -> str:
        return self._pwd_ctx.hash(self._plain_pwd)

    @property
    def verify_passwd(self) -> bool:
        return self._pwd_ctx.verify(self._plain_pwd, self._hash_pwd)


class FabricHandle:
    def __init__(self, ip: str = None, zone: dict = None) -> None:
        self._ip    = ip
        self._zone = zone

    @property
    async def update_config(self) -> dict:
        cmd = f"""
          if [ ! -d {settings.svn_data} ];then
            mkdir -p {settings.svn_data}
            version=$(svn --username {settings.svn_user} --password {settings.svn_password} checkout {settings.svn_address} {settings.svn_data} |grep -w revision)
            echo "update config success $version"
          else
            version=$(svn update --username {settings.svn_user} --password {settings.svn_password} {settings.svn_data} |grep -w revision)
            echo "update config success $version"
          fi
        """
        if ret := Connection(self._ip).run(cmd) and not ret.exited:
            return {"msg": ret.stderr}
        return {"msg": ret.stdout}

    @property
    async def update_binfile(self) -> dict:
        Connection(self._ip).put(settings.local_bin, settings.remot_bin)
        return {"msg": "put binfile success"}

    @property
    async def add_zone(self) -> dict:
        game_path = settings.gm_path + f"{self._zone['name']}_{self._zone['zone_id']}"
        cmd = f"""
          mkdir -p {game_path}
          if [ ! -d {settings.svn_data} ];then
            mkdir -p {settings.svn_data}
            svn --username {settings.svn_user} --password {settings.svn_password} checkout {settings.svn_address} {settings.svn_data} |grep -w revision
          else
            svn update --username {settings.svn_user} --password {settings.svn_password} {settings.svn_data} |grep -w revision
          fi
          cp -rf {settings.svn_data}* {game_path}
        """
        
        if ret := Connection(self._zone['ip']).run(cmd) and not ret.exited:
            print("fabric_add_zone: ", ret.stderr)
            self._zone["msg"] = ret.stderr
        else:
            print("fabric_add_zone: ", ret.stdout)
            self._zone["msg"] = ret.stdout
        return self._zone

    @property
    async def operate_zone(self):
        game_path = settings.gm_path + f"{self._zone['name']}_{self._zone['zone_id']}"
        cmd = f"""
            cd {game_path}
            sh {settings.gm_shell} {self._zone["opt"]}
        """
        if ret := Connection(self._zone['ip']).run(cmd) and not ret.exited:
            self._zone["msg"] = f"zone operate zone failed: {ret.stderr}"
        else:
            self._zone["msg"] = f"zone operate zone success: {ret.stdout}"
        return self._zone

    @property
    async def update_zone_binfile(self) -> dict:
        cmd = f"""
          cp -rf {settings.remot_bin} {settings.gm_path}{self._zone['name']}_{self._zone['zone_id']} && \
            md5sum {settings.gm_path}{self._zone['name']}_{self._zone['zone_id']}/gameserv
        """
        if ret := Connection(self._zone["ip"]).run(cmd) and not ret.exited:
            self._zone["msg"] = f"update binfile to zone failed: {ret.stderr}"
        else:
            self._zone["msg"] = f"update binfile to zone success: {ret.stdout}"
        return self._zone
    
    @property
    async def update_zone_config(self) -> dict:
        cmd = f"""
          cp -rf {settings.svn_data}/* {settings.gm_path}{self._zone['name']}_{self._zone['zone_id']}
        """
        if ret := Connection(self._zone['ip']).run(cmd) and not ret.exited:
            self._zone['msg'] = f"update config to zone failed: {ret.stderr}"
        else:
            self._zone['msg'] = f"update config to zone success: {ret.stdout}"
        return self._zone

    @property
    async def get_host_info(self) -> dict:
        cmd = """
            #!/bin/bash
            # cpu
            echo "{'cpu': 10}"
            # disk
            echo "{'disk': 50}"
            # mem
            echo "{'mem': 20}"
            # load
            echo "{'load': 30}"
        """
        ret = Connection(self._ip).run(cmd)
        if not ret.exited:
            # print(ret.stdout)
            pass
        else:
            # print("eeeeeeeeeee")
            pass


class LogHandle:
    def __init__(self) -> None:
        pass


async def get_current_user(token: str = Depends(oauth2_scheme)):
    return TokeHandle(
               crt_key   = settings.app_key, 
               algorithm = settings.app_algorithm, 
               token     = token
               ).verify_token