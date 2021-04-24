from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.customerModel import Customer, CustomerSchema
from models.userModel import User

user_schema = CustomerSchema()
users_schema = CustomerSchema(many=True)


class CustomerDao(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        if not id:
            customers = Customer.query.join(User, User.id == Customer.id).add_columns(
                User.first_name, User.last_name, User.email, User.username, User.password, Customer.id).all()
            return jsonify(users_schema.dump(customers))
        customer = Customer.query.filter_by(id=id).join(User, User.id == Customer.id).add_columns(
                User.first_name, User.last_name, User.email, User.username, User.password, Customer.id).first()
        return jsonify(user_schema.dump(customer))

    @staticmethod
    def post():
        id = request.json['id']

        customer = Customer(id)
        db.session.add(customer)
        db.session.commit()
        return jsonify({
            'Message': f'Customer inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        customer = Customer.query.get(id)

        id = request.json['id']

        customer.id = id

        db.session.commit()

        return jsonify({
            'Message': f'User altered.'
        })

    @staticmethod
    def delete():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        customer = Customer.query.get(id)

        db.session.delete(customer)
        db.session.commit()

        return jsonify({
            'Message': f'User {str(id)} deleted.'
        })
