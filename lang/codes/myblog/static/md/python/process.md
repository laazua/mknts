## ***多进程***

* *示例代码*
```
import time
from multiprocessing import Pool


def mtask(x):
    time.sleep(2)    
    print("children process: %s" % x)
    return "P = > %d" % x

def main():
    start = time.time()
    pool = Pool(4)
    rlist = [ pool.apply_async(mtask, (i,)) for i in range(24) ] 
    pool.close()
    pool.join()
    print("time: ", time.time() - start)
    print([r.get() for r in rlist])


if __name__ == "__main__":
    main()
```
> 也可使用from concurrent.futures import ProcessPoolExecutor进程池类创建进程池。    
> 使用队列Queue进行进程间通信。    