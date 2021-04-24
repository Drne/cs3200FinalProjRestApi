from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.chefModel import Chef, ChefSchema
from models.userModel import User

chef_schema = ChefSchema()
chefs_schema = ChefSchema(many=True)


class ChefDao(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        if not id:
            chefs = Chef.query.join(User, User.id == Chef.id).add_columns(
                Chef.cuisine_specialty,
                User.first_name, User.last_name, User.email, User.username, User.password, Chef.id).all()
            return jsonify(chefs_schema.dump(chefs))
        # chef = Chef.query.get(id)
        chef = Chef.query.filter_by(id=id).join(User, User.id == Chef.id).add_columns(
                Chef.cuisine_specialty,
                User.first_name, User.last_name, User.email, User.username, User.password, Chef.id).first()
        return jsonify(chef_schema.dump(chef))

    @staticmethod
    def post():
        id = request.json['id']
        cuisine_specialty = request.json['cuisineSpecialty']

        customer = Chef(id, cuisine_specialty)
        db.session.add(customer)
        db.session.commit()
        return jsonify({
            'Message': f'Chef inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        chef = Chef.query.get(id)

        id = request.json['id']
        cuisine_specialty = request.json['cuisineSpecialty']

        chef.id = id
        chef.cuisine_specialty = cuisine_specialty

        db.session.commit()

        return jsonify({
            'Message': f'User altered.'
        })

    @staticmethod
    def delete():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        customer = Chef.query.get(id)

        db.session.delete(customer)
        db.session.commit()

        return jsonify({
            'Message': f'User {str(id)} deleted.'
        })
