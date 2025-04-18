## ***python多线程***

* *示例*
```
    import time
    import threading
    from concurrent.futures import ThreadPoolExecutor


    num = 0
    mutex = threading.Lock()


    def mtask(x):
        print("children thread: %s" % (x))
        time.sleep(2)
        mutex.acquire()
        global num
        if x[0] % 2 == 0:
            num += 2
        else:
            num -= 1
        mutex.release()
        return "current num: %d" % (num)


    def main():
        start = time.time()
        print("main thread start")
        pool = ThreadPoolExecutor(max_workers=5)
        futures = [ pool.submit(mtask, (i,)) for i in range(20) ]
        for f in futures:
            print(f.result())
        pool.shutdown(wait=True)
        print("main thread end")
        print("time: ", time.time() - start)


    if __name__ == "__main__":
        main()

```
