# -*-coding:utf-8-*-
"""
robotparser为robots.txt文件格式实现一个解析器, 提供了一个函数来检查给定用户代理是否可以访问一个资源.这个模块就可以用于合法蜘蛛或者需要
抑制的其他爬虫应用中.
robots.txt文件格式是一个基于文本的简单访问控制系统, 用于自动访问web资源的计算机程序(如‘蜘蛛’‘爬虫’等).这个文件由记录构成,各个记录会指
定程序的用户代理标识符,后面是该代理不能访问的一个URL(或URL前缀)列表.如下:
Disallow: /downloads/
Disallow: /media/
Disallow: /static/
Disallow: /codehosting/
这个文件会阻止访问网站中某些计算资源代价昂贵的部分,如果搜索引擎试图索引这些部分,那么可能会让服务器负载过重.
"""