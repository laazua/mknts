### concurrent.futures

- **线程池**
```python
# IO密集型任务
import time
import concurrent.futures


def task(n):
    print(f"任务 {n} 开始")
    time.sleep(2)
    print(f"任务 {n} 完成")
    return f"结果 {n}"


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务
        futures = [executor.submit(task, i) for i in range(5)]
        # 获取结果
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
```

- **进程池**
```python
# CPU密集型任务
import math
import concurrent.futures


def compute_factorial(n):
    return math.factorial(n)


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # 提交任务
        futures = [executor.submit(compute_factorial, i) for i in range(5, 10)]
        # 获取结果
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
```