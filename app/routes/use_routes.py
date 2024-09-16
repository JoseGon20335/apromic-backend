from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/', methods=['GET'])
def get_users():
    user_service = UserService(app.db)
    users = user_service.get_all_users()
    return jsonify(users)

@bp.route('/', methods=['POST'])
def add_user():
    user_data = request.get_json()
    user_service = UserService(app.db)
    user_service.add_user(user_data)
    return jsonify({"message": "User added successfully"}), 201
