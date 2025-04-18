from enum import Enum, unique


@unique
class CountType(Enum):
    """统计类型判断"""
    TOTAL = "total"
    USER  = "user"
    OTHER = "other"