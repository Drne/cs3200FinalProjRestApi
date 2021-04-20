from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.ingredientModel import Ingredient, IngredientSchema

user_schema = IngredientSchema()
users_schema = IngredientSchema(many=True)


class IngredientDao(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        try:
            recipe_id = request.args['recipe_id']
        except Exception as _:
            recipe_id = None

        if not id:
            ingredients = Ingredient.query.all()
            return jsonify(users_schema.dump(ingredients))

        elif recipe_id:
            ingredients = Ingredient.query.filter_by(recipe_id=int(recipe_id))
            return jsonify(users_schema.dump(ingredients))
        ingredient = Ingredient.query.get(id)
        return jsonify(user_schema.dump(ingredient))

    @staticmethod
    def post():
        description = request.args['description']
        amount = request.args['amount']
        unit = request.args['unit']
        recipe_id = request.args['recipeId']

        ingredient = Ingredient(description, amount, unit, recipe_id)
        db.session.add(ingredient)
        db.session.commit()
        return jsonify({
            'Message': f'Ingredient {description} inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        ingredient = Ingredient.query.get(id)

        description = request.args['description']
        amount = request.args['amount']
        unit = request.args['unit']
        recipe_id = request.args['recipeId']

        ingredient.description = description
        ingredient.amount = amount
        ingredient.unit = unit
        ingredient.recipe_id = recipe_id

        db.session.commit()
        return jsonify({
            'Message': f'Ingredient {description} altered.'
        })

    @staticmethod
    def delete():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        user = Ingredient.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'Message': f'Ingredient {str(id)} deleted.'
        })
