"""
__init__.py
"""
from flask import Blueprint, render_template
from app import markdown_to_html


py = Blueprint('py', __name__, template_folder='templates')


@py.route('/index.md')
def index():
    """python index"""
    content = markdown_to_html('static/md/python/index.md')
    return render_template('index.html', content=content)


@py.route('/base.md')
def index_base():
    """python base"""
    content = markdown_to_html('static/md/python/base.md')
    return render_template('index.html', content=content)


@py.route('/socket.md')
def index_socket():
    """python socket"""
    content = markdown_to_html('static/md/python/socket.md')
    return render_template('index.html', content=content)


@py.route('/env.md')
def index_env():
    """python env"""
    content = markdown_to_html('static/md/python/env.md')
    return render_template('index.html', content=content)


@py.route('/process.md')
def index_process():
    """python process"""
    content = markdown_to_html('static/md/python/process.md')
    return render_template('index.html', content=content)


@py.route('/thread.md')
def index_thread():
    """python thread"""
    content = markdown_to_html('static/md/python/thread.md')
    return render_template('index.html', content=content)


@py.route('/sockets.md')
def index_sockets():
    """socketserver"""
    content = markdown_to_html('static/md/python/sockets.md')
    return render_template('index.html', content=content)


@py.route('/async.md')
def index_async():
    """asyncio"""
    content = markdown_to_html('static/md/python/async.md')
    return render_template('index.html', content=content)


@py.route('/pattern.md')
def index_pattern():
    """design pattern"""
    content = markdown_to_html('static/md/python/pattern.md')
    return render_template('index.html', content=content)
