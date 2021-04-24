from app import db, ma
from models.userModel import User


class Chef(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    cuisine_specialty = db.Column(db.String)
    # recipes = db.relationship('Recipe', backref='chef', lazy=True)
    user = db.relationship(User, backref='chefs')

    def __init__(self, id, cuisine_specialty):
        self.id = id
        self.cuisine_specialty = cuisine_specialty

    def toJson(self):
        return self.id


class ChefSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cuisine_specialty', 'first_name', 'last_name', 'username', 'password', 'email')
