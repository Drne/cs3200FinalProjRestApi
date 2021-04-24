from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.ingredientModel import Ingredient, IngredientSchema

ingredient_schema = IngredientSchema()
Ingredients_schema = IngredientSchema(many=True)


class IngredientDao(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        try:
            recipe_id = request.args['recipeId']
        except Exception as _:
            recipe_id = None

        if recipe_id:
            ingredients = Ingredient.query.filter_by(recipe_id=int(recipe_id)).all()
            return jsonify(Ingredients_schema.dump(ingredients))

        elif not id:
            ingredients = Ingredient.query.all()
            return jsonify(Ingredients_schema.dump(ingredients))
        ingredient = Ingredient.query.get(id)
        return jsonify(ingredient_schema.dump(ingredient))

    @staticmethod
    def post():
        description = request.json['description']
        amount = request.json['amount']
        unit = request.json['unit']
        recipe_id = request.json['recipeId']

        ingredient = Ingredient(description, amount, unit, recipe_id)
        db.session.add(ingredient)
        db.session.commit()
        return jsonify({
            'Message': f'Ingredient {description} inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        ingredient = Ingredient.query.get(id)

        description = request.json['description']
        amount = request.json['amount']
        unit = request.json['unit']
        recipe_id = request.json['recipeId']

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
            id = request.json['id']
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
