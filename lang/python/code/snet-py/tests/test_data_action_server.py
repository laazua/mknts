import asyncio
import time
from snet import SNetServer, RouteConfig, RouteType

async def login_handler(data):
    """登录处理器"""
    print(f"Login handler received: {data}")
    
    username = data.get('username', '')
    password = data.get('password', '')
    
    if username == "admin" and password == "password123":
        return {
            "status": "success", 
            "message": "Login successful",
            "token": "jwt_token_abc123"
        }
    else:
        return {"status": "error", "message": "Invalid credentials"}

async def payment_handler(data):
    """支付处理器"""
    print(f"Payment handler received: {data}")
    
    order_id = data.get('order_id', '')
    amount = data.get('amount', 0)
    
    if amount > 0:
        return {
            "status": "success",
            "order_id": order_id,
            "transaction_id": f"txn_{int(time.time())}",
            "amount": amount
        }
    else:
        return {"status": "error", "message": "Invalid amount"}

async def echo_handler(data):
    """回显处理器"""
    return {"echo": data, "timestamp": time.time()}

async def default_handler(data):
    """默认处理器"""
    return {"status": "error", "message": f"Unknown action: {data.get('action', 'unknown')}"}

async def main():
    """
    使用Action字段路由的服务器
    """
    
    server = SNetServer(
        host='0.0.0.0',
        port=8889,  # 使用不同端口
        route_config=RouteConfig(
            route_type=RouteType.BY_ACTION,  # 按action字段路由
            action_field="action"  # 指定action字段名
        )
    )
    
    # 注册处理器 - 使用action值作为路由键
    server.register_handler("login", login_handler)
    server.register_handler("payment", payment_handler)
    server.register_handler("echo", echo_handler)
    server.register_default_handler(default_handler)
    
    print("Starting Action-based Server...")
    print(f"Registered actions: {server.router.get_registered_types()}")
    
    try:
        await server.start()
        await asyncio.Future()
    except KeyboardInterrupt:
        await server.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass