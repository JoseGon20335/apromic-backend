from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes import user_routes
import firebase_admin
from firebase_admin import credentials, firestore, storage
from app.routes import user_routes, auth_routes
from app.routes import boletin_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar Firebase con el archivo de credenciales
    cred = credentials.Certificate('apromic-4b215-firebase-adminsdk-q48a2-048c75fccc.json')
    firebase_admin.initialize_app(cred)

    # Inicializar Firebase
    cred = credentials.Certificate('firebase_key.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

     # Inicializar Firebase con el archivo de credenciales
    cred = credentials.Certificate('apromic-4b215-firebase-adminsdk-q48a2-048c75fccc.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'apromic-4b215.appspot.com'  # Reemplaza con el nombre de tu bucket
    })

    # Inicializar Firestore
    db = firestore.client()
    
    # Inicializar Storage
    bucket = storage.bucket()

    # Hacer que la base de datos y el bucket estén disponibles en todo el proyecto
    app.db = db
    app.bucket = bucket

    # Registrar Blueprints
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(boletin_routes.bp)

    # Hacer que la base de datos esté disponible en todo el proyecto
    app.db = db

    return app