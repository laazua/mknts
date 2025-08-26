### 懒加载

- **装饰器**
```python
class LazyObject:
    def __init__(self):
        self._expensive_object = None
    
    @property
    def expensive_object(self):
        if self._expensive_object is None:
            print("Creating expensive object...")
            self._expensive_object = self._create_expensive_object()
        return self._expensive_object
    
    def _create_expensive_object(self):
        # 模拟昂贵的初始化操作
        return {"name": "Lazy Instance", "data": list(range(1000))}

# 使用
obj = LazyObject()
print("Object created, but expensive object not yet initialized")

# 第一次访问时初始化
print(obj.expensive_object["name"])  # 输出: Creating expensive object... 然后 Lazy Instance

# 后续访问使用已初始化的对象
print(obj.expensive_object["data"][:5])  # 直接返回，不再初始化
```

- **描述符**
```python
class lazy_property:
    def __init__(self, func):
        self.func = func
        self.attr_name = f"_{func.__name__}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        if not hasattr(instance, self.attr_name):
            value = self.func(instance)
            setattr(instance, self.attr_name, value)
        return getattr(instance, self.attr_name)

class ExpensiveClass:
    @lazy_property
    def expensive_data(self):
        print("Initializing expensive data...")
        # 模拟昂贵的计算或IO操作
        return {"computed": sum(i**2 for i in range(10000))}
    
    @lazy_property
    def another_expensive_thing(self):
        print("Initializing another expensive thing...")
        return list(range(1000))

# 使用
obj = ExpensiveClass()
print("Object created")

# 第一次访问时初始化
print(obj.expensive_data["computed"])  # 输出: Initializing expensive data...

# 第二次访问使用缓存
print(obj.expensive_data["computed"])  # 直接返回结果

# 另一个属性的懒加载
print(obj.another_expensive_thing[:5])  # 输出: Initializing another expensive thing...
```

- **__getattr__**
```python
class LazyLoader:
    def __init__(self):
        self._cache = {}
    
    def __getattr__(self, name):
        if name not in self._cache:
            if name == 'expensive_data':
                print(f"Lazy loading {name}...")
                self._cache[name] = self._load_expensive_data()
            elif name == 'config':
                print(f"Lazy loading {name}...")
                self._cache[name] = self._load_config()
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        return self._cache[name]
    
    def _load_expensive_data(self):
        # 模拟从数据库或网络加载
        return {"items": [f"item_{i}" for i in range(100)]}
    
    def _load_config(self):
        # 模拟加载配置
        return {"timeout": 30, "retries": 3}

# 使用
loader = LazyLoader()
print("Loader created")

# 第一次访问时加载
print(loader.expensive_data["items"][:3])  # 输出: Lazy loading expensive_data...

# 第二次访问使用缓存
print(loader.config["timeout"])  # 输出: Lazy loading config...
print(loader.config["retries"])  # 直接返回缓存
```

- **函数缓存**
```python
from functools import cached_property

class CachedClass:
    def __init__(self, n):
        self.n = n
    
    @cached_property
    def computed_value(self):
        print(f"Computing for n={self.n}...")
        # 昂贵的计算
        result = sum(i * i for i in range(self.n))
        return result
    
    @cached_property
    def processed_data(self):
        print("Processing data...")
        return [x * 2 for x in range(self.n)]

# 使用
obj = CachedClass(1000)
print("Object created")

# 第一次计算
print(obj.computed_value)  # 输出: Computing for n=1000...

# 第二次使用缓存
print(obj.computed_value)  # 直接返回结果

# 另一个属性的懒加载
print(obj.processed_data[:5])  # 输出: Processing data...
```

- **元类**
```python
class LazyMeta(type):
    def __new__(cls, name, bases, attrs):
        # 标记需要懒加载的属性
        lazy_attrs = {}
        for attr_name, attr_value in attrs.items():
            if hasattr(attr_value, '_lazy'):
                lazy_attrs[attr_name] = attr_value
        
        # 创建类
        new_cls = super().__new__(cls, name, bases, attrs)
        new_cls._lazy_attrs = lazy_attrs
        return new_cls

def lazy(func):
    func._lazy = True
    return func

class DatabaseService(metaclass=LazyMeta):
    def __init__(self):
        self._cache = {}
    
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        lazy_attrs = super().__getattribute__('_lazy_attrs')
        
        if name in lazy_attrs and name not in super().__getattribute__('_cache'):
            print(f"Lazy initializing {name}...")
            value = attr(self)
            self._cache[name] = value
            return value
        
        return attr
    
    @lazy
    def database_connection(self):
        # 模拟数据库连接
        return {"connected": True, "url": "mysql://localhost:3306/mydb"}
    
    @lazy
    def cache_client(self):
        # 模拟缓存客户端
        return {"type": "redis", "host": "localhost", "port": 6379}

# 使用
service = DatabaseService()
print("Service created")

# 第一次访问时初始化
print(service.database_connection)  # 输出: Lazy initializing database_connection...

# 第二次访问使用缓存
print(service.cache_client)  # 输出: Lazy initializing cache_client...
print(service.database_connection)  # 直接返回缓存
```

- **线程安全**
```python
from threading import Lock

class ThreadSafeLazy:
    def __init__(self):
        self._lock = Lock()
        self._value = None
    
    @property
    def value(self):
        if self._value is None:
            with self._lock:
                if self._value is None:  # 双重检查锁定
                    print("Thread-safe initialization...")
                    self._value = self._initialize()
        return self._value
    
    def _initialize(self):
        # 线程安全的初始化逻辑
        return {"thread_safe": True, "data": "safe_data"}

# 使用
safe_obj = ThreadSafeLazy()
print(safe_obj.value)
```
