from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12Ozymandias!@localhost:3306/recipe_share'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Have to import dao modules after app, db instantiation
from daos.userDao import UserDao
from daos.customerDao import CustomerDao
from daos.chefDao import ChefDao
from daos.recipeDao import RecipeDao
from daos.ingredientDao import IngredientDao

api.add_resource(UserDao, '/api/users')
api.add_resource(CustomerDao, '/api/customers')
api.add_resource(ChefDao, '/api/chefs')
api.add_resource(RecipeDao, '/api/recipes')
api.add_resource(IngredientDao, '/api/ingredients')

if __name__ == '__main__':
    app.run(debug=True)
