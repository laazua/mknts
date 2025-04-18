import typing
import pydantic


class Zone(pydantic.BaseModel):
    zid: str
    zname: str
    zip: str
    target: typing.Optional[str]
    zsvnversion: typing.Optional[str]


class OptZone(pydantic.BaseModel):
    zone: typing.List[Zone]
