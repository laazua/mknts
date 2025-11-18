import asyncio
from snet import SNetClient

async def main():
    """Action字段路由客户端"""
    client = SNetClient('localhost', 8889)
    
    await client.connect()
    
    # 发送action请求
    requests = [
        {"action": "login", "username": "admin", "password": "password123"},
        {"action": "payment", "order_id": "order_123", "amount": 50.0},
        {"action": "echo", "message": "Hello World"},
        {"action": "unknown", "data": "test"}
    ]
    
    for request in requests:
        print(f"\nSending: {request}")
        response = await client.send(request)
        print(f"Response: {response}")
    
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())