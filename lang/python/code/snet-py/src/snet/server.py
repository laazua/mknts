import asyncio
import ssl
from typing import Callable, Optional, Any, Dict
from .pool import CoroutinePool
from .connection import Connection, ConnectionConfig
from .protocol import Message
from .router import TypeRouter, RouteHandler, RouteConfig, RouteType
from .exceptions import ConnectionError

class MultiHandlerServer:
    """多处理器服务器接口"""
    
    def __init__(self):
        self.router = TypeRouter()
        
    def register_handler(self, data_type: Any, handler: Callable):
        """
        注册处理器
        
        Args:
            data_type: 数据类型标识
            handler: 处理器函数
        """
        self.router.register(data_type, handler)
        
    def register_default_handler(self, handler: Callable):
        """注册默认处理器"""
        self.router.register_default(handler)

class SNetServer(MultiHandlerServer):
    """
    SNet服务器 - 支持多处理器注册
    """
    
    def __init__(
        self,
        host: str = 'localhost',
        port: int = 8888,
        max_workers: int = 100,
        route_config: Optional[RouteConfig] = None,
        ssl_certfile: Optional[str] = None,
        ssl_keyfile: Optional[str] = None,
        ssl_ca_certs: Optional[str] = None
    ):
        super().__init__()
        self.host = host
        self.port = port
        
        # 使用自定义路由配置
        if route_config:
            self.router = TypeRouter(route_config)
        else:
            self.router = TypeRouter()
        
        # 初始化协程池
        self.pool = CoroutinePool(max_workers=max_workers)
        
        # SSL配置
        self.ssl_context = None
        if ssl_certfile and ssl_keyfile:
            self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            self.ssl_context.load_cert_chain(ssl_certfile, ssl_keyfile)
            if ssl_ca_certs:
                self.ssl_context.load_verify_locations(ssl_ca_certs)
                self.ssl_context.verify_mode = ssl.CERT_REQUIRED
        
        self._server: Optional[asyncio.Server] = None
        self._connections = set()
        
    async def start(self):
        """启动服务器"""
        # 启动协程池
        await self.pool.start()
        
        # 启动TCP服务器
        self._server = await asyncio.start_server(
            self._handle_client,
            self.host,
            self.port,
            ssl=self.ssl_context
        )
        
        print(f"SNet server started on {self.host}:{self.port}")
        print(f"Registered handlers for: {self.router.get_registered_types()}")
        
    async def stop(self):
        """停止服务器"""
        # 关闭所有连接
        for connection in self._connections.copy():
            await connection.close()
            
        # 停止服务器
        if self._server:
            self._server.close()
            await self._server.wait_closed()
            
        # 停止协程池
        await self.pool.stop()
        
        print("SNet server stopped")
        
    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """处理客户端连接"""
        # 创建客户端连接
        config = ConnectionConfig(
            host=self.host,
            port=self.port
        )
        connection = ClientConnection(reader, writer, config, self.pool, self.router)
        self._connections.add(connection)
        
        try:
            await connection.start()
        finally:
            self._connections.remove(connection)

class ClientConnection(Connection):
    """客户端连接"""
    
    def __init__(self, reader, writer, config, pool, router):
        super().__init__(config)
        self._reader = reader
        self._writer = writer
        self.pool = pool
        self.router = router
        self._is_connected = True
        
    async def start(self):
        """启动连接处理"""
        await self._receive_loop()
        
    async def on_request_received(self, msg_id: str, data: Any):
        """处理请求 - 使用路由处理器"""
        try:
            # 使用协程池和路由处理器处理请求
            response = await self.pool.submit(
                self.router.route,
                data
            )
            await self.send_response(msg_id, response)
        except Exception as e:
            # 发送错误响应
            error_response = {"error": str(e), "success": False}
            await self.send_response(msg_id, error_response)