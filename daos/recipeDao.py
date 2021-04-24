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

        try:
            chefId = request.args['chefId']
        except Exception as _:
            chefId = None

        if chefId:
            recipes = Recipe.query.filter_by(author=int(chefId)).all()
            return jsonify(recipes_schema.dump(recipes))

        if not id:
            recipes = Recipe.query.all()
            return jsonify(recipes_schema.dump(recipes))
        recipe = Recipe.query.get(id)
        return jsonify(recipe_schema.dump(recipe))

    @staticmethod
    def post():
        print(request.json)
        name = request.json['name']
        instructions = request.json['instructions']
        author = request.json['author']
        cuisine = request.json['cuisine']
        print(author)
        recipe = Recipe(instructions, name, author, cuisine)
        db.session.add(recipe)
        db.session.commit()
        return jsonify({
            'Message': f'Recipe {name} inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.json['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the recipe ID'})
        recipe = Recipe.query.get(id)

        name = request.json['name']
        instructions = request.json['instructions']
        author = request.json['author']
        cuisine = request.json['cuisine']

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
            id = request.json['id']
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
