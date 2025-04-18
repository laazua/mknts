# -*- coding: utf-8 -*-
"""
event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数
coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用
future 对象： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。
async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield
"""

import time
import asyncio
from queue import Queue
from threading import Thread


## 协程工作流程
async def test(args):
    """协成函数"""
    print(args)


# 定义协程对象
coroutine = test("haha")
# 定义时间循环对象容器
loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# 将协程转为task任务
task = loop.create_task(coroutine)
# 将task任务添加到时间循环对象容器中并触发
loop.run_until_complete(task)
# loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(asyncio.gather(*tasks))


## 协程并发
# 协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

# 协程对象
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

# 将协程转成task，并组成list
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

# 将协程注册到事件循环中
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))


## 协程嵌套
# 用于内部的协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

# 外部的协程函数
async def main():
    # 创建三个协程对象
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    # 将协程转为task，并组成list
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    # 【重点】：await 一个task列表（协程）
    # dones：表示已经完成的任务
    # pendings：表示未完成的任务
    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print('Task ret: ', task.result())

    # results = await asyncio.gather(*tasks)
    # for result in results:
    #    print('Task ret: ', result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


## 动态添加协程
# 主线程同步
def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()

def do_sleep(x, queue, msg=""):
    time.sleep(x)
    queue.put(msg)

queue = Queue()

new_loop = asyncio.new_event_loop()

# 定义一个线程，并传入一个事件循环对象
t = Thread(target=start_loop, args=(new_loop,))
t.start()

print(time.ctime())

# 动态添加两个协程
# 这种方法，在主线程是同步的
new_loop.call_soon_threadsafe(do_sleep, 6, queue, "第一个")
new_loop.call_soon_threadsafe(do_sleep, 3, queue, "第二个")

# 这种方法，在主线程是异步的
# asyncio.run_coroutine_threadsafe(do_sleep(6, queue, "第一个"), new_loop)
# asyncio.run_coroutine_threadsafe(do_sleep(3, queue, "第二个"), new_loop)

while True:
    msg = queue.get()
    print("{} 协程运行完..".format(msg))
    print(time.ctime())