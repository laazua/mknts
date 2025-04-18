# -*-coding:utf-8-*-
"""
HTTPServer是socketserver.TCPServer的一个简单子类,并不使用多线程或进程来处理请求,要增加线程或进程,需要使用适当的mix-in技术从
socketserver创建一个新类.
用ForkingMixIn替换ThreadingMixIn会得到类似的结果,不过需要使用单独的进程而不是线程
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write(b'\n')


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in separate thread"""


if __name__ == '__main__':
    server = ThreadedHTTPServer(('', 8080), Handler)
    print('Starting server, use <ctrl-c> to stop')
    server.serve_forever()
