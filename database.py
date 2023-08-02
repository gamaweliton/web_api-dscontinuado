from pymongo import MongoClient

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['users_db']
        self.users = self.db['users']

    def insert_user(self, user_data):
        return self.users.insert_one(user_data)

    def get_user_by_id(self, user_id):
        return self.users.find_one({'_id': user_id})

    def get_users(self):
        return self.users.find()

    def update_user(self, user_id, user_data):
        return self.users.update_one({'_id': user_id}, {'$set': user_data})

    def delete_user(self, user_id):
        return self.users.delete_one({'_id': user_id})
