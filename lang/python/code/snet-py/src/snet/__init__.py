"""
SNet - 高性能TCP通信包
"""

from .server import SNetServer, MultiHandlerServer
from .client import SNetClient
from .pool import CoroutinePool
from .protocol import Message, MessageType
from .connection import ConnectionConfig
from .router import RouteHandler, TypeRouter, RouteConfig, RouteType
from .exceptions import SNetError, ConnectionError, ProtocolError, PoolError, TimeoutError

__version__ = "2.0.0"
__all__ = [
    'SNetServer',
    'SNetClient',
    'MultiHandlerServer',
    'RouteHandler',
    'TypeRouter',
    'RouteConfig', 
    'RouteType',
    'CoroutinePool',
    'Message',
    'MessageType',
    'ConnectionConfig',
    'SNetError',
    'ConnectionError',
    'ProtocolError',
    'PoolError',
    'TimeoutError'
]