class UserService:
    def __init__(self, db):
        self.db = db

    def get_all_users(self):
        users_ref = self.db.collection('users')
        docs = users_ref.stream()
        users = [doc.to_dict() for doc in docs]
        return users

    def add_user(self, user_data):
        self.db.collection('users').add(user_data)
