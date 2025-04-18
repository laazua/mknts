### typing模块

- **静态类型注解**
1. 类型注解可以清楚地表示函数的参数类型、返回值类型、变量的类型 .  
   这不仅提高了代码的可读性，使其他开发者甚至自己在一段时间后能够快速理解代码的意图，还增强了代码的可维护性.  

- **示例代码**
1. List
```python
"""
必须是包含整数的列表.函数的返回值类型被注解为int,即函数将返回一个整数.
"""
from typing import List


def add_numbers(nums: List[int]) -> int:
    return sum(nums)
```

2. Union
```python
"""
参数可以是整数或浮点数,该函数的返回值类型也是整数或浮点数.
"""
from typing import Union


def double_or_square(num: Union[int, float]) -> Union[int, float]:
    if isinstance(num, int):
        return num * 2
    else:
        return num ** 2
```

3. Optional
```python
"""
参数可能有值，也可能没有值使用Optional注解.
"""
from typing import Optional


def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, stranger!"
    else:
        return f"Hello, {name}!"
```

4. TypeVar
```python
"""
泛型注解
"""
from typing import TypeVar, List

T = TypeVar('T')

def get_first_element(items: List[T]) -> T:
    return items[0]

first_element = get_first_element([1, 2, 3])  # The deduced type is int
```

5. Callable
```python
"""
Callable 用于对可调用对象（通常是函数）的类型进行注解，它可以指定函数的参数类型和返回值类型.
例如,以下代码定义了一个 apply_function 函数,该函数接受可调用对象 func 和整数序列号作为参数,并返回整数列表.
"""
from typing import Callable, Sequence

def apply_function(
    func: Callable[[int, int], int],
    numbers: Sequence[int]
) -> List[int]:
    return [func(num, num) for num in numbers]
```

6. 类成员类型注解
```python
"""
在类的定义中,对类的成员变量和方法进行注释也具有重要意义.它可以清楚地描述类的结构和行为,使代码更加标准化,更易于维护.
"""
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

7. Generator
```python
"""
generate_numbers 函数的返回值类型注释为 Generator[int, None, None].其中,第一个类型参数 int 表示 generator 生成的元素类型为整数.
这两个 None 值分别表示生成器在生成元素时不需要额外的输入(通常在使用 send 方法时可能会有输入,这里的 None 表示不需要输入),
并且生成器在结束时返回 None(生成器通常在结束时返回 None).
通过这个类型注解,其他开发者在使用这个 generator 函数时可以清楚地知道 generator 生成的数据类型，方便正确处理 generator 返回的结果.
"""
from typing import Generator

def generate_numbers(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i
```

8. 类型嵌套注解
```python
"""
在此定义中,Tree 类型定义为列表,列表中的元素可以是整数或字典.此字典的键是字符串,值为 Tree 类型，形成递归结构.
"""
from typing import List, Dict, Union

Tree = List[Union[int, Dict[str, 'Tree']]]
```

9. 类型别名注解
```python
"""
定义自定义类型别名是提高代码可读性的有效方法.通过为复杂类型定义简洁明了的别名,可以使代码更加清晰易懂,也便于在代码中统一修改和维护类型.
例如,在处理与用户相关的数据时，可以定义以下类型别名.
"""
UserId = int
Username = str

def get_user_details(user_id: UserId) -> Tuple[UserId, Username]:
    # some code
```

- **类型检查工具**
1. mypy