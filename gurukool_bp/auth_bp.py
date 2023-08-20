from datetime import timedelta

from flask import Flask, request, make_response, session,g
from flask import Blueprint
from mongo.mongo import get_user


auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=["POST"])
def login():
    if session.get("id"):
        session.pop("id", None)

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name:
        return make_response({"status": 400, "msg": "Invalid request, name not found in request body"}, 400)
    if not email:
        return make_response({"status": 400, "msg": "Invalid request, email not found in request body"}, 400)
    if not password:
        return make_response({"status": 400, "msg": "Invalid request, password not found in request body"}, 400)

    if email:
        existing_user = get_user(email)
        if existing_user:
            passw = existing_user.get("password")
            if passw == password:
                user_id = existing_user.get("_id")
                session["id"] = user_id
                print(session)
                user_name = existing_user.get("username")
                response = {"status": 200, "msg": "Logged in", "token": user_id,"user_name": user_name}
                return make_response(response, 200)
            else:
                return make_response({"status": 400, "msg": "Incorrect password"}, 400)
        else:
            return make_response({"status": 400, "msg": "account doesn't exists"}, 400)


@auth_bp.route('/logout', methods=["GET"])
def logout():
    print(session)
    id = session.get("id")
    session.pop("id", None)
    print(session)
    return make_response({"status": 200, "msg": "Logged out", "token": id}, 200)
