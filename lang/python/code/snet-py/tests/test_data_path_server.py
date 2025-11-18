import asyncio
import time
import logging
from dataclasses import dataclass
from snet import SNetServer, RouteConfig, RouteType, RouteHandler

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class Product:
    id: int
    name: str
    price: float
    category: str

@dataclass 
class Order:
    id: int
    user_id: int
    products: list
    total_amount: float

class UserHandler(RouteHandler):
    """用户相关处理器"""
    
    def __init__(self):
        self.users = {
            1: User(1, "Alice", "alice@example.com"),
            2: User(2, "Bob", "bob@example.com"),
            3: User(3, "Charlie", "charlie@example.com")
        }
    
    async def handle(self, data):
        logger.info(f"UserHandler received: {data}")
        
        path = data.get('path', '')
        method = data.get('method', 'GET')
        user_id = data.get('user_id')
        
        if path == "/users" and method == "GET":
            # 获取所有用户
            return {
                "status": "success",
                "data": [{"id": u.id, "name": u.name, "email": u.email} for u in self.users.values()],
                "count": len(self.users)
            }
        
        elif path.startswith("/users/") and method == "GET":
            # 获取特定用户
            if user_id and user_id in self.users:
                user = self.users[user_id]
                return {
                    "status": "success",
                    "data": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email
                    }
                }
            else:
                return {"status": "error", "message": "User not found"}
        
        elif path == "/users" and method == "POST":
            # 创建用户
            name = data.get('name')
            email = data.get('email')
            if name and email:
                new_id = max(self.users.keys()) + 1
                new_user = User(new_id, name, email)
                self.users[new_id] = new_user
                return {
                    "status": "success",
                    "message": "User created",
                    "data": {"id": new_id, "name": name, "email": email}
                }
            else:
                return {"status": "error", "message": "Missing name or email"}
        
        else:
            return {"status": "error", "message": f"Unsupported user operation: {method} {path}"}

class ProductHandler(RouteHandler):
    """产品相关处理器"""
    
    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 999.99, "Electronics"),
            2: Product(2, "Book", 29.99, "Education"),
            3: Product(3, "Headphones", 149.99, "Electronics"),
            4: Product(4, "Desk", 199.99, "Furniture")
        }
    
    async def handle(self, data):
        logger.info(f"ProductHandler received: {data}")
        
        path = data.get('path', '')
        method = data.get('method', 'GET')
        product_id = data.get('product_id')
        category = data.get('category')
        
        if path == "/products" and method == "GET":
            # 获取所有产品或按类别筛选
            if category:
                filtered_products = [p for p in self.products.values() if p.category == category]
                return {
                    "status": "success",
                    "data": [{"id": p.id, "name": p.name, "price": p.price, "category": p.category} 
                            for p in filtered_products],
                    "count": len(filtered_products),
                    "category": category
                }
            else:
                return {
                    "status": "success",
                    "data": [{"id": p.id, "name": p.name, "price": p.price, "category": p.category} 
                            for p in self.products.values()],
                    "count": len(self.products)
                }
        
        elif path.startswith("/products/") and method == "GET":
            # 获取特定产品
            if product_id and product_id in self.products:
                product = self.products[product_id]
                return {
                    "status": "success",
                    "data": {
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                        "category": product.category
                    }
                }
            else:
                return {"status": "error", "message": "Product not found"}
        
        elif path == "/products/search" and method == "GET":
            # 搜索产品
            query = data.get('query', '').lower()
            if query:
                results = [
                    p for p in self.products.values() 
                    if query in p.name.lower() or query in p.category.lower()
                ]
                return {
                    "status": "success",
                    "data": [{"id": p.id, "name": p.name, "price": p.price, "category": p.category} 
                            for p in results],
                    "count": len(results),
                    "query": query
                }
            else:
                return {"status": "error", "message": "Missing search query"}
        
        else:
            return {"status": "error", "message": f"Unsupported product operation: {method} {path}"}

