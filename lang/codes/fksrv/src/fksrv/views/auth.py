import functools

from flask import (
    Blueprint,
    g,
    redirect,
    url_for,
    request,
    render_template,
    jsonify,
    session,
    flash,
)


bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """login required"""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = "root"


@bp.route("index", methods=("GET",))
def index():
    return render_template("index.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if username != "root":
            error = "Incorrect username"
        if password != "123456":
            error = "Incorrect password"

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = 1
            return redirect(url_for("auth.dashboard"))

        flash(error)

    return render_template("login.html")


@bp.route("/register", methods=("GET", "POST"))
def register():
    return jsonify({"message": "register success"})


@bp.route("/dashboard", methods=("GET", "POST"))
@login_required
def dashboard():
    return render_template("dashboard.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("dashboard"))
