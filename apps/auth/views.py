from flask import Blueprint
from flask import render_template, request, flash, url_for, redirect

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
)

@auth.route("/login/")
def login():
    # 要檢查是否已經login，如果已經login，redirect到/courses/
    # 登入，將名字放到session['username']
    return render_template("index.html")

@auth.route("/logout/")
def logout():
    # 登出
    return redirect("/login/")

