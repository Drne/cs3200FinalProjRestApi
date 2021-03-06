from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.userModel import User, UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserDao(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        if not id:
            users = User.query.all()
            return jsonify(users_schema.dump(users))
        user = User.query.get(id)
        return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']

        user = User(username, password, first_name, last_name, email)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'Message': f'User {first_name} {last_name} inserted.',
            "id": user.id
        })

    @staticmethod
    def put():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        user = User.query.get(id)

        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']

        user.username = username
        user.password = password
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        db.session.commit()
        return jsonify({
            'Message': f'User {first_name} {last_name} altered.'
        })

    @staticmethod
    def delete():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'Message': f'User {str(id)} deleted.'
        })
