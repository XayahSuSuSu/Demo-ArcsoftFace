from flask import Blueprint

router = Blueprint('router', __name__)


@router.route("/")
def init():
    return "Server is running..."
