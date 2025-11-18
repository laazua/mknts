import asyncio
import ssl
import time
import uuid
from typing import Optional, Dict, Any
from dataclasses import dataclass
from .protocol import Protocol, Message, MessageType
from .exceptions import ConnectionError, ProtocolError

@dataclass
class ConnectionConfig:
    """连接配置"""
    host: str = 'localhost'
    port: int = 8888
    timeout: float = 30.0
    heartbeat_interval: float = 30.0
    ssl_certfile: Optional[str] = None
    ssl_keyfile: Optional[str] = None
    ssl_ca_certs: Optional[str] = None
    ssl_verify: bool = True

class Connection:
    """
    TCP连接管理
    """
    
    def __init__(self, config: ConnectionConfig):
        self.config = config
        self.protocol = Protocol()
        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._is_connected = False
        self._heartbeat_task: Optional[asyncio.Task] = None
        self._pending_requests: Dict[str, asyncio.Future] = {}
        
    async def connect(self):
        """建立连接"""
        try:
            if self.config.ssl_certfile:
                # TLS连接
                ssl_context = ssl.create_default_context(
                    ssl.Purpose.SERVER_AUTH,
                    cafile=self.config.ssl_ca_certs
                )
                if self.config.ssl_certfile and self.config.ssl_keyfile:
                    ssl_context.load_cert_chain(
                        self.config.ssl_certfile,
                        self.config.ssl_keyfile
                    )
                if not self.config.ssl_verify:
                    ssl_context.check_hostname = False
                    ssl_context.verify_mode = ssl.CERT_NONE
                    
                self._reader, self._writer = await asyncio.wait_for(
                    asyncio.open_ssl_stream(
                        self._reader,
                        self._writer,
                        hostname=self.config.host,
                        port=self.config.port,
                        ssl_context=ssl_context
                    ),
                    timeout=self.config.timeout
                )
            else:
                # 普通TCP连接
                self._reader, self._writer = await asyncio.wait_for(
                    asyncio.open_connection(
                        self.config.host,
                        self.config.port
                    ),
                    timeout=self.config.timeout
                )
                
            self._is_connected = True
            # 启动心跳和接收任务
            asyncio.create_task(self._receive_loop())
            if self.config.heartbeat_interval > 0:
                self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
                
        except Exception as e:
            raise ConnectionError(f"Failed to connect to {self.config.host}:{self.config.port}: {e}")
            
    async def close(self):
        """关闭连接"""
        self._is_connected = False
        
        # 取消心跳任务
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
            try:
                await self._heartbeat_task
            except asyncio.CancelledError:
                pass
                
        # 关闭writer
        if self._writer:
            self._writer.close()
            await self._writer.wait_closed()
            
        # 取消所有pending请求
        for future in self._pending_requests.values():
            if not future.done():
                future.set_exception(ConnectionError("Connection closed"))
        self._pending_requests.clear()
        
    async def send_request(self, data: Any, timeout: Optional[float] = None) -> Any:
        """
        发送请求并等待响应
        
        Args:
            data: 请求数据
            timeout: 超时时间
            
        Returns:
            响应数据
        """
        if not self._is_connected:
            raise ConnectionError("Not connected")
            
        msg_id = str(uuid.uuid4())
        message = Message(
            msg_id=msg_id,
            msg_type=MessageType.REQUEST,
            data=data,
            timestamp=time.time()
        )
        
        future = asyncio.Future()
        self._pending_requests[msg_id] = future
        
        try:
            # 发送消息
            packed_data = self.protocol.pack_message(message)
            self._writer.write(packed_data)
            await self._writer.drain()
            
            # 等待响应
            return await asyncio.wait_for(future, timeout=timeout or self.config.timeout)
            
        except Exception as e:
            if msg_id in self._pending_requests:
                del self._pending_requests[msg_id]
            raise e
            
    async def send_response(self, msg_id: str, data: Any):
        """
        发送响应
        
        Args:
            msg_id: 消息ID
            data: 响应数据
        """
        if not self._is_connected:
            raise ConnectionError("Not connected")
            
        message = Message(
            msg_id=msg_id,
            msg_type=MessageType.RESPONSE,
            data=data,
            timestamp=time.time()
        )
        
        packed_data = self.protocol.pack_message(message)
        self._writer.write(packed_data)
        await self._writer.drain()
        
    async def _receive_loop(self):
        """接收消息循环"""
        while self._is_connected:
            try:
                message = await self.protocol.unpack_message(self._reader)
                if message is None:
                    break
                    
                await self._handle_message(message)
                
            except ProtocolError as e:
                print(f"Protocol error: {e}")
                break
            except Exception as e:
                print(f"Receive error: {e}")
                break
                
        self._is_connected = False
        
    async def _handle_message(self, message: Message):
        """处理接收到的消息"""
        if message.msg_type == MessageType.RESPONSE:
            # 处理响应
            if message.msg_id in self._pending_requests:
                future = self._pending_requests.pop(message.msg_id)
                if not future.done():
                    future.set_result(message.data)
        elif message.msg_type == MessageType.HEARTBEAT:
            # 处理心跳
            await self._send_heartbeat_response(message.msg_id)
        else:
            # 交给上层处理请求
            await self.on_request_received(message.msg_id, message.data)
            
    async def on_request_received(self, msg_id: str, data: Any):
        """请求接收回调（由子类实现）"""
        pass
        
    async def _heartbeat_loop(self):
        """心跳循环"""
        while self._is_connected:
            try:
                await asyncio.sleep(self.config.heartbeat_interval)
                if self._is_connected:
                    await self._send_heartbeat()
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"Heartbeat error: {e}")
                break
                
    async def _send_heartbeat(self):
        """发送心跳"""
        message = Message(
            msg_id=str(uuid.uuid4()),
            msg_type=MessageType.HEARTBEAT,
            data=None,
            timestamp=time.time()
        )
        packed_data = self.protocol.pack_message(message)
        self._writer.write(packed_data)
        await self._writer.drain()
        
    async def _send_heartbeat_response(self, msg_id: str):
        """发送心跳响应"""
        message = Message(
            msg_id=msg_id,
            msg_type=MessageType.RESPONSE,
            data="pong",
            timestamp=time.time()
        )
        packed_data = self.protocol.pack_message(message)
        self._writer.write(packed_data)
        await self._writer.drain()
        
    @property
    def is_connected(self) -> bool:
        """连接状态"""
        return self._is_connected