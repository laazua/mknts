"""
__init__.py
"""
from flask import Blueprint, render_template
from app import markdown_to_html


go = Blueprint('go', __name__, template_folder='templates')


@go.route('/index.md')
def index():
    """go index"""
    content = markdown_to_html('static/md/golang/index.md')
    return render_template('index.html', content=content)
