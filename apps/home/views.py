from flask import Blueprint
from flask import render_template, request, flash, url_for, redirect

home = Blueprint(
    "home",
    __name__,
    template_folder="templates",
)

@home.route("/")
def index():
    return redirect("/login/")
