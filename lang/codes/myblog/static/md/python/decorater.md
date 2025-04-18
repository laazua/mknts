### ***装饰器***

* *说明*
> 装饰器是可调用的对象，其参数是另一个函数(被装饰的函数)，装饰器在被装饰的函数定义后立即执行


* *示例*
```
from functools import wraps


def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something
        print(f"装饰器函数1 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something
        print(f"装饰器函数2 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@decorator_one
@decorator_two
def say(name="hi"):
    print(f"say {name}")


if __name__ == "__main__":
    say("hello")


## 输出如下:
# 装饰器函数1 say
# 装饰器函数2 say
# say hello
```