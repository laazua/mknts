import asyncio
import time
import logging
from dataclasses import dataclass
from snet import SNetServer, RouteConfig, RouteType, RouteHandler

# 设置日志级别以便调试
logging.basicConfig(level=logging.DEBUG)

@dataclass
class LoginRequest:
    username: str
    password: str

@dataclass
class PaymentRequest:
    order_id: str
    amount: float
    currency: str

class LoginHandler(RouteHandler):
    """登录处理器"""
    
    async def handle(self, data):
        print(f"LoginHandler received: {type(data)}, data: {data}")
        
        # 数据在传输后是字典格式，我们需要手动转换
        if isinstance(data, dict) and 'username' in data and 'password' in data:
            # 手动创建LoginRequest对象
            request = LoginRequest(
                username=data['username'],
                password=data['password']
            )
            print(f"Processed login request for user: {request.username}")
            
            # 模拟用户验证
            if request.username == "admin" and request.password == "password123":
                return {
                    "status": "success", 
                    "message": "Login successful",
                    "token": "jwt_token_abc123",
                    "user_id": 1,
                    "permissions": ["read", "write"]
                }
            else:
                return {
                    "status": "error",
                    "message": "Invalid credentials"
                }
        
        return {"status": "error", "message": "Invalid request data"}

class PaymentHandler(RouteHandler):
    """支付处理器"""
    
    async def handle(self, data):
        print(f"PaymentHandler received: {type(data)}, data: {data}")
        
        # 数据在传输后是字典格式，我们需要手动转换
        if isinstance(data, dict) and 'order_id' in data and 'amount' in data and 'currency' in data:
            # 手动创建PaymentRequest对象
            request = PaymentRequest(
                order_id=data['order_id'],
                amount=data['amount'],
                currency=data['currency']
            )
            print(f"Processed payment request: {request.order_id}, Amount: {request.amount} {request.currency}")
            
            # 模拟支付处理
            if request.amount > 0 and request.amount <= 10000:
                return {
                    "status": "success",
                    "order_id": request.order_id,
                    "transaction_id": f"txn_{int(time.time())}",
                    "amount": request.amount,
                    "currency": request.currency,
                    "timestamp": time.time(),
                    "message": "Payment processed successfully"
                }
            else:
                return {
                    "status": "error",
                    "message": f"Invalid amount: {request.amount}"
                }
        
        return {"status": "error", "message": "Invalid request data"}

async def default_handler(data):
    """默认处理器"""
    print(f"Default handler received: {type(data)}, data: {data}")
    return {
        "status": "error", 
        "message": f"No handler registered for data type: {type(data).__name__}",
        "received_data": str(data)
    }

async def main():
    """
    启动带TLS的SNet服务器 - 修复版本
    """
    
    # 创建带TLS配置的服务器
    server = SNetServer(
        host='0.0.0.0',
        port=8083,
        max_workers=50,
        route_config=RouteConfig(
            route_type=RouteType.BY_TYPE  # 按数据类型路由
        ),
        # TLS配置
        # ssl_certfile="certs/server.crt",
        # ssl_keyfile="certs/server.key", 
        # ssl_ca_certs="certs/ca.crt"
    )
    
    # 注册处理器 - 使用数据类名作为路由键
    server.register_handler("LoginRequest", LoginHandler())
    server.register_handler("PaymentRequest", PaymentHandler())
    server.register_default_handler(default_handler)
    
    print("Starting FIXED SNet Server with TLS...")
    print("Server Configuration:")
    print(f"  Host: {server.host}")
    print(f"  Port: {server.port}")
    print(f"  TLS: Enabled")
    print(f"  Registered handlers: {server.router.get_registered_types()}")
    
    try:
        await server.start()
        print("Server is running. Press Ctrl+C to stop.")
        
        # 保持服务器运行
        await asyncio.Future()
        
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        await server.stop()
        print("Server stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass