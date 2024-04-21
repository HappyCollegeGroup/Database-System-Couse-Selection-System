from flask import Blueprint, session, render_template, redirect, request, flash
import MySQLdb

timetable = Blueprint(
    "timetable",
    __name__,
    template_folder="templates",
)

@timetable.route("/timetable/")
def my_timetable():
    if 'sid' not in session:
        return redirect("/login/")
    
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
    
    query_courses = f"""
    SELECT
        section.time_id AS 時間,
        course.course_id AS 課程代號,
        course.cname AS 課程名稱,
        teacher.tname AS 老師姓名,
        section.loc_name AS 課程地點,
        course.compulsory AS 必選修,
        course.credit AS 學分
    FROM
        takes
    LEFT JOIN
        section ON takes.course_id = section.course_id
    LEFT JOIN
        course ON takes.course_id = course.course_id
    LEFT JOIN
        teacher ON course.tid = teacher.tid
    WHERE
        takes.sid = '{session['sid']}'
    """

    cursor = conn.cursor()
    cursor.execute(query_courses)
    courses_result = cursor.fetchall()

    total_query = f"""
    SELECT IFNULL(SUM(course.credit) , 0)
    FROM takes 
    LEFT JOIN course ON takes.course_id = course.course_id 
    WHERE sid = '{session['sid']}'
    """
    cursor.execute(total_query)
    total_credit = cursor.fetchone()[0]

    return render_template("timetable.html", table=courses_result, total_credit=total_credit)

@timetable.route("/timetable/withdraw/<course_id>", methods=["POST"])
def withdraw_course(course_id):
    if 'sid' not in session:
        return redirect("/login/")

    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")

    credit_query = f"""
    SELECT IFNULL(SUM(course.credit) , 0)
    FROM takes 
    LEFT JOIN course ON takes.course_id = course.course_id 
    WHERE sid = '{session['sid']}' AND takes.course_id != '{course_id}'
    """
    cursor = conn.cursor()
    cursor.execute(credit_query)
    total_credit = cursor.fetchone()[0]

    if total_credit < 9:
        return redirect("/timetable/?msg='學分總數<9，退選失敗'")
    
    delete_query = f"""
    DELETE FROM takes
    WHERE sid = '{session['sid']}' AND course_id = '{course_id}'
    """

    cursor.execute(delete_query)
    conn.commit()
    conn.close()

    return redirect("/timetable/?msg='成功退選'")
