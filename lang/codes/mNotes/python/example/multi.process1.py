# 自定义一个类并继承Process类,重写其__init__()方法和run()方法
from multiprocessing import Process


class TProcess(Process):
    def __init__(self, some_word):
        super().__init__()
        self.some_word = some_word

    def run(self):
        print(self.some_word)


if __name__ == '__main__':
    p_one = TProcess("hello world")
    p_tow = TProcess("ni hao")
    p_one.start()
    p_tow.start()
    p_one.join()
    p_tow.join()