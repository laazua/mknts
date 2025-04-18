class Calculator:
    """对象链式调用"""
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self
    
    def subtract(self, num):
        self.result -= num
        return self
    
    def multiply(self, num):
        self.result *= num
        return self
    
    def divide(self, num):
        self.result /= num
        return self
    
    def clear(self):
        self.result = 0
        return self

# 示例用法
calc = Calculator()
result = calc.add(5).multiply(3).subtract(2).divide(4).clear().add(10).result
print(result)  # 输出: 10

##############################################################################
def chainable(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return args[0]
    return wrapper

@chainable
def greet(name):
    """函数链式调用"""
    print(f"Hello, {name}!")

greet("Alice").greet("Bob").greet("Charlie")

##############################################################################
class Chainable:
    """上下文管理器链式调用"""
    def __init__(self, value):
        self.value = value
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def method1(self):
        print(f"Method 1: {self.value}")
        return self
    
    def method2(self):
        print(f"Method 2: {self.value}")
        return self
    
    def method3(self):
        print(f"Method 3: {self.value}")
        return self

with Chainable("Hello") as c:
    c.method1().method2().method3()

###############################################################################
class Chainable:
    def __init__(self):
        self.steps = []
    
    def __getattr__(self, name):
        self.steps.append(name)
        return self
    
    def execute(self):
        # 执行操作
        print("Executing steps:", self.steps)

c = Chainable()
c.step1.step2.step3.execute()  #输出：Executing steps: ['step1', 'step2', 'step3']