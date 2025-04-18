"""
__init__.py
"""
from flask import Blueprint, render_template
from app import markdown_to_html


dc = Blueprint('dc', __name__, template_folder='templates')


@dc.route('/index.md')
def index():
    """docker index"""
    content = markdown_to_html('static/md/docker/index.md')
    return render_template('index.html', content=content)
