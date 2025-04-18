# -*- coding: utf-8 -*-

import os, sys
import time

# 普通进度条
def process_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("Download process: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")


# 带时间的进度条
def process_bar_time():
    scale = 50
    print("执行开始".center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
        time.sleep(0.1)
    print("\n" + "执行结束".center(scale // 2, "-"))


# tpdm进度条
from time import sleep
from tqdm import tqdm
def process_bar_tpdm():
    for i in tqdm(range(1, 500)):
        # 模拟你的任务
        sleep(0.01)
    sleep(0.5)


# progress进度条
from progress.bar import IncrementalBar
def progress():
    mlist = [1,2,3,4,5,6,7,8]
    bar = IncrementalBar("Countdown", max = len(mlist))
    for item in mlist:
        bar.next()
        time.sleep(1)
        bar.fibish()


# alive_progress进度条
from alive_progress import alive_bar
def alive_progress_process():
    items = range(100)
    with alive_bar(len(items)) as bar:
        for item in items:
            # process each item


# 可视化进度条
import PySimpleGUI as sg
def gui_process_bar():
    mlist = [1,2,3,4,5,6,7,8]
    for i, item in enumerate(mlist):
        sg.one_line_progress_meter("this is my process meter!", i + 1, len(mlist), "-key-")
        time.sleep(1)


if __name__ == "__main__":
    process_bar()
    process_bar_time()
    #process_bar_tpdm()