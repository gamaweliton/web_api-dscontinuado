from database import Database
from user import User

class UserService:
    def __init__(self):
        self.db = Database('mongodb://localhost:27017')

    def create_user(self, user_dict):
        user = User.from_dict(user_dict)
        user_id = str(self.db.insert_user(user.to_dict()).inserted_id)
        return {'id': user_id}

    def get_user(self, user_id):
        user_dict = self.db.get_user_by_id(user_id)
        if user_dict:
            return user_dict
        else:
            return None

    def get_users(self):
        users_dict = self.db.get_users()
        users = []
        for user_dict in users_dict:
            users.append(User.from_dict(user_dict))
        return [user.to_dict() for user in users]

    def update_user(self, user_id, user_dict):
        user = User.from_dict(user_dict)
        user_update = self.db.update_user(user_id, user)
        if user_update:
            return user_update
        else:
            return None
        
    def delete_user(self, user_id):
        user_delete = self.db.delete_user(user_id)
        if user_delete:
            return user_delete
        else:
            return None