# app/services/about_service.py

class AboutService:
    @staticmethod
    def get_quienes_somos():
        # Contenido estático o puedes obtenerlo de una base de datos
        return "Somos una organización dedicada a..."

    @staticmethod
    def get_mision():
        return "Nuestra misión es..."

    @staticmethod
    def get_vision():
        return "Nuestra visión es..."
