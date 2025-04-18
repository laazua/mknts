# -*- coding:utf-8 -*-
'''
def func1():
    print(1)

    print(2)


def func2():
    print(3)
    print(4)


func1()
func2()

# greenlet模块实现协程


# yield实现协程

def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)

# asyncio内置模块实现(python3.4+)
import asyncio


@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)   # 遇到I0耗时操作,自动切换到其他task中的任务
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future( func1() ),

    asyncio.ensure_future( func2() )
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

# async & await关键字(python3.7以前), await后面跟的是协程对象,Future,task
import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(3)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

#python3.7+
import asyncio


async def func1():
    print(1)
    #await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    #await asyncio.sleep(3)
    print(4)


async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2())
    ]

    done, pend = await asyncio.wait(tasks, timeout=None)


if __name__ == '__main__':
    asyncio.run(main())

# 协程的意义: 利用在一个线程中如果遇到io等待的时间,线程不会一直等待,会利用空闲的时间去做其他的事。

# 线程池&进程池
import time
from concurrent.futures import Future
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor


def func(arg):
    time.sleep(2)
    print(arg, end='   ')


def main():
    # 创建线程池
    pools = ThreadPoolExecutor(max_workers=10)

    # 创建进程池
    # pools = ProcessPoolExecutor(max_workers=10)
    for i in range(10):
        res = pools.submit(func, i)
        # print(res)


if __name__ == '__main__':
    main()


# 异步可迭代对象：必须通过__aiter__()方法返回一个asynchronous.iterator
import asyncio


class Reader(object):
    """自定义异步可迭代器"""
    def __init__(self):
        self.count = 0
    
    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.readline()
        if value == None:
            raise StopAsyncIteration
        return value


async def main():
    ob = Reader()
    # async for 必须放在一个协程函数中执行
    async for item in ob:
        print(item)

if __name__ == '__main__':
    asyncio.run( main() )


# 异步上下文管理器
import asyncio


class AsyncContextManager(object):
    def __init__(self, conn='fd'):
        self.conn = conn

    async def do_something(self, *args):
        # 异步要做的事
        print(args)

    async def __aenter__(self):
        return self

    async def __aexit__(self, axc_type, exc, tb):
        await asyncio.sleep(2)


async def main():
    async with AsyncContextManager(12) as fd:
        result = await fd.do_something('hello world')

if __name__ == '__main__':
    asyncio.run( main() )


# unloop 性能更好
pip install uvloop
import asyncio
import uvloop
asyncio.set_evnet_loop_policy(uvloop.EventLoopPolicy())


# 案例1 (异步操作redis) pip install aioredis
import asyncio

import aioredis


async def execte(address, pwd):
    print('start', address)
    redis = await aioredis.create_redis(address, pwd)
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()
    await redis.wait_closed()

    print('end', address)


if __name__ == '__main__':
    asyncio.run(execte('redis://127.0.0.1', '123456'))


# 示例2 （异步操作mysql） pip install aiomysql

import asyncio

import aiomysql


async def execute(address, pwd):
    print('start', address)
    conn = await aiomysql.connect(host=address, port=3306, user='root', password=pwd, db='test')

    cur = await conn.cursor()

    await cur.execute('SELECT test.User FROM user')

    result = await cur.fetchall()
    print(result)

    await cur.close()
    conn.close()
    print('end', address)


if __name__ == '__main__':
    tasks = [
        execute('127.0.0.1', '123456'),
        execute('127.0.0.1', '456789')
    ]
    asyncio.run(asyncio.wait(tasks))
'''
