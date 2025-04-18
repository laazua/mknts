# -*-coding:utf-8-*-
"""
支持POST请求需要多做一些工作,因为基类不会自动解析表单数据.cgi模块提供了FieldStorrage类,如果给定了正确的输入,它便知道如何解析表单
"""

import cgi
from http.server import BaseHTTPRequestHandler
import io


class PostHandlerr(BaseHTTPRequestHandler):
    def do_POST(self):
        # parse the form data posted.
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD:': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )
        # begin the response
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )
        out.write('Client: {}\n'.format(self.client_address))
        out.write('User-agent: {}\n'.format(
            self.headers['user-agent']
        ))
        out.write('Path: {}\n'.format(self.path))
        out.write('Form data:\n')

        # echo back information about what was posted in the form.
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # the field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write(
                    '\tUpload {} as {1r} ({} bytes)\n'.format(
                        field, field_item.filename, file_len
                    )
                )
            else:
                # regular form value
                out.write('\t{}={}\n'.format(field, form[field].value))
        # disconnect the  encoding wrapper from the underlying buffer so that deleting the wrapper
        # dose not close the socket, which is still being used by the server.
        out.detach()


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandlerr)
    print('Starting server, use <ctrl-c> to stop')
    server.serve_forever()
