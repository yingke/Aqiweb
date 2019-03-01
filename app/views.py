from flask import Blueprint, render_template

from app import models
from app.ext import db
from app.models import city_hour

blue = Blueprint('main_blue',__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():

    return render_template('index.html')
@blue.route("/getcity/",methods=['GET', 'POST'])
def getcity():
    Cityhour = city_hour()
    xt = Cityhour.query.order_by(db.desc(city_hour.DataTime)).limit(13).all()
    for i in xt:
        print(i.CityName)
        print(i.DataTime)
    return "ssssss"

