import typing

from pydantic import Field
from pydantic import BaseModel


class AuthSchema(BaseModel):
    username: str = Field(max_length=54)
    password: str = Field(max_length=128)


class AuthResponse(BaseModel):
    msg: typing.Optional[str]
    data: typing.Any
