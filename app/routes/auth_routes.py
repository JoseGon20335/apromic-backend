from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        user_id = AuthService.create_user(email, password)
        return jsonify({"message": "User created", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        custom_token = AuthService.sign_in_user(email, password)
        return jsonify({"token": custom_token.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        AuthService.delete_user(user_id)
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
