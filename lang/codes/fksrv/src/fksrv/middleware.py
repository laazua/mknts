

class SimpleMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # 在处理请求前执行的操作
        print("Middleware: Before handling the request")

        # 将请求传递给 Flask 应用
        response = self.app(environ, start_response)

        # 在处理请求后执行的操作
        print("Middleware: After handling the request")

        return response
