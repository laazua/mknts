class SNetError(Exception):
    """SNet基础异常"""
    pass

class ConnectionError(SNetError):
    """连接异常"""
    pass

class ProtocolError(SNetError):
    """协议异常"""
    pass

class PoolError(SNetError):
    """协程池异常"""
    pass

class TimeoutError(SNetError):
    """超时异常"""
    pass