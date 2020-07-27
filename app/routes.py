from app import app,db
from flask import render_template, request, Response, redirect,url_for,json
from app.models import Shop

@app.route("/")
def index():
    shop = Shop.objects.all()
    return render_template('index.html',shop = shop)


