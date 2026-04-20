from flask import request, jsonify, Blueprint
from .models import User
from .extensions import db, bcrypt
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json

    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    user = User(username=data["username"], password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201


@auth.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(username=data["username"]).first()

    if user and bcrypt.check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=str(user.id))  # ✅ FIX
        return jsonify(access_token=token)

    return jsonify({"msg": "Invalid credentials"}), 401