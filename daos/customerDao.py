from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.customerModel import Customer, CustomerSchema

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
            users = Customer.query.all()
            return jsonify(users_schema.dump(users))
        user = Customer.query.get(id)
        return jsonify(user_schema.dump(user))

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
            id = request.args['id']
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
