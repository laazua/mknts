"""
__init__.py
"""
from flask import Blueprint, render_template
from app import markdown_to_html


vs = Blueprint('py', __name__, template_folder='templates')


vs.route("/index.md")
def index():
    """index"""
    content = markdown_to_html('static/md/vscode/index.md')
    return render_template('index.html', content=content)

