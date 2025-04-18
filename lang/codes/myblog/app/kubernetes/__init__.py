"""
__init__.py
"""
from flask import Blueprint, render_template
from app import markdown_to_html


ks = Blueprint('ks', __name__, template_folder='templates')


@ks.route('/index.md')
def index():
    """k8s index"""
    content = markdown_to_html('static/md/k8s/index.md')
    return render_template('index.html', content=content)
