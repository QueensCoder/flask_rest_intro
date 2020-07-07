import db from .demo_api


class UserModel(db.Model):
    __tablename__ = 'cars'  # tablename needs to be specified?

    # pk has to be manually added
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<User {self.name}>"
