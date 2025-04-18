# -*-coding:utf-8-*-
"""
如果一个应用需要花很长时间来处理它下载的资源,或者受到抑制,需要在下载之间暂停,那么这样的应用应当以它下载内容的寿命为根据,定期检查新的
robots.txt文件.这个寿命并不是自动管理的, 不过有一些简单方法可以方便的跟踪其寿命.
"""

from urllib import robotparser
import time


AGENT_NAME = 'PyMOTW'
parser = robotparser.RobotFileParser()
# use the local copy
parser.set_url('file:robots.txt')
parser.read()
parser.modified()

PATHS = [
    '/',
    '/PyMOTW',
    '/admin',
    '/downloads/PyMOTW-1.92.tar.gz',
]

for path in  PATHS:
    age = int(time.time() - parser.mtime())
    print('age:', age, end=' ')
    if age > 1:
        print('rereading robots.txt')
        parser.read()
        parser.modified()
    else:
        print()
    print('{!:>6} {}'.format(parser.can_fetch(AGENT_NAME, path), path))
    # simulate a delay in processing.
    time.sleep(1)
    print()
