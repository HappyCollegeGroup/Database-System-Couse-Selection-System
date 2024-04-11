#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
from flask import Flask
import MySQLdb
import os

# flask 教學
# https://ithelp.ithome.com.tw/users/20114746/ironman/4037?page=2
# 老師範例
# https://github.com/hjhsu/105DBSys_ProjectExample/blob/master/python_example/python_example.py

def create_app():    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)


    from apps.home import views as home_views
    app.register_blueprint(home_views.home)

    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth)

    from apps.courses import views as courses_views
    app.register_blueprint(courses_views.courses)

    from apps.timetable import views as timetable_views
    app.register_blueprint(timetable_views.timetable)

    return app
