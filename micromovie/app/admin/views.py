# coding:utf8
from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:red'>This is the admin</h1>"