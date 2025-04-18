from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneReply(_message.Message):
    __slots__ = ["ip", "name", "result", "zid"]
    IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ZID_FIELD_NUMBER: _ClassVar[int]
    ip: str
    name: str
    result: str
    zid: str
    def __init__(self, name: _Optional[str] = ..., zid: _Optional[str] = ..., ip: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...

class ZoneRequest(_message.Message):
    __slots__ = ["ip", "name", "target", "zid"]
    IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ZID_FIELD_NUMBER: _ClassVar[int]
    ip: str
    name: str
    target: str
    zid: str
    def __init__(self, target: _Optional[str] = ..., name: _Optional[str] = ..., zid: _Optional[str] = ..., ip: _Optional[str] = ...) -> None: ...
