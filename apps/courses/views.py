from flask import Blueprint, session, render_template, request, flash, url_for, redirect
import MySQLdb

courses = Blueprint(
    "courses",
    __name__,
    template_folder="templates",
)

def str_rm_null(str):
    if str != None:
        return str + '。'
    return ''

@courses.route("/course/")
def list_courses():
    # 顯示可選課表
    # 顯示關注清單，取消關注
    # 選課，需滿足加選條件
    
    if 'sid' not in session:
        return redirect("/login/")
    
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")

    course_query = f"""
        SELECT course_id, cname, tname, compulsory, credit, GROUP_CONCAT(CONCAT(time_id, " ", loc_name) SEPARATOR '<br>') AS Time, IFNULL(TakeCount, 0), capicity, CONCAT(COALESCE(Duplicate_Time, ''), '<br>', COALESCE(Duplicate_Name, ''), '<br>', COALESCE(More_Credit, ''), '<br>', COALESCE(Follows, '')) AS reason 
        FROM
            (SELECT course_id, cname, tname, compulsory, credit, TakeCount, capicity,
                    CASE
                        WHEN (
                            SELECT COUNT(*) FROM section 
                            WHERE course.course_id=section.course_id
                            AND time_id 
                            IN (SELECT time_id FROM takes LEFT JOIN section USING (course_id) WHERE sid='{session['sid']}')
                        ) > 0
                        THEN '衝堂'
                    END AS Duplicate_Time,
                    CASE
                        WHEN cname IN (SELECT cname FROM takes LEFT JOIN course USING (course_id) WHERE sid = '{session['sid']}') 
                        THEN '已選同名課程'
                    END AS Duplicate_Name,
                    CASE
                        WHEN (SELECT SUM(credit) FROM takes LEFT JOIN course USING (course_id) WHERE sid = '{session['sid']}') + credit > 30
                        THEN '加選後，學分數超過30'
                    END AS More_Credit,
                    CASE
                        WHEN course_id IN (SELECT course_id FROM follows WHERE sid = '{session['sid']}')
                        THEN '已關注'
                    END AS Follows
                FROM Course
                -- 加入老師名稱
                LEFT JOIN Teacher USING (tid)
                -- 加入已選人數
                LEFT JOIN (SELECT course_id, COUNT(*) AS TakeCount FROM Takes GROUP BY course_id) AS CourseTakeCount USING (course_id)
                -- 檢查科系
                WHERE course.dept_name='{session['dept_name']}'
                -- 還沒選課
                AND course_id NOT IN (SELECT course_id FROM takes WHERE sid = '{session['sid']}')) AS Temp
        LEFT JOIN section USING (course_id)
        GROUP BY course_id
    """

    cursor = conn.cursor()
    cursor.execute(course_query)

    # print(cursor.fetchall())
    return render_template("course.html", 
                           course_list=cursor.fetchall())

@courses.route('/course/select/', methods=['POST'])
def select_course():
    if 'sid' not in session:
        return redirect("/login/")
    
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
    
    course_id = request.values.get("course_id", None)
    action = request.values.get("action", None)
    
    query = f"""
        SELECT 
            CASE
                WHEN IFNULL(TakeCount, 0) >= Capicity
                THEN '已滿'
            END AS Available,
            CASE
                WHEN cname IN (SELECT cname FROM takes LEFT JOIN course USING (course_id) WHERE sid = '{session['sid']}') 
                THEN '已選同名課程'
            END AS Duplicate_Name,
            CASE
                WHEN (
                    SELECT COUNT(*) FROM section 
                    WHERE course.course_id=section.course_id
                    AND time_id 
                    IN (SELECT time_id FROM takes LEFT JOIN section USING (course_id) WHERE sid='{session['sid']}')
                ) > 0
                THEN '衝堂'
            END AS Duplicate_Time,
            CASE
                WHEN (SELECT SUM(credit) FROM takes LEFT JOIN course USING (course_id) WHERE sid = '{session['sid']}') + credit > 30
                THEN '加選後，學分數超過30'
            END AS More_Credit,
            CASE
                WHEN course.dept_name!='{session['dept_name']}'
                THEN '不同科系'
            END AS Different_Dept,
            CASE
                WHEN course_id IN (SELECT course_id FROM follows WHERE sid = '{session['sid']}')
                THEN '已關注'
            END AS Follows,
            CASE
                WHEN course_id IN (SELECT course_id FROM takes WHERE sid = '{session['sid']}')
                THEN '已選課'
            END AS Takes
        -- 加入已選人數
        FROM course
        LEFT JOIN (SELECT course_id, COUNT(*) AS TakeCount FROM Takes GROUP BY course_id) AS CourseTakeCount USING (course_id)
        WHERE course_id='{course_id}'
    """
    # print(query)

    cursor = conn.cursor()
    cursor.execute(query)

    result = cursor.fetchall()[0]

    if action == '加選' and result[0]==None and result[1]==None and result[2]==None and result[3]==None and result[4]==None and result[5]==None and result[6]==None:
        select_query = f"""
            INSERT INTO takes (sid, course_id) VALUES
            ('{session['sid']}', '{course_id}');
        """
        cursor.execute(select_query)
        conn.commit()

        return redirect("/course/?msg='成功加選'")
    elif action == '加選' and result[6]!=None:
        return redirect("/course/?msg='不能加選已選課程'")
    elif action == '加選':
        return redirect(f"/course/?msg='{str_rm_null(result[0])}{str_rm_null(result[1])}{str_rm_null(result[2])}{str_rm_null(result[3])}{str_rm_null(result[4])}'")
    elif action == '關注' and result[0]!=None and result[1]==None and result[2]==None and result[3]==None and result[4]==None and result[5]==None and result[6]==None:
        select_query = f"""
            INSERT INTO follows (sid, course_id) VALUES
            ('{session['sid']}', '{course_id}');
        """
        cursor.execute(select_query)
        conn.commit()

        return redirect("/course/?msg='成功關注'")
    elif action == '關注' and result[6]!=None:
        return redirect("/course/?msg='不能關注已選課程'")
    elif action == '關注' and result[0]==None:
        return redirect("/course/?msg='不能關注未滿課程'")
    elif action == '關注':
        return redirect(f"/course/?msg='{str_rm_null(result[1])}{str_rm_null(result[2])}{str_rm_null(result[3])}{str_rm_null(result[4])}{str_rm_null(result[5])}'")
    elif action == '取消關注':
        select_query = f"""
            DELETE FROM follows WHERE sid='{session['sid']}' AND course_id='{course_id}';
        """
        cursor.execute(select_query)
        conn.commit()

        return redirect("/course/?msg='成功取消關注'")
    else:
        return redirect("/course/")
