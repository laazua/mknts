from flask import Blueprint, render_template


jobs_bp = Blueprint("jobs", __name__, url_prefix="/jobs")


@jobs_bp.route("/dashboard", methods=("GET", "POST"))
def dashboard():
    
    return render_template("dashboard.html")
