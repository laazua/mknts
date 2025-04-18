## ***异步io编程***

* *说明*
```
  协程的开销比线程更小,所以在能够使用协程处理io高并发的场景下,尽量使用协程处理
```

* *声明协程*
* > async/await语法声明协程
```
import asyncio


async def hello(s):
    print("xxx")
    await asyncio.sleep(s)
    print("ooo")
```

* *运行协程*
* >asyncio.run(hello())

* *并发多个协程任务*
* > asyncio.create_task()
```
async def main():
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))

    await task1
    await task2

    # 或者使用asyncio.TaskGroup
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(hello(1))
        task2 = tg.create_task(hello(2))
```

* *可等待对象类型*
* > 协程: async/await定义的函数
* > 任务: create_task()接口返回的一个任务
* > Future: 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果

* *更多异步io参考python官网*