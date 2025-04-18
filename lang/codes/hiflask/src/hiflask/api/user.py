"""
用户相关接口
"""

from flask import Blueprint


bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=("POST", "GET"))
def login():
    return "login success !"