class OrderHandler(RouteHandler):
    """订单相关处理器"""
    
    def __init__(self):
        self.orders = {}
        self.next_order_id = 1
    
    async def handle(self, data):
        logger.info(f"OrderHandler received: {data}")
        
        path = data.get('path', '')
        method = data.get('method', 'GET')
        order_id = data.get('order_id')
        user_id = data.get('user_id')
        
        if path == "/orders" and method == "GET":
            # 获取所有订单或用户订单
            if user_id:
                user_orders = [o for o in self.orders.values() if o.user_id == user_id]
                return {
                    "status": "success",
                    "data": [
                        {
                            "id": o.id,
                            "user_id": o.user_id,
                            "products": o.products,
                            "total_amount": o.total_amount,
                            "created_at": getattr(o, 'created_at', time.time())
                        } for o in user_orders
                    ],
                    "count": len(user_orders)
                }
            else:
                return {
                    "status": "success",
                    "data": [
                        {
                            "id": o.id,
                            "user_id": o.user_id, 
                            "products": o.products,
                            "total_amount": o.total_amount,
                            "created_at": getattr(o, 'created_at', time.time())
                        } for o in self.orders.values()
                    ],
                    "count": len(self.orders)
                }
        
        elif path == "/orders" and method == "POST":
            # 创建订单
            user_id = data.get('user_id')
            products = data.get('products', [])
            
            if user_id and products:
                total_amount = sum(p.get('price', 0) * p.get('quantity', 1) for p in products)
                order = Order(
                    id=self.next_order_id,
                    user_id=user_id,
                    products=products,
                    total_amount=total_amount
                )
                order.created_at = time.time()
                self.orders[self.next_order_id] = order
                self.next_order_id += 1
                
                return {
                    "status": "success",
                    "message": "Order created",
                    "data": {
                        "id": order.id,
                        "user_id": order.user_id,
                        "products": order.products,
                        "total_amount": order.total_amount,
                        "created_at": order.created_at
                    }
                }
            else:
                return {"status": "error", "message": "Missing user_id or products"}
        
        elif path.startswith("/orders/") and method == "GET":
            # 获取特定订单
            if order_id and order_id in self.orders:
                order = self.orders[order_id]
                return {
                    "status": "success",
                    "data": {
                        "id": order.id,
                        "user_id": order.user_id,
                        "products": order.products,
                        "total_amount": order.total_amount,
                        "created_at": getattr(order, 'created_at', time.time())
                    }
                }
            else:
                return {"status": "error", "message": "Order not found"}
        
        else:
            return {"status": "error", "message": f"Unsupported order operation: {method} {path}"}

class AuthHandler(RouteHandler):
    """认证处理器"""
    
    async def handle(self, data):
        logger.info(f"AuthHandler received: {data}")
        
        path = data.get('path', '')
        method = data.get('method', 'POST')
        username = data.get('username')
        password = data.get('password')
        
        if path == "/auth/login" and method == "POST":
            # 模拟登录
            if username == "admin" and password == "admin123":
                return {
                    "status": "success",
                    "message": "Login successful",
                    "token": f"jwt_token_{int(time.time())}",
                    "user": {"id": 1, "username": "admin", "role": "administrator"},
                    "expires_in": 3600
                }
            else:
                return {"status": "error", "message": "Invalid credentials"}
        
        elif path == "/auth/register" and method == "POST":
            # 模拟注册
            email = data.get('email')
            if username and password and email:
                return {
                    "status": "success",
                    "message": "User registered successfully",
                    "user": {"id": 100, "username": username, "email": email},
                    "token": f"jwt_token_{int(time.time())}"
                }
            else:
                return {"status": "error", "message": "Missing required fields"}
        
        elif path == "/auth/verify" and method == "POST":
            # 验证token
            token = data.get('token')
            if token and token.startswith("jwt_token_"):
                return {
                    "status": "success",
                    "message": "Token is valid",
                    "user": {"id": 1, "username": "admin", "role": "administrator"}
                }
            else:
                return {"status": "error", "message": "Invalid token"}
        
        else:
            return {"status": "error", "message": f"Unsupported auth operation: {method} {path}"}

