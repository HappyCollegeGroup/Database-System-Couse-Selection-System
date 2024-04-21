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

    takes_count_query = f"""
    SELECT COUNT(*) AS take_count FROM takes WHERE course_id='{course_id}';
    """
    capicity_query = f"""
    SELECT capicity FROM course WHERE course_id='{course_id}';
    """
    get_random_followers_query = f"""
    SELECT follows.sid, dept_name FROM follows LEFT JOIN student ON student.sid=follows.sid WHERE course_id='{course_id}' ORDER BY RAND() LIMIT 1
    """
    while True:
        cursor.execute(takes_count_query)
        takes_count = cursor.fetchall()[0][0]
        cursor.execute(capicity_query)
        capicity = cursor.fetchall()[0][0]
        if takes_count >= capicity:
            break
        
        cursor.execute(get_random_followers_query)
        stu = cursor.fetchall()
        if len(stu) > 0:
            sid = stu[0][0]
            dept_name = stu[0][1]

            delete_followers = f"""
            DELETE FROM follows WHERE sid='{sid}' AND course_id='{course_id}'
            """
            cursor.execute(delete_followers)
            conn.commit()

            add_query = f"""
            SELECT 
                CASE
                    WHEN IFNULL(TakeCount, 0) >= Capicity
                    THEN '已滿'
                END AS Available,
                CASE
                    WHEN cname IN (SELECT cname FROM takes LEFT JOIN course USING (course_id) WHERE sid = '{sid}') 
                    THEN '已選同名課程'
                END AS Duplicate_Name,
                CASE
                    WHEN (
                        SELECT COUNT(*) FROM section 
                        WHERE course.course_id=section.course_id
                        AND time_id 
                        IN (SELECT time_id FROM takes LEFT JOIN section USING (course_id) WHERE sid='{sid}')
                    ) > 0
                    THEN '衝堂'
                END AS Duplicate_Time,
                CASE
                    WHEN (SELECT SUM(credit) FROM takes LEFT JOIN course USING (course_id) WHERE sid = '{sid}') + credit > 30
                    THEN '加選後，學分數超過30'
                END AS More_Credit,
                CASE
                    WHEN course.dept_name!='{dept_name}'
                    THEN '不同科系'
                END AS Different_Dept,
                CASE
                    WHEN course_id IN (SELECT course_id FROM follows WHERE sid = '{sid}')
                    THEN '已關注'
                END AS Follows,
                CASE
                    WHEN course_id IN (SELECT course_id FROM takes WHERE sid = '{sid}')
                    THEN '已選課'
                END AS Takes
            -- 加入已選人數
            FROM course
            LEFT JOIN (SELECT course_id, COUNT(*) AS TakeCount FROM Takes GROUP BY course_id) AS CourseTakeCount USING (course_id)
            WHERE course_id='{course_id}'
            """
            cursor.execute(add_query)
            print(cursor.fetchall())
            cursor.execute(add_query)
            result = cursor.fetchall()[0]
            if result[0]==None and result[1]==None and result[2]==None and result[3]==None and result[4]==None and result[5]==None and result[6]==None:
                select_query = f"""
                    INSERT INTO takes (sid, course_id) VALUES
                    ('{sid}', '{course_id}');
                """
                cursor.execute(select_query)
                conn.commit()
        else:
            break
    conn.close()

    return redirect("/timetable/?msg='成功退選'")
