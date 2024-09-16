# app/services/anuncios_service.py

class AnunciosService:
    @staticmethod
    def get_anuncios():
        # Contenido estático o puedes obtenerlo de una base de datos
        return [
            {"title": "Anuncio 1", "content": "Contenido del anuncio 1"},
            {"title": "Anuncio 2", "content": "Contenido del anuncio 2"}
        ]
