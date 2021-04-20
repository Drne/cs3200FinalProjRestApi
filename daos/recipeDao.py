from flask import request, jsonify
from flask_restful import Resource

from app import db
from models.recipeModel import Recipe, RecipeSchema

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)


class RecipeDao(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        if not id:
            recipes = Recipe.query.all()
            return jsonify(recipes_schema.dump(recipes))
        recipe = Recipe.query.get(id)
        return jsonify(recipe_schema.dump(recipe))

    @staticmethod
    def post():
        name = request.args['name']
        instructions = request.args['instructions']
        author = request.args['author']
        cuisine = request.args['cuisine']

        recipe = Recipe(instructions, name, author, cuisine)
        db.session.add(recipe)
        db.session.commit()
        return jsonify({
            'Message': f'Recipe {name} inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        recipe = Recipe.query.get(id)

        name = request.args['name']
        instructions = request.args['instructions']
        author = request.args['author']
        cuisine = request.args['cuisine']

        recipe.name = name
        recipe.instructions = instructions
        recipe.author = author
        recipe.cuisine = cuisine

        db.session.commit()
        return jsonify({
            'Message': f'Recipe {name} altered.'
        })

    @staticmethod
    def delete():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        recipe = Recipe.query.get(id)

        db.session.delete(recipe)
        db.session.commit()

        return jsonify({
            'Message': f'Recipe {str(id)} deleted.'
        })
