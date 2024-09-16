# app/routes/anuncios_routes.py

from flask import Blueprint, jsonify
from app.services.anuncios_service import AnunciosService

bp = Blueprint('anuncios', __name__, url_prefix='/anuncios')

@bp.route('/', methods=['GET'])
def get_anuncios():
    anuncios = AnunciosService.get_anuncios()
    return jsonify(anuncios)
