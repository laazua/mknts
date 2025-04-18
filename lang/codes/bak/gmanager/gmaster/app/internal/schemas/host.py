from pydantic import BaseModel, Field
from typing import Optional, List


class CreateHost(BaseModel):
    ip: str = Field(regex="[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}")
    system: Optional[str]
    cpu: Optional[str]
    mem: Optional[str]
    disk: Optional[str]