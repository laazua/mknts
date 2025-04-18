# coding=utf-8
# 编写跨平台多进程，windows进程模型与linux不一致
import os, time
from multiprocessing import Process, Pool, Queue


def child_process(name: str) -> None:
    """
    :param name: process name
    :return: None
    """
    print("Run child process %s (%s)" % (name, os.getpid()))


def test_child_process() -> None:
    """
    :param: None
    :return: None
    """
    print("Parent process %s." % os.getpid())
    p = Process(target=child_process, args=("test",))
    print("process will start.")
    p.start()
    p.join()
    print("process ended.")


def process_pool(x) -> None:
    """
    进程池
    :param x:
    :return:
    """
    print("Run task %s (pid: %s)" % (x, os.getpid()))
    time.sleep(2)
    print("Task %s result is: %s" % (x, x * x))


def test_process_pool() -> None:
    """
    test process pool
    :return: None
    """
    print("Parent process %s." % (os.getpid()))
    p = Pool(4)  # set number of process
    for i in range(5):
        p.apply_async(process_pool, args=(i,))  # 设置每个进程要执行的函数和参数
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")


# 进程间通信:Pipe, Queue
def write_data(queue: Queue) -> None:
    """
    向队列中写入数据
    :param queue: 一个创建好的队列实例
    :return: None
    """
    try:
        n = 1
        while n < 5:
            print("write, %d" % n)
            queue.put(n)
            time.sleep(2)
            n += 1
    except BaseException as e:
        print("write task error: " + e)
    finally:
        print("write task done")


def read_data(queue: Queue) -> None:
    """
    从队列中读取数据
    :param queue: 一个创建好的队列实例, 同上write_data
    :return: None
    """
    try:
        n = 1
        while n < 5:
            print("read, %d" % queue.get())
            time.sleep(2)
            n += 1
    except BaseException as e:
        print("read task error: " + e)
    finally:
        print("read task done.")


def test_writeANDread_task() -> None:
    """
    test write_data and read_data
    :return: None
    """
    queue = Queue()    # 父进程创建queue,并传递给各个子进程

    pw = Process(target=write_data, args=(queue,))
    pr = Process(target=read_data, args=(queue,))

    pw.start()      # 启动子进程pw,写入
    pr.start()      # 启动子进程pr,读取
    pw.join()       # 等待pw结束
    pr.join()       # 等待pr结束
    print("Done.")


if __name__ == "__main__":
    test_child_process()
    print("+++++++++++++++++++++++++++++++")
    test_process_pool()
    print("+++++++++++++++++++++++++++++++")
    test_writeANDread_task()