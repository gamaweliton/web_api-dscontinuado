class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }

    @staticmethod
    def from_dict(user_dict):
        return User(user_dict['name'], user_dict['email'])
