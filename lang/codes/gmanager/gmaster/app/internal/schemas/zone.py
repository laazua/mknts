from pydantic import BaseModel, Field
from typing import Optional, List


class Zone(BaseModel):
    zid: str
    name: str = Field(min_length=3, max_length=24)
    public_ip: str = Field(regex="[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
    priviate_ip: str = Field(regex="[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
    domain_name: str
    target: Optional[str]
    svn_ver: Optional[int]
    create_time: Optional[str]
    is_close: Optional[bool] = False


class OptionZone(BaseModel):
    zone: List[Zone]