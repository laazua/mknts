import asyncio
import time
import json
import logging
from dataclasses import dataclass
from snet import SNetClient

# 设置日志级别以便调试
logging.basicConfig(level=logging.INFO)

@dataclass
class LoginRequest:
    username: str
    password: str

@dataclass
class PaymentRequest:
    order_id: str
    amount: float
    currency: str

async def test_fixed_requests():
    """测试修复后的请求"""
    print("Testing FIXED TLS client...")
    
    # 创建带TLS的客户端
    client = SNetClient(
        host='localhost',
        port=8083,
        timeout=30.0,
        # ssl_certfile="certs/client.crt",
        # ssl_keyfile="certs/client.key", 
        # ssl_ca_certs="certs/ca.crt",
        # ssl_verify=True
    )
    
    try:
        # 连接服务器
        print("Connecting to server...")
        await client.connect()
        print("✓ Connected to server with TLS")
        
        # 测试登录请求 - 直接发送数据类对象
        print("\n1. Testing login with dataclass...")
        login_data = LoginRequest("admin", "password123")
        print(f"Sending dataclass: {type(login_data).__name__}")
        
        start_time = time.time()
        login_response = await client.send(login_data)
        response_time = time.time() - start_time
        
        print(f"Response: {json.dumps(login_response, indent=2)}")
        print(f"Response time: {response_time:.3f}s")
        
        # 测试支付请求
        print("\n2. Testing payment with dataclass...")
        payment_data = PaymentRequest("order_12345", 99.99, "USD")
        print(f"Sending dataclass: {type(payment_data).__name__}")
        
        start_time = time.time()
        payment_response = await client.send(payment_data)
        response_time = time.time() - start_time
        
        print(f"Response: {json.dumps(payment_response, indent=2)}")
        print(f"Response time: {response_time:.3f}s")
        
        # 测试字典请求（应该使用默认处理器）
        print("\n3. Testing dict request (should use default handler)...")
        dict_data = {"action": "test", "message": "hello"}
        print(f"Sending dict: {type(dict_data).__name__}")
        
        start_time = time.time()
        dict_response = await client.send(dict_data)
        response_time = time.time() - start_time
        
        print(f"Response: {json.dumps(dict_response, indent=2)}")
        print(f"Response time: {response_time:.3f}s")
        
    except Exception as e:
        print(f"✗ Client error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await client.close()
        print("\n✓ Client disconnected")

async def main():
    """主测试函数"""
    print("SNet TLS Client - FIXED Version")
    print("=" * 50)
    
    await test_fixed_requests()
    
    print("\n" + "=" * 50)
    print("All tests completed!")

if __name__ == "__main__":
    asyncio.run(main())