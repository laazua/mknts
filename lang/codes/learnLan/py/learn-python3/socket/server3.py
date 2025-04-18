# -*- coding:utf-8 -*-
"""
web server with socket.io
pip install python-socketio
pip install aiohttp
"""

from aiohttp import web
import socketio


## create a new async socket IO Server
sio = socketio.AsyncServer()

## create a new aiohttp web application
app = web.Application()

## Binds our socket.IO server to our Web App
sio.attach(app)

## we can define aiohttp endpoints just as we normally
## would with no change
async def index(request):
    with open('index.html')as fd:
        return web.Response(text=fd.read(), content_type='text/html')


## if we wanted to create a new websocket endpoint,
## use this decorator, passing in the name of the
## event we wish to listen out for
@sio.on('message')
async def print_message(sid, message):
    """
    when we receive a new event of type 'message' through
    a socket.io connection we print the socket ID and the message
    """
    print("socket ID: ", sid)
    print(message)

app.router.add_get('/', index)
if __name__ == "__main__":

    web.run_app(app)