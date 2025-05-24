### decorator

- 装饰器
```python
# 无参装饰器
def decorator(func):
    """装饰器函数: 接收被装饰的函数func"""
    def wrapper(*args, **kwargs):
        """这里的*args和**kwargs是被装饰函数的参数列表"""
        print("===== 装饰逻辑 =====")
        print("xxxx我是无参装饰器xxxx")
        return func(*args, **kwargs)

    return wrapper


# 带参装饰器
def decorator_with_args(address):
    """包装装饰器参数: address"""
    def decorator(func):
        """装饰器函数: 接收被装饰的函数func"""
        def wrapper(*args, **kwargs):
            """这里的*args和**kwargs是被装饰函数的参数列表"""
            print("===== 装饰逻辑 =====")
            print(f"xxxxxxx{address}xxxxxxxx")
            print("xxxx我是带参装饰器xxxx")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@decorator
@decorator_with_args("成都")
def greet(name):
    print("hello: ", name)


if __name__ == "__main__":

    greet("张三")

    # decorator(greet("张三"))

```