async def analytics_handler(data):
    """数据分析处理器 - 使用函数形式"""
    logger.info(f"AnalyticsHandler received: {data}")
    
    path = data.get('path', '')
    method = data.get('method', 'GET')
    
    if path == "/analytics/dashboard" and method == "GET":
        # 模拟仪表板数据
        return {
            "status": "success",
            "data": {
                "total_users": 1500,
                "total_orders": 890,
                "revenue": 125000.50,
                "active_users": 234,
                "popular_products": [
                    {"name": "Laptop", "sales": 45},
                    {"name": "Headphones", "sales": 32},
                    {"name": "Book", "sales": 28}
                ]
            }
        }
    
    elif path == "/analytics/sales" and method == "GET":
        # 销售分析
        period = data.get('period', 'weekly')
        return {
            "status": "success",
            "data": {
                "period": period,
                "sales_data": [
                    {"date": "2024-01-01", "amount": 1200},
                    {"date": "2024-01-02", "amount": 1800},
                    {"date": "2024-01-03", "amount": 1500},
                    {"date": "2024-01-04", "amount": 2200},
                    {"date": "2024-01-05", "amount": 1900}
                ],
                "total_sales": 8600,
                "average_daily": 1720
            }
        }
    
    else:
        return {"status": "error", "message": f"Unsupported analytics operation: {method} {path}"}

async def default_handler(data):
    """默认处理器"""
    logger.warning(f"Default handler received unknown request: {data}")
    return {
        "status": "error",
        "message": f"Route not found: {data.get('path', 'unknown')}",
        "supported_paths": [
            "/users", "/products", "/orders", "/auth/login", 
            "/auth/register", "/analytics/dashboard", "/analytics/sales"
        ]
    }

async def main():
    """
    Path字段路由服务器示例
    模拟RESTful API风格的路由
    """
    
    server = SNetServer(
        host='0.0.0.0',
        port=8890,  # 使用8890端口
        max_workers=50,
        route_config=RouteConfig(
            route_type=RouteType.BY_PATH,  # 使用Path字段路由
            path_field="path"  # 指定path字段名
        )
    )
    
    # 注册路径处理器
    server.register_handler("/users", UserHandler())
    server.register_handler("/products", ProductHandler()) 
    server.register_handler("/orders", OrderHandler())
    server.register_handler("/auth", AuthHandler())
    server.register_handler("/analytics", analytics_handler)  # 使用函数处理器
    
    # 注册默认处理器
    server.register_default_handler(default_handler)
    
    print("🚀 Starting Path-based Routing Server...")
    print("=" * 60)
    print("Server Configuration:")
    print(f"  Host: {server.host}")
    print(f"  Port: {server.port}")
    print(f"  Routing: Path-based")
    print(f"  Path Field: 'path'")
    print(f"  Registered Paths: {server.router.get_registered_types()}")
    print("=" * 60)
    print("Available API Endpoints:")
    print("  Users: /users [GET, POST], /users/{id} [GET]")
    print("  Products: /products [GET], /products/{id} [GET], /products/search [GET]")
    print("  Orders: /orders [GET, POST], /orders/{id} [GET]")
    print("  Auth: /auth/login [POST], /auth/register [POST], /auth/verify [POST]")
    print("  Analytics: /analytics/dashboard [GET], /analytics/sales [GET]")
    print("=" * 60)
    
    try:
        await server.start()
        print("✅ Server is running. Press Ctrl+C to stop.")
        
        # 保持服务器运行
        await asyncio.Future()
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server...")
    except Exception as e:
        print(f"❌ Server error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await server.stop()
        print("✅ Server stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass