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
                roll_number = request.cookies.get('roll_number')
                print(roll_number)
                # result = ast.literal_eval(result)
                cursor.close()
                return render_template('take.html', data={'result': result, 'roll_number': roll_number, "subject": lecture, 'class': class_name, 'students': stun, 'role': request.cookies.get('role')})
            else:
                result = request.cookies.get('result')
                print(result)
                roll_number = request.cookies.get('roll_number')
                print(roll_number)
                cursor.close()
                return render_template('take.html', data={'class': class_name, 'subject': lecture, 'role': request.cookies.get('role'), 'result': result, 'roll_number': roll_number})
        else:
            return redirect("http://localhost:9000/", code=302)
    else:
        return redirect("http://localhost:9000/", code=302)


@take_app.route("/<lecture>/<class_name>/", methods=["POST"])
def take_post(lecture, class_name):
    global role, result, username, login
    if 'result' in request.cookies:
        if request.cookies.get('result') != "":
            connection = sql.connect(host='localhost', user='root', password='', db='MAP')
            cursor = connection.cursor()
            query = "SELECT * FROM student;"
            cursor.execute(query)
            stu = cursor.fetchall()
            stun = []
            print(lecture, class_name, type(lecture), type(class_name))
            if lecture != '-' and class_name != '-':
                length = len(class_name)
                if length == 4:
                    sem = class_name[0]
                    branch = class_name[1: length - 1]
                    batch = class_name[length - 1]
                    find_student_query = "SELECT * FROM student WHERE semester=" + str(sem) + " AND branch='" + branch + "' AND batch='" + batch + "';"
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 5:
                    sem = class_name[0]
                    branch = class_name[1:length - 2]
                    batch = class_name[length - 2:]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND lab_batch='" + batch + "';"
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
                prof_name = request.cookies.get('result')
                query_2 = "SELECT username FROM professor WHERE name='" + prof_name + "';"
                cursor.execute(query_2)
                prof_username = cursor.fetchone()
                prof_username = prof_username[0]
                if len(class_name) == 4:
                    lecture_type = 0
                elif len(class_name) == 5:
                    lecture_type = 1
                elif len(class_name) == 6:
                    lecture_type = 2
                else:
                    lecture_type = 3
                now = datetime.datetime.now()
                now = now.replace(hour=0, minute=0, second=0, microsecond=0)
                now.strftime('%Y-%m-%d %H:%M:%S')
                for i in stun:
                    print(i)
                    query = "INSERT INTO attendance (`date`, `lecture`, `prof_username`, `roll_number`, `lecture_type`, `status`) VALUES (%s, %s, %s, %s, %s, %s);"
                    roll_number = i
                    if i in arr:
                        status = 'P'
                    else:
                        status = 'A'
                    cursor.execute(query, (now, lecture, prof_username, roll_number, lecture_type, status))
                connection.commit()
                print(cursor.rowcount, " records inserted.")
                result = request.cookies.get('result')
                print(result)
                roll_number = request.cookies.get('roll_number')
                print(roll_number)
                cursor.close()
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
                    query = "SELECT * FROM student WHERE semester=" + str(sem) + " AND branch='" + branch + "' AND batch='" + batch + "';"
                    cursor.execute(query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 5:
                    sem = class_name[0]
                    branch = class_name[1:length - 2]
                    batch = class_name[length - 2:]
                    query = "SELECT * FROM student WHERE semester=" + str(sem) + " AND branch='" + branch + "' AND lab_batch='" + batch + "';"
                    cursor.execute(query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                elif length == 6:
                    sem = class_name[0]
                    branch = class_name[1:length - 3]
                    cl = class_name[length - 3]
                    batch = class_name[length - 2:]
                    query = "SELECT * FROM student WHERE semester=" + str(sem) + " AND branch='" + branch + "' AND batch='" + cl + "' AND tut_batch='" + batch + "';"
                    cursor.execute(query)
                    stu = cursor.fetchall()
                    for i in stu:
                        stun.append(i[0])
                # arr = request.form.getlist('roll')
                # print(arr)
                # for i in stun:
                #     now = datetime.datetime.now()
                #     now.strftime('%Y-%m-%d %H:%M:%S')
                #     query = "INSERT INTO attendance (`date`, `lecture`, `prof_username`, `roll_number`, `lecture_type`, `status`) VALUES (%s, %s, %s, %s, %s, %s);"
                #     prof_name = request.cookies.get('result')
                #     query_2 = "SELECT username FROM professor WHERE name='" + prof_name + "';"
                #     cursor.execute(query_2)
                #     prof_username = cursor.fetchone()
                #     prof_username = prof_username[0]
                #     roll_number = i
                #     if len(class_name) == 4:
                #         lecture_type = 0
                #     elif len(class_name) == 5:
                #         lecture_type = 1
                #     elif len(class_name) == 6:
                #         lecture_type = 2
                #     else:
                #         lecture_type = 3
                #     if i in arr:
                #         status = "P"
                #     else:
                #         status = "A"
                #     cursor.execute(query, (now, lecture, prof_username, roll_number, str(lecture_type), status))
                result = request.cookies.get('result')
                print(result)
                roll_number = request.cookies.get('roll_number')
                print(roll_number)
                students = [i[0] for i in stu]
                print(students)
                cursor.close()
                return render_template('take.html', data={'class': class_name, 'subject': lecture, 'role': request.cookies.get('role'), 'result': result, 'roll_number': roll_number, 'students': students})
                # return redirect('http://localhost:2222/dashboard/')
        else:
            return redirect('http://localhost:9000/')
    else:
        return redirect('http://localhost:9000/')


if __name__ == "__main__":
    take_app.run(debug=True, port=3000)
