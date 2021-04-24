from app import db, ma
from models.chefModel import Chef


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instructions = db.Column(db.String(45))
    name = db.Column(db.String(45))
    author = db.Column(db.Integer, db.ForeignKey('chef.id'))
    authorObj = db.relationship(Chef, backref='recipes')
    cuisine = db.Column(db.String(45))

    def __init__(self, instructions, name, author, cuisine):
        self.instructions = instructions
        self.name = name
        self.author = author
        self.cuisine = cuisine


class RecipeSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'instructions', 'name', 'author', 'authorObj.user.first_name', 'authorObj.user.last_name', 'cuisine')
