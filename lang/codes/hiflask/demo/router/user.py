from flask import Blueprint


bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/test", methods=("GET",))
def test():
    return "hello world"
