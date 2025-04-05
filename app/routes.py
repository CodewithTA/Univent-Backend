from flask import Blueprint

main = Blueprint('main', __name__)


@main.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}, 200

