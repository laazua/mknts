from pydantic import BaseModel, Field
from typing import Optional, List


class UserSign(BaseModel):
    name: str = Field(min_length=3, max_length=24)
    password: str = Field(min_length=6, max_length=255)


class CreateUser(BaseModel):
    name: str = Field(min_length=3, max_length=24)
    password: str = Field(min_length=6, max_length=255)
    desc: Optional[str]
    avatar: Optional[str]
    roles: Optional[List[str]]
    create_time: Optional[str] = None
    update_time: Optional[str] = None


class UpdateUser(BaseModel):
    name: str = Field(min_length=3, max_length=24)
    password: str = Field(min_length=6, max_length=255)
    desc: Optional[str]
    avatar: Optional[str]
    roles: Optional[List[str]]
    create_time: Optional[str]
    update_time: Optional[str]


class UserInfo(BaseModel):
    name: str
    desc: str
    roles: List[str]
    create_time: str
    update_time: str