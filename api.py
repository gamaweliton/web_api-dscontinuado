from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from user_service import UserService

app = Flask(__name__)
api = Api(app)

class UserList(Resource):
    def get(self):
        user_service = UserService()
        users = user_service.get_users()
        return jsonify(users)

    def post(self):
        user_service = UserService()
        user_id = user_service.create_user(request.json)
        return jsonify(user_id)

class User(Resource):
    def get(self, user_id):
        user_service = UserService()
        user = user_service.get_user(user_id)
        if user:
            return jsonify(user)
        else:
            return '', 404

    def put(self, user_id):
        user_service = UserService()
        result = user_service.update_user(user_id, request.json)
        if result.modified_count > 0:
            return '', 204
        else:
            return '', 404

    def delete(self, user_id):
        user_service = UserService()
        result = user_service.delete_user(user_id)
        if result.deleted_count > 0:
            return '', 204
        else:
            return '', 404

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
