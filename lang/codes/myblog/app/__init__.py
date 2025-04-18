"""
__init__.py
"""
import markdown
from flask import  Markup


def markdown_to_html(filename):
    """markdown to html"""
    exts = [
        'markdown.extensions.extra', 
        'markdown.extensions.codehilite', 
        'markdown.extensions.tables',
        'markdown.extensions.toc'
    ]
    mdcontent = ""
    with open(filename, 'r', encoding='utf-8') as fd:
        mdcontent = fd.read()
    html = markdown.markdown(mdcontent, extensions=exts)
    content = Markup(html)
    return content
