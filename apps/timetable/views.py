from flask import Blueprint
from flask import render_template, request, flash, url_for, redirect

timetable = Blueprint(
    "timetable",
    __name__,
    template_folder="templates",
)

@timetable.route("/timetable/")
def my_timetable():
    # 顯示功課表
    # 可退選
    # 退選後，關注抽籤功能
    # 須符合老師要求
    return render_template("timetable.html")

