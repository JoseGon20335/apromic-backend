# app/routes/about_routes.py

from flask import Blueprint, jsonify
from app.services.about_service import AboutService

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/quienes-somos', methods=['GET'])
def quienes_somos():
    content = AboutService.get_quienes_somos()
    return jsonify({"content": content})

@bp.route('/mision', methods=['GET'])
def mision():
    content = AboutService.get_mision()
    return jsonify({"content": content})

@bp.route('/vision', methods=['GET'])
def vision():
    content = AboutService.get_vision()
    return jsonify({"content": content})
