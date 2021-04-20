from app import db, ma


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instructions = db.Column(db.String(45))
    name = db.Column(db.String(45))
    author = db.Column(db.Integer, db.ForeignKey('chef.id'))
    cuisine = db.Column(db.String(45))

    def __init__(self, instructions, name, author, cuisine):
        self.instructions = instructions
        self.name = name
        self.author = author
        self.cuisine = cuisine


class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'instructions', 'name', 'author', 'cuisine')
