from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneRequest(_message.Message):
    __slots__ = ["ip", "name", "number", "svnversion", "target"]
    IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SVNVERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ip: str
    name: str
    number: str
    svnversion: str
    target: str
    def __init__(self, name: _Optional[str] = ..., number: _Optional[str] = ..., ip: _Optional[str] = ..., target: _Optional[str] = ..., svnversion: _Optional[str] = ...) -> None: ...

class ZoneResponse(_message.Message):
    __slots__ = ["ip", "name", "number", "result", "target"]
    IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ip: str
    name: str
    number: str
    result: str
    target: str
    def __init__(self, name: _Optional[str] = ..., number: _Optional[str] = ..., ip: _Optional[str] = ..., target: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...
