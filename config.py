import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    MONGODB_SETTINGS = { 'db' : 'bakery','host':'mongodb+srv://root:root@cluster0.bhknw.mongodb.net/bakery?retryWrites=true&w=majority'}