# -*-coding:utf-8-*-
"""
send_header方法向HTTP响应增加首部数据.这个方法有两个参数: 首部名和值
"""

from http.server import BaseHTTPRequestHandler
import time


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header(
            'Content-Type',
            'text/plain; charset=utf-8',
        )
        self.send_header(
            'Last-Modified',
            self.date_time_string(time.time())
        )
        self.end_headers()
        self.wfile.write('Response body\n'.encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <ctrl-c> to stop')
    server.serve_forever()
