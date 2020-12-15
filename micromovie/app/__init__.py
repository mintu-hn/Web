# coding:utf8
from flask import Flask

app_ = Flask(__name__)
app_.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app_.register_blueprint(home_blueprint)
app_.register_blueprint(admin_blueprint, url_prefix="/admin")
