# -*- condig: utf-8 -*-
"""
协程
可等待对象: 协程, 任务, Future
"""
import asyncio


# 通过async/await语法进行声明
async def test_asycn():
    """
    这是一个协程声明的示例函数
    """
    print("hahahaha")
    await asyncio.sleep(2)
    print("hehehehe")


# asyncio.create_task()打包协程任务
import time
async def do_task(arg):
    """定义一个可等待的协程"""
    print(arg)
    time.sleep(2)

async def test_task():
    """
    协程任务
    """
    tasks = []
    start = time.time()
    for i in range(11):
        tasks.append(asyncio.create_task(
            do_task(i)
        ))
    for task in tasks:
        await task     # 等待协程任务执行完毕,即,被asyncio.create_task()函数打包的任务
    end = time.time()
    print("total time: ", end - start)


# 并发运行协程任务
async def test_multi_task():
    """
    并发运行协程任务
    """
    # 同时调用多个任务
    await asyncio.gather(
        do_task("I am the first task."),
        do_task("I am the second task."),
        do_task("I am the third task."),
    )



if __name__ == "__main__":
    # 调用asyncio.run()运行asyncio程序
    #asyncio.run(test_asycn())

    asyncio.run(test_task())
    #asyncio.run(test_multi_task())