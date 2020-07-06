from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data_base = {
    'id': 1,
    'name': 'test'
}


class HelloWorld(Resource):
    def get(self):
        print('got to hello world,<><><>>')
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
