import inspect
import logging
from typing import Any, Dict, Callable, Optional, Type, Union
from dataclasses import dataclass, is_dataclass
from enum import Enum
from .exceptions import ProtocolError

logger = logging.getLogger(__name__)

class RouteType(Enum):
    """路由类型"""
    BY_TYPE = "type"        # 按数据类型路由
    BY_ACTION = "action"    # 按action字段路由
    BY_PATH = "path"        # 按路径路由

@dataclass
class RouteConfig:
    """路由配置"""
    route_type: RouteType = RouteType.BY_TYPE
    type_field: str = "type"      # 类型字段名
    action_field: str = "action"  # action字段名
    path_field: str = "path"      # 路径字段名

class RouteHandler:
    """路由处理器基类"""
    
    async def handle(self, data: Any) -> Any:
        """
        处理请求
        
        Args:
            data: 请求数据
            
        Returns:
            响应数据
        """
        raise NotImplementedError

class TypeRouter:
    """
    类型路由管理器
    """
    
    def __init__(self, config: Optional[RouteConfig] = None):
        self.config = config or RouteConfig()
        self._handlers: Dict[Any, Callable] = {}
        self._default_handler: Optional[Callable] = None
        
    def register(self, data_type: Any, handler: Union[Callable, RouteHandler]):
        """
        注册处理器
        
        Args:
            data_type: 数据类型或标识
            handler: 处理器函数或对象
        """
        if isinstance(handler, RouteHandler):
            # 如果是RouteHandler对象，使用其handle方法
            self._handlers[data_type] = handler.handle
        else:
            self._handlers[data_type] = handler
            
        logger.debug(f"Registered handler for type: {data_type}")
        
    def register_default(self, handler: Union[Callable, RouteHandler]):
        """注册默认处理器"""
        if isinstance(handler, RouteHandler):
            self._default_handler = handler.handle
        else:
            self._default_handler = handler
        logger.debug("Registered default handler")
        
    def unregister(self, data_type: Any):
        """取消注册处理器"""
        if data_type in self._handlers:
            del self._handlers[data_type]
            logger.debug(f"Unregistered handler for type: {data_type}")
            
    async def route(self, data: Any) -> Any:
        """
        路由请求到对应的处理器
        
        Args:
            data: 请求数据
            
        Returns:
            处理结果
        """
        route_key = self._get_route_key(data)
        logger.debug(f"Routing data: {type(data).__name__}, route_key: {route_key}")
        
        if route_key in self._handlers:
            handler = self._handlers[route_key]
            logger.debug(f"Found handler for key: {route_key}")
            return await self._execute_handler(handler, data)
        elif self._default_handler:
            logger.debug(f"No specific handler for {route_key}, using default")
            return await self._execute_handler(self._default_handler, data)
        else:
            raise ProtocolError(f"No handler registered for data type: {type(data).__name__}, route_key: {route_key}")
            
    def _get_route_key(self, data: Any) -> Any:
        """获取路由键"""
        if self.config.route_type == RouteType.BY_TYPE:
            # 修复：直接使用数据类的类名
            return type(data).__name__
        elif self.config.route_type == RouteType.BY_ACTION:
            return self._get_dict_value(data, self.config.action_field)
        elif self.config.route_type == RouteType.BY_PATH:
            return self._get_dict_value(data, self.config.path_field)
        else:
            return type(data).__name__
            
    def _get_dict_value(self, data: Any, field: str) -> Any:
        """从字典或对象中获取字段值"""
        if isinstance(data, dict):
            return data.get(field)
        elif hasattr(data, field):
            return getattr(data, field)
        else:
            return None
            
    async def _execute_handler(self, handler: Callable, data: Any) -> Any:
        """执行处理器"""
        try:
            if inspect.iscoroutinefunction(handler):
                result = await handler(data)
            else:
                result = handler(data)
            logger.debug(f"Handler executed successfully, result: {type(result)}")
            return result
        except Exception as e:
            logger.error(f"Handler execution error: {e}")
            raise ProtocolError(f"Handler execution failed: {e}")
            
    def get_registered_types(self) -> list:
        """获取已注册的类型"""
        return list(self._handlers.keys())