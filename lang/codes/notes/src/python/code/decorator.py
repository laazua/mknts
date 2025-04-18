"""
装饰器
"""

def my_decorator_with_args(arg1, arg2):
    """带参装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result
        return wrapper
    return decorator

@my_decorator_with_args("arg1_value", "arg2_value")
def say_hello(name):
    print(f"Hello, {name}!")


def my_decorator(func):
    """无参装饰器"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hi():
    print("Hello!")


class MyDecorator:
    """类装饰器"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 添加额外的功能
        print("Something is happening before the function is called.")
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")

@MyDecorator
def say_ni():
    print("Hello!")


if __name__ == "__main__":
    # 调用被装饰的函数
    say_hello("John")
    say_hi()
    say_ni()

