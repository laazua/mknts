import threading
import time

# 定义一个共享变量和锁
shared_sum = 0
lock = threading.Lock()

def add_to_sum(n):
    global shared_sum
    for _ in range(n):
        with lock:
            shared_sum += 1

def main():
    num_threads = 10
    increments_per_thread = 1000000
    threads = []

    # 创建并启动线程
    for _ in range(num_threads):
        thread = threading.Thread(target=add_to_sum, args=(increments_per_thread,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f'Total sum: {shared_sum}')

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Time taken: {end_time - start_time} seconds')
