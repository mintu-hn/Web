# coding:utf8
from . import home


@home.route("/")
def index():
    return "<h1 style='color:green'>This is the home</h1>"