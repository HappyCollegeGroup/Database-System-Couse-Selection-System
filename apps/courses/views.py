from flask import Blueprint, session, render_template, request, flash, url_for, redirect
import MySQLdb

courses = Blueprint(
    "courses",
    __name__,
    template_folder="templates",
)

@courses.route("/course/")
def list_courses():
    # 顯示可選課表
    # 顯示關注清單，取消關注
    # 選課，需滿足加選條件
    
    return render_template("course.html")
    pass

@courses.route('/course/select/', methods=['POST'])
def select_course():
    pass