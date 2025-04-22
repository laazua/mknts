from flask import Blueprint, render_template


bp = Blueprint("test", __name__, url_prefix="/test")


@bp.route("/footers", methods=("GET", "POST"))
def footers():
    return render_template("footers.html")


@bp.route("/navbars", methods=("GET", "POST"))
def navbars():
    return render_template("navbars.html")


@bp.route("/sidebars", methods=("GET", "POST"))
def sidebars():
    return render_template("sidebars.html")


@bp.route("/dashboard", methods=("GET", "POST"))
def dashboard():
    return render_template("dashboard.html")


@bp.route("dashboardrtl", methods=("GET", "POST"))
def dashboardrtl():
    return render_template("dashboard-rtl.html")


@bp.route("/index", methods=("GET", "POST"))
def index():
    return render_template("index.html")
