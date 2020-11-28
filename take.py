from flask import Flask, render_template, request, redirect
import pymysql as sql
import os
import sys
import datetime
import ast


take_app = Flask(__name__)


@take_app.route("/<lecture>/<class_name>/", methods=["GET"])
def take_get(lecture, class_name):
    if 'result' in request.cookies:
        if request.cookies.get('result') != "":
            connection = sql.connect(host='localhost', user='root', password='', db='MAP')
            cursor = connection.cursor()
            query = "SELECT * FROM student;"
            cursor.execute(query)
            stu = cursor.fetchall()
            stun = []
            if lecture != '-' and class_name != '-':
                length = len(class_name)
                if length == 4:
                    sem = class_name[0]
                    branch = class_name[1:length - 1]
                    batch = class_name[length - 1]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND batch='" + batch + "';"
                    print(find_student_query)
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 5:
                    sem = class_name[0]
                    branch = class_name[1:length - 2]
                    batch = class_name[length - 2:]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND lab_batch='" + batch + "';"
                    print(find_student_query)
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 6:
                    sem = class_name[0]
                    branch = class_name[1:length - 3]
                    cl = class_name[length - 3]
                    batch = class_name[length - 2:]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND batch='" + cl + "' AND tut_batch='" + batch + "';"
                    print(find_student_query)
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                result = request.cookies.get('result')
                print(result)
                result = ast.literal_eval(result)
                return render_template('take.html', data=result)
            else:
                result = request.cookies.get('result')
                result = ast.literal_eval(result)
                print(result)
                return render_template('home/take_attendance.html', data={'class': class_name, 'subject': lecture, 'role': request.cookies.get('role')})
        else:
            return redirect("http://localhost:9000/", code=302)
    else:
        return redirect("http://localhost:9000/", code=302)


@take_app.route("/<lecture>/<class_name>/", methods=["POST"])
def take_post(lecture, class_name):
    global role, result, username, login
    if result in request.cookies:
        if request.cookies.get('result') != "":
            connection = sql.connect(host='localhost', user='root', password='', db='MAP')
            cursor = connection.cursor()
            query = "SELECT * FROM student;"
            cursor.execute(query)
            stu = cursor.fetchall()
            stun = []
            if lecture != '-' and class_name != '-':
                length = len(class_name)
                if length == 4:
                    sem = class_name[0]
                    branch = class_name[1:length - 1]
                    batch = class_name[length - 1]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + "AND branch-'" + branch + "' AND batch='" + batch + "';"
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 5:
                    sem = class_name[0]
                    branch = class_name[1:length - 2]
                    batch = class_name[length - 2:]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + "AND branch-'" + branch + "' AND lab_batch='" + batch + "';"
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 6:
                    sem = class_name[0]
                    branch = class_name[1:length - 3]
                    cl = class_name[length - 3]
                    batch = class_name[length - 2:]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND batch='" + cl + "' AND tut_batch='" + batch + "';"
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                # arr = smart_attendance()
                arr = request.form.getlist('roll')
                print(arr)
                for i in stun:
                    query = "INSERT INTO student (`lecture`, `prof_username`, `roll_number`, `lecture_type`, `status`) VALUES ('%s', '%s', '%s', %s, '%s');"
                    prof_username = ast.literal_eval(request.cookies.get('result'))['name']
                    roll_number = i
                    if len(class_name) == 4:
                        lecture_type = 0
                    elif len(class_name) == 5:
                        lecture_type = 1
                    elif len(class_name) == 6:
                        lecture_type = 2
                    else:
                        lecture_type = 3
                    if i in arr:
                        status = 'P'
                    else:
                        status = 'A'
                    cursor.execute(query, (lecture, prof_username, roll_number, lecture_type, status))
                return redirect('http://localhost:2222/dashboard/')
            else:
                query = "SELECT * FROM student;"
                cursor.execute(query)
                stu = cursor.fetchall()
                # stu = Student.objects.all()
                stun = []
                length = len(request.form['class'])
                class_name = request.form['class']
                print(length)
                lecture = request.form['subject']
                print(lecture)
                if length == 4:
                    sem = class_name[0]
                    branch = class_name[1:length - 1]
                    batch = class_name[length - 1]
                    query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND batch='" + batch + "'" + "';"
                    cursor.execute(query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 5:
                    sem = class_name[0]
                    branch = class_name[1:length - 2]
                    batch = class_name[length - 2:]
                    query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND lab_batch='" + batch + "'" + "';"
                    cursor.execute(query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 6:
                    sem = class_name[0]
                    branch = class_name[1:length - 3]
                    cl = class_name[length - 3]
                    batch = class_name[length - 2:]
                    query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND batch='" + cl + "' AND tut_batch='" + batch + "'" + "';"
                    cursor.execute(query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                arr = request.form.getlist('roll')
                print(arr)
                for i in stun:
                    query = "INSERT INTO student (`lecture`, `prof_username`, `roll_number`, `lecture_type`, `status`) VALUES ('%s', '%s', '%s', %s, '%s');"
                    prof_username = ast.literal_eval(request.cookies.get('result'))['name']
                    roll_number = i
                    if len(class_name) == 4:
                        lecture_type = 0
                    elif len(class_name) == 5:
                        lecture_type = 1
                    elif len(class_name) == 6:
                        lecture_type = 2
                    else:
                        lecture_type = 3
                    if i in arr:
                        status = 'P'
                    else:
                        status = 'A'
                    cursor.execute(query, (lecture, prof_username, roll_number, lecture_type, status))
                return redirect('http://localhost:2222/dashboard/')
        else:
            return redirect('http://localhost:9000/')
    else:
        return redirect('http://localhost:9000/')


if __name__ == "__main__":
    take_app.run(debug=True, port=3000)
