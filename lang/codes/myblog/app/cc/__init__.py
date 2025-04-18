"""
__init__.py
"""
from flask import Blueprint, render_template
from app import markdown_to_html


cc = Blueprint('dc', __name__, template_folder='templates')


@cc.route('/index.md')
def index():
    """cc index"""
    content = markdown_to_html('static/md/cc/index.md')
    return render_template('index.html', content=content)