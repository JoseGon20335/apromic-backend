import firebase_admin
from firebase_admin import auth

class AuthService:
    @staticmethod
    def create_user(email, password):
        user = auth.create_user(
            email=email,
            password=password
        )
        return user.uid

    @staticmethod
    def sign_in_user(email, password):
        # En un sistema puro backend, usaremos Custom Tokens
        custom_token = auth.create_custom_token(email)
        return custom_token

    @staticmethod
    def delete_user(uid):
        auth.delete_user(uid)
