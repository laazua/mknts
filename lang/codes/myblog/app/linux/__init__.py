"""linux doc"""

from flask import Blueprint, render_template
from app import markdown_to_html


lx = Blueprint('lx', __name__, template_folder='templates')


@lx.route('/index.md')
def index():
    """linux"""
    content = markdown_to_html('static/md/linux/index.md')
    return render_template('index.html', content=content)


@lx.route('/base.md')
def index_base():
    """base"""
    content = markdown_to_html('static/md/linux/base.md')
    return render_template('index.html', content=content)


@lx.route('/desc.md')
def index_desc():
    """linux desc"""
    content = markdown_to_html('static/md/linux/desc.md')
    return render_template('index.html', content=content)


@lx.route('/elk.md')
def index_elk():
    """elk"""
    content = markdown_to_html('static/md/linux/elk.md')
    return render_template('index.html', content=content)


@lx.route('/kafka.md')
def index_kafka():
    """kafka"""
    content = markdown_to_html('static/md/linux/kafka.md')
    return render_template('index.html', content=content)


@lx.route('/zookeeper.md')
def index_zookeeper():
    """zookeeper"""
    content = markdown_to_html('static/md/linux/zookeeper.md')
    return render_template('index.html', content=content)
