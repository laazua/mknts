# -*-coding:utf-8-*-
"""
    urllib.request提供了对HTTP(S), FTP和本地iiii文件访问的内置支持. 为了增加对其他URL类型的支持, 可以注册另外的协议处理器.例如,
为了支持指向远程NFS服务器上任意文件的URL,而不需要用户在访问文件之前先装载路径.可以创建一个派生BaseHandler的类.并包含一个nfs_open()方法.
    协议特定的open()方法有一个参数, 即Request实例, 它会返回一个对象, 这个对象有一个read()方法来读取数据, 一个info()方法来返回响应首部,
还有一个geturl()方法返回所读文件的具体URL. 要满足这些需求, 一种简单的办法就是创建urllib.response.addinfourl的一个实例, 然后把首部,URL
和打开的文件句柄传入它的构造函数.
"""

import io
import os
import mimetypes
import tempfile
from urllib import request
from urllib import response


class NFSFile:
    def __init__(self, tempdir, filename):
        self.tempdir = tempdir
        self.filename = filename
        with open(os.path.join(tempdir, filename), 'rb') as f:
            self.buffer = io.BytesIO(f.read())

    def read(self, *args):
        return self.buffer.read(*args)

    def readline(self, * args):
        return self.buffer.readline(*args)

    def close(self):
        print('\nNFSFile:')
        print('  unmounting {}'.format(os.path.basename(self.tempdir)))
        print('  when {} is closed'.format(os.path.basename(self.filename)))


class FauxNFSHandller(request.BaseHandler):
    def __init__(self, tempdir):
        self.tempdir = tempdir
        super().__init__()

    def nfs_open(self, req):
        url = req.full_url
        directory_name, file_name = os.path.split(url)
        server_name = req.host
        print('FauxNFSHandler simulating mount: ')
        print('  Remote path: {}'.format(directory_name))
        print('  Server     : {}'.format(server_name))
        print('  Local path : {}'.format(os.path.basename(tempdir)))
        print('  Filename   : {}'.format(file_name))
        local_file = os.path.join(tempdir, file_name)
        fp = NFSFile(self.tempdir, file_name)
        content_type = (mimetypes.guess_type(file_name)[0] or 'application/octet-stream')
        stats = os.stat(local_file)
        size = stats.st_size
        headers = {
            'Content-type': content_type,
            'Content-length': size,
        }

        return response.addinfourl(fp, headers, req.get_full_url())


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tempdir:
        # populate the temporary file for the simulation.
        filename = os.path.join(tempdir, 'file.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Contents of file.txt')

        # construct an opener with our NFS handler and register it as the default opener
        opener = request.build_opener(FauxNFSHandller(tempdir))
        request.install_opener(opener)

        # open the file through a URL
        resp = request.urlopen('nfs://remote_server/path/to/the/file.txt')
        print()
        print('READ CONTENTS: ', resp.read())
        print('URL          : ', resp.geturl())
        print('HEADERS:')
        for name, value in sorted(resp.info().items()):
            print('  {:<15} = {}'.format(name, value))
        resp.close()
