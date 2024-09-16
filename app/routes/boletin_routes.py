from flask import Blueprint, jsonify, request
from app.services.boletin_service import BoletinService

bp = Blueprint('boletin', __name__, url_prefix='/boletin')

@bp.route('/upload', methods=['POST'])
def upload_boletin():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    name_boletin = request.form.get('name_boletin')

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    boletin_service = BoletinService(app.db, app.bucket)
    boletin_service.upload_boletin(file, name_boletin)
    return jsonify({"message": "Boletin uploaded successfully"}), 201

@bp.route('/<boletin_id>', methods=['GET'])
def get_boletin(boletin_id):
    boletin_service = BoletinService(app.db, app.bucket)
    boletin = boletin_service.get_boletin(boletin_id)
    if boletin:
        return jsonify(boletin), 200
    else:
        return jsonify({"error": "Boletin not found"}), 404

@bp.route('/<boletin_id>', methods=['DELETE'])
def delete_boletin(boletin_id):
    boletin_service = BoletinService(app.db, app.bucket)
    boletin_service.delete_boletin(boletin_id)
    return jsonify({"message": "Boletin deleted successfully"}), 200
