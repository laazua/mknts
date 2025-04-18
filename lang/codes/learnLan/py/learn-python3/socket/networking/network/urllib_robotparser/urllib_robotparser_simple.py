# -*-coding:utf-8-*-
"""
一个简单的爬虫应用可以使用RobotFileParse.can_fetch()测试是否允许下载一个页面
"""

from urllib import parse
from urllib import robotparser


AGENT_MAME = 'PyMOTW'
URL_BASE = 'https://pymotw.com/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robotstxt'))
parser.read()

PATHS = [
    '/',
    '/PyMOTW/',
    '/admin/',
    '/downloads/PyMOTW-1.92.tar.gz',
]
for path in PATHS:
    print('{!r:>6} : {}'.format(parser.can_fetch(AGENT_MAME, path), path))
    url = parse.urljoin(URL_BASE, path)
    print('{!r:>6} : {}'.format(parser.can_fetch(AGENT_MAME, url), url))
    print()
