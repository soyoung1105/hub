from flask import Flask
from flask_restful import Api
from .resource import Item

app = Flask(__name__)

api = Api(app)

api.add_resource(item)

api.add_resource(Item, '/item/<string:name')