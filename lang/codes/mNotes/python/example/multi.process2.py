# 创建一个Process类的实例,并指定目标任务函数

from multiprocessing import Process
def task(some_word):
    print(some_word)

if __name__ == '__main__':
    p_one = Process(target=task, args=("hello world",))
    p_tow = Process(target=task, args=("ni hao",))
    p_one.start()
    p_tow.start()
    p_one.join()
    p_tow.join()