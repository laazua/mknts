from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneReq(_message.Message):
    __slots__ = ["target", "zid", "zip", "zname", "zsvnversion"]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ZID_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    ZNAME_FIELD_NUMBER: _ClassVar[int]
    ZSVNVERSION_FIELD_NUMBER: _ClassVar[int]
    target: str
    zid: str
    zip: str
    zname: str
    zsvnversion: str
    def __init__(self, zid: _Optional[str] = ..., zname: _Optional[str] = ..., zip: _Optional[str] = ..., zsvnversion: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...

class ZoneResp(_message.Message):
    __slots__ = ["result", "zid", "zip", "zname"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ZID_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    ZNAME_FIELD_NUMBER: _ClassVar[int]
    result: str
    zid: str
    zip: str
    zname: str
    def __init__(self, zid: _Optional[str] = ..., zname: _Optional[str] = ..., zip: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...
