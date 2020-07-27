import flask
from app import db
from pymongo import MongoClient

class Shop(db.Document):
    title = db.StringField()
    description = db.StringField()
    discount  = db.StringField()
    welcome = db.StringField()
    history = db.StringField()
    why = db.StringField()
    reasons = db.ListField(db.ListField(db.StringField()))
    
    
