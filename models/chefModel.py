from app import db, ma


class Chef(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    cuisine_specialty = db.Column(db.String)
    recipes = db.relationship('Recipe', backref='chef', lazy=True)

    def __init__(self, id, cuisine_specialty):
        self.id = id
        self.cuisine_specialty = cuisine_specialty


class ChefSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cuisine_specialty')
