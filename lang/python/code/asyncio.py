import asyncio
import time


async def do_task(num):
    print(f"Run task {num}")
    await asyncio.sleep(2.0)


async def do_rate_limited(semaphore, num):
    print(f"Run task {num}")
    async with semaphore:
        await asyncio.sleep(2.0)


async def main():
    ### asyncio.gather() 示例
    # tasks = [do_task(i) for i in range(10)]
    # results = await asyncio.gather(*tasks)

    ### asyncio.as_completed() 示例
    # results = []
    # tasks = [do_task(i) for i in range(10)]
    # for task in asyncio.as_completed(tasks):
    #     result = await task
    #     results.append(result)

    ### asyncio.create_task() 示例
    # results = []
    # tasks = [asyncio.create_task(do_task(i)) for i in range(10)]
    # for task in tasks:
    #     result = await task
    #     results.append(result)

    ### 信号量[限速]和asyncio.gather() 示例
    # semaphore = asyncio.Semaphore(3)
    # tasks = [do_rate_limited(semaphore, i) for i in range(10)]
    # results = await asyncio.gather(*tasks)

    ### 信号量[限速]和asyncio.as_completed() 示例
    # semaphore = asyncio.Semaphore(5)
    # results = []
    # tasks = [do_rate_limited(semaphore, i) for i in range(10)]
    # for task in asyncio.as_completed(tasks):
    #     result = await task
    #     results.append(result)

    ### 信号量[限速]和asyncio.create_task() 示例
    semaphore = asyncio.Semaphore(5)
    results = []
    tasks = [asyncio.create_task(do_rate_limited(semaphore, i)) for i in range(10)]
    for task in tasks:
        result = await task
        results.append(result)


if __name__ == '__main__':
    start = time.perf_counter()
    ### 新式: 获取事件循环，运行任务直到它们被标记为完成，然后关闭事件循环
    # asyncio.run(main())
    ### 老式: 获取事件循环，运行任务直到它们被标记为完成，然后关闭事件循环
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    print(f"total time: {time.perf_counter()-start}")
