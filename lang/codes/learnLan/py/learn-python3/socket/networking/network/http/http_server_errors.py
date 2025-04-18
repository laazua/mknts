# -*-coding:utf-8-*-
"""
处理错误时要调用send_error(),并传入适当的错误码和一个可选的错误消息.真个响应(包括首部，状态码和响应体)会自动生成.
"""

from http.server import BaseHTTPRequestHandler


class ErrorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_error(404)


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print('Starting server, use <ctrl-c> to stop')
    server.serve_forever()
