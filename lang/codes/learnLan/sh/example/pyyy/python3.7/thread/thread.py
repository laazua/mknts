# coding=utf-8
from threading import Thread, current_thread, Lock, local

num = 0
lock = Lock()

global_data = local()


def calc() -> None:
    """
    :param: None
    :return: None
    """
    global num
    print('thread %s is running...' % current_thread().name)
    for _ in range(10000):
        lock.acquire()
        num += 1
        lock.release()
    print('thead %s ended.' % current_thread().name)


def test_calc() -> None:
    """
    :param: None
    :return: None
    """
    print('thread %s is running...' % current_thread().name)
    threads = []
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].start()
    for i in range(5):
        threads[i].join()

    print('global num %d' % num)
    print('thread %s ended.' % current_thread().name)


def echo() -> None:
    """
    :param: None
    :return: None
    """
    num = global_data.num
    print(current_thread().name, num)


def add() -> None:
    """
    :param: None
    :return: None
    """
    print("thread %s is running..." % current_thread().name)
    global_data.num = 0
    for _ in range(10000):
        global_data.num += 1
    echo()

    print("thread %s ended." % current_thread().name)


def test_add() -> None:
    """
    :param: None
    :return: None
    """
    print("thread %s is running..." % current_thread().name)

    threads = []
    for i in range(5):
        threads.append(Thread(target=add))
        threads[i].start()
    for i in range(5):
        threads[i].join()

    print("thread %s ended" % current_thread().name)


if __name__ == '__main__':
    test_calc()
    print("++++++++++++++++++++++++")
    test_add()