from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine()
db.init_app(app)

from app import routes

