import functools

from flask import Blueprint, g, render_template, request, redirect, url_for, session, current_app

from taoist.db import get_db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        # 查询数据库
        g.user = get_db()

@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None
        
        # 跟数据库对比用户和密码
        if username != "root":
            error = "username error !"
        if password != "123456":
            error = "password error !"
        if error is None:
            session.clear()
            # 将userId存储再session中
            session["user_id"] = 1
            current_app.logger.info(f"{username} login success")
            return redirect(url_for("jobs.dashboard"))

    return render_template("login.html")


@auth_bp.route("/register", methods=("GET", "POST"))
def register():

    return render_template("register.html")


@auth_bp.route("logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))