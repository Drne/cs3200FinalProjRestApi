from app import db, ma


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(45))
    amount = db.Column(db.Float)
    unit = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __init__(self, description, amount, unit, recipe_id):
        self.description = description
        self.amount = amount
        self.unit = unit
        self.recipe_id = recipe_id


class IngredientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'amount', 'unit', 'recipe_id')
