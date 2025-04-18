# -*- coding:utf-8 -*-
"""
多线程
线程与线程之间是无感知的,即线程之间不知道各自都执行到了哪一步.所以当线程对同一资源争抢时,要加锁
多线程设计要减少线程创建和销毁所带来的系统资源的损耗.(线程池)
"""
import threading, time

#=====================================================#
class TestThread(threading.Thread):
    """
    多线程类
    """
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        
    def run(self):
        """
        必须函数,被start()调用, 执行要做的具体线程事务
        """        
        t_name = threading.current_thread().name
        test_thread(self.lock, t_name)


def test_thread(lock, t_name):
    """
    TestThread类要执行的线程事务
    使用with语句加锁更加优雅
    lock.acquire()
    print(f"thread start: {t_name}")
    print("ha ha ha.")
    time.sleep(1)
    print(f"thread   end: {t_name}")
    lock.release()
    """
    with lock:
        print(f"thread start: {t_name}")
        print("hahaha.")
        time.sleep(2)
        print(f"thread end: {t_name}")
    print("Exit main thread.")

def do_test_thread():
    """
    线程事务测试函数
    """
    # 自定义锁要从实现的线程类外部传入,如果锁定义在线程内部,则不同线程的所就是不同的锁变量,就达不到资源同步的效果
    lock = threading.Lock()
    tlist = []

    # 创建线程实例
    for i in range(10):
        tlist.append(TestThread(lock))

    # 启动线程实例
    for t in tlist:
        t.start()

    # 等待线程实例执行完毕后才结束
    for j in tlist:
        j.join()
#======================================================#


from concurrent.futures import ThreadPoolExecutor
def do_task(i):
    """
    测试线程池
    """
    print(f"Thread-{i}, ha ha")
    time.sleep(2)


def test_thread_pool():
    """
    添加线程池对象
    """
    with ThreadPoolExecutor(max_workers=3) as t_pool:
        plist = []
        # l = [1, 2, 3, 4, 5]
        for i in range(1, 6):
            plist.append(t_pool.submit(do_task, i))
            # plist.append(t_pool.map(do_task, l))

        for j in plist:
            print(f"task: {j.done()}")
            print(j.result())
        

if __name__ == "__main__":
    do_test_thread()
    # test_thread_pool()
    for i in range(10):
        t = threading.Thread(target=do_task, args=(i,))
        t.start()
        