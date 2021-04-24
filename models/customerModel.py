from app import db, ma


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, id):
        self.id = id


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email')
