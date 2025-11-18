import time
from typing import Any, Optional, Dict

from .connection import Connection, ConnectionConfig
from .exceptions import ConnectionError


class SNetClient:
    """
    SNet客户端
    """
    
    def __init__(
        self,
        host: str = 'localhost',
        port: int = 8888,
        timeout: float = 30.0,
        ssl_certfile: Optional[str] = None,
        ssl_keyfile: Optional[str] = None,
        ssl_ca_certs: Optional[str] = None,
        ssl_verify: bool = True
    ):
        config = ConnectionConfig(
            host=host,
            port=port,
            timeout=timeout,
            ssl_certfile=ssl_certfile,
            ssl_keyfile=ssl_keyfile,
            ssl_ca_certs=ssl_ca_certs,
            ssl_verify=ssl_verify
        )
        self.connection = Connection(config)
        
    async def connect(self):
        """连接服务器"""
        await self.connection.connect()
        
    async def close(self):
        """关闭连接"""
        await self.connection.close()
        
    async def send(self, data: Any, timeout: Optional[float] = None) -> Any:
        """
        发送数据
        
        Args:
            data: 要发送的数据
            timeout: 超时时间
            
        Returns:
            响应数据
        """
        if not self.connection.is_connected:
            raise ConnectionError("Not connected to server")
            
        return await self.connection.send_request(data, timeout)
        
    async def send_typed_request(self, request_type: str, data: Dict, timeout: Optional[float] = None) -> Any:
        """
        发送类型化请求
        
        Args:
            request_type: 请求类型
            data: 请求数据
            timeout: 超时时间
            
        Returns:
            响应数据
        """
        request_data = {
            "type": request_type,
            "data": data,
            "timestamp": time.time()
        }
        return await self.send(request_data, timeout)
        
    @property
    def is_connected(self) -> bool:
        """连接状态"""
        return self.connection.is_connected