from flask import Blueprint
from flask import render_template, request, flash, url_for, redirect, make_response,session
import pymysql

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
)

@auth.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        response = make_response(render_template("login.html"))    
    elif request.method == "POST":
        account = request.values.get("username", None)
        password = request.values.get("password", None)

        connect_db = pymysql.connect(host='localhost',user='hj', password='test1234', charset='utf8', db='testdb')
        with connect_db.cursor() as cursor:
            sql = "SELECT dept_name FROM student WHERE sid = %s"
            cursor.execute(sql, (account,))
            data = cursor.fetchone()
            dept_name = data[0]
            sql = "SELECT sname FROM student WHERE sid = %s"
            cursor.execute(sql, (account,))
            data = cursor.fetchone()
            sname = data[0]
            sql = "SELECT sgrade FROM student WHERE sid = %s"
            cursor.execute(sql, (account,))
            data = cursor.fetchone()
            sgrade = data[0]
            sql = "SELECT password FROM student WHERE sid = %s"
            cursor.execute(sql, (account,))
            data = cursor.fetchone()
            data = data[0]
        connect_db.close()

        if (password == data and password != None):
            auth_result = 'success'
        else:
            auth_result = 'fail'

        if auth_result == 'success':
            response = make_response(redirect(url_for('courses.list_courses')))
            session['username'] = account
            session['dept_name'] = dept_name
            session['sname'] = sname
            session['sgrade'] = sgrade
        else:
            response = make_response(redirect(url_for('auth.login')))
    else:
        response = make_response(redirect('index.html'))
        # 要檢查是否已經login，如果已經login，redirect到/courses/
        # 登入，將名字放到session['username']
    return response

@auth.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
