from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# set up flask api with api end point
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return 'hello worldd'


api.add_resource(HelloWorld, '/')

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/flask_demo"
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class CarModel(db.Model):
    __tablename__ = 'cars'  # tablename needs to be specified?

    # pk has to be manually added
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


# get records from db

class CarRouter(Resource):
    def get(self):
        cars = CarModel.query.all()
        print(cars)
        return cars


api.add_resource(CarRouter, '/cars')


# run app
if __name__ == '__main__':
    app.debug = True
    app.run()
