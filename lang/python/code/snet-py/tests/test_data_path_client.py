import asyncio
import time
import json
from snet import SNetClient

async def test_user_operations(client):
    """测试用户相关操作"""
    print("\n" + "="*50)
    print("🧑 Testing User Operations")
    print("="*50)
    
    # 获取所有用户
    print("\n1. Getting all users...")
    response = await client.send({
        "path": "/users",
        "method": "GET"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 获取特定用户
    print("\n2. Getting user by ID...")
    response = await client.send({
        "path": "/users/1",
        "method": "GET",
        "user_id": 1
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 创建新用户
    print("\n3. Creating new user...")
    response = await client.send({
        "path": "/users",
        "method": "POST",
        "name": "David",
        "email": "david@example.com"
    })
    print(f"Response: {json.dumps(response, indent=2)}")

async def test_product_operations(client):
    """测试产品相关操作"""
    print("\n" + "="*50)
    print("📦 Testing Product Operations")
    print("="*50)
    
    # 获取所有产品
    print("\n1. Getting all products...")
    response = await client.send({
        "path": "/products", 
        "method": "GET"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 按类别筛选产品
    print("\n2. Getting products by category...")
    response = await client.send({
        "path": "/products",
        "method": "GET", 
        "category": "Electronics"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 搜索产品
    print("\n3. Searching products...")
    response = await client.send({
        "path": "/products/search",
        "method": "GET",
        "query": "book"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 获取特定产品
    print("\n4. Getting product by ID...")
    response = await client.send({
        "path": "/products/1",
        "method": "GET",
        "product_id": 1
    })
    print(f"Response: {json.dumps(response, indent=2)}")

async def test_order_operations(client):
    """测试订单相关操作"""
    print("\n" + "="*50)
    print("🛒 Testing Order Operations")
    print("="*50)
    
    # 创建订单
    print("\n1. Creating new order...")
    response = await client.send({
        "path": "/orders",
        "method": "POST",
        "user_id": 1,
        "products": [
            {"id": 1, "name": "Laptop", "price": 999.99, "quantity": 1},
            {"id": 3, "name": "Headphones", "price": 149.99, "quantity": 2}
        ]
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 获取所有订单
    print("\n2. Getting all orders...")
    response = await client.send({
        "path": "/orders",
        "method": "GET"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 获取用户订单
    print("\n3. Getting user orders...")
    response = await client.send({
        "path": "/orders",
        "method": "GET",
        "user_id": 1
    })
    print(f"Response: {json.dumps(response, indent=2)}")

async def test_auth_operations(client):
    """测试认证操作"""
    print("\n" + "="*50)
    print("🔐 Testing Auth Operations")
    print("="*50)
    
    # 登录
    print("\n1. Login...")
    response = await client.send({
        "path": "/auth/login",
        "method": "POST",
        "username": "admin",
        "password": "admin123"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 注册
    print("\n2. Register...")
    response = await client.send({
        "path": "/auth/register",
        "method": "POST",
        "username": "newuser",
        "password": "newpass123",
        "email": "newuser@example.com"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 验证token
    token = "jwt_token_123456"
    print(f"\n3. Verify token: {token}")
    response = await client.send({
        "path": "/auth/verify",
        "method": "POST",
        "token": token
    })
    print(f"Response: {json.dumps(response, indent=2)}")

async def test_analytics_operations(client):
    """测试数据分析操作"""
    print("\n" + "="*50)
    print("📊 Testing Analytics Operations")
    print("="*50)
    
    # 获取仪表板数据
    print("\n1. Getting dashboard analytics...")
    response = await client.send({
        "path": "/analytics/dashboard",
        "method": "GET"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 获取销售数据
    print("\n2. Getting sales analytics...")
    response = await client.send({
        "path": "/analytics/sales",
        "method": "GET",
        "period": "weekly"
    })
    print(f"Response: {json.dumps(response, indent=2)}")

async def test_error_cases(client):
    """测试错误情况"""
    print("\n" + "="*50)
    print("❌ Testing Error Cases")
    print("="*50)
    
    # 不存在的路径
    print("\n1. Unknown path...")
    response = await client.send({
        "path": "/unknown/path",
        "method": "GET"
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 不支持的HTTP方法
    print("\n2. Unsupported method...")
    response = await client.send({
        "path": "/users",
        "method": "DELETE"  # 服务器不支持DELETE
    })
    print(f"Response: {json.dumps(response, indent=2)}")
    
    # 缺少必需字段
    print("\n3. Missing required fields...")
    response = await client.send({
        "path": "/auth/login",
        "method": "POST"
        # 缺少username和password
    })
    print(f"Response: {json.dumps(response, indent=2)}")

async def test_concurrent_requests(client):
    """测试并发请求"""
    print("\n" + "="*50)
    print("⚡ Testing Concurrent Requests")
    print("="*50)
    
    async def make_request(i):
        request_data = {
            "path": "/products/search",
            "method": "GET",
            "query": f"product{i}"
        }
        response = await client.send(request_data)
        return f"Request {i}: {response['status']} - {response['count']} results"
    
    # 并发5个请求
    tasks = [make_request(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

async def main():
    """主测试函数"""
    print("🚀 SNet Path-Based Routing Client Demo")
    print("=" * 60)
    
    # 创建客户端
    client = SNetClient(
        host='localhost',
        port=8890,
        timeout=30.0
    )
    
    try:
        # 连接服务器
        print("Connecting to server...")
        await client.connect()
        print("✅ Connected to server successfully!")
        
        # 执行各种测试
        await test_user_operations(client)
        await test_product_operations(client) 
        await test_order_operations(client)
        await test_auth_operations(client)
        await test_analytics_operations(client)
        await test_error_cases(client)
        await test_concurrent_requests(client)
        
        print("\n" + "=" * 60)
        print("✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Client error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await client.close()
        print("🔌 Client disconnected.")

if __name__ == "__main__":
    asyncio.run(main())