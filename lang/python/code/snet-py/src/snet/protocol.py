import asyncio
import struct
import pickle
import json
from typing import Any, Optional, Dict, Union
from dataclasses import dataclass, asdict, is_dataclass
from enum import IntEnum
import time
from .exceptions import ProtocolError

class MessageType(IntEnum):
    """消息类型枚举"""
    REQUEST = 1
    RESPONSE = 2
    HEARTBEAT = 3

@dataclass
class Message:
    """消息结构体"""
    msg_id: str
    msg_type: MessageType
    data: Any
    timestamp: float
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            'msg_id': self.msg_id,
            'msg_type': self.msg_type.value,
            'data': self._serialize_data(self.data),
            'timestamp': self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Message':
        """从字典创建消息"""
        return cls(
            msg_id=data['msg_id'],
            msg_type=MessageType(data['msg_type']),
            data=cls._deserialize_data(data['data']),
            timestamp=data['timestamp']
        )
    
    @staticmethod
    def _serialize_data(data: Any) -> Any:
        """序列化数据 - 修复数据类序列化"""
        if is_dataclass(data) and not isinstance(data, type):
            # 保存数据类类型信息
            return {
                '__dataclass__': True,
                'class_name': type(data).__name__,
                'data': asdict(data)
            }
        elif isinstance(data, (dict, list, tuple, str, int, float, bool, type(None))):
            return data
        else:
            # 其他类型使用pickle序列化
            return {'__pickle__': True, 'data': pickle.dumps(data).hex()}
    
    @staticmethod
    def _deserialize_data(data: Any) -> Any:
        """反序列化数据 - 修复数据类反序列化"""
        if isinstance(data, dict):
            if data.get('__dataclass__'):
                # 这里我们返回原始字典数据，让业务层处理具体的数据类转换
                # 在实际应用中，您可能需要一个注册表来映射类名到实际的类
                return data['data']  # 直接返回数据部分，保持字段信息
            elif data.get('__pickle__'):
                # 处理pickle数据
                return pickle.loads(bytes.fromhex(data['data']))
        return data

class Protocol:
    """
    协议处理器 - 解决TCP粘包问题
    """
    
    HEADER_FORMAT = '!I'  # 4字节无符号整数，表示数据长度
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
    
    def __init__(self, max_packet_size: int = 10 * 1024 * 1024):  # 10MB
        self.max_packet_size = max_packet_size
        
    def pack_message(self, message: Message) -> bytes:
        """
        打包消息
        
        Args:
            message: 消息对象
            
        Returns:
            打包后的字节数据
        """
        try:
            # 序列化消息
            serialized_data = pickle.dumps(message.to_dict())
            
            # 检查数据大小
            if len(serialized_data) > self.max_packet_size:
                raise ProtocolError(f"Message too large: {len(serialized_data)} bytes")
                
            # 打包头部(数据长度) + 数据
            header = struct.pack(self.HEADER_FORMAT, len(serialized_data))
            return header + serialized_data
            
        except Exception as e:
            raise ProtocolError(f"Failed to pack message: {e}")
            
    async def unpack_message(self, reader: asyncio.StreamReader) -> Optional[Message]:
        """
        从流中解包消息
        
        Args:
            reader: 流读取器
            
        Returns:
            消息对象，如果连接关闭返回None
        """
        try:
            # 读取头部
            header_data = await reader.readexactly(self.HEADER_SIZE)
            if not header_data:
                return None
                
            # 解析数据长度
            data_size = struct.unpack(self.HEADER_FORMAT, header_data)[0]
            
            # 检查数据大小
            if data_size > self.max_packet_size:
                raise ProtocolError(f"Packet too large: {data_size} bytes")
                
            # 读取数据
            data = await reader.readexactly(data_size)
            
            # 反序列化
            message_dict = pickle.loads(data)
            return Message.from_dict(message_dict)
            
        except asyncio.IncompleteReadError:
            return None
        except Exception as e:
            raise ProtocolError(f"Failed to unpack message: {e}")