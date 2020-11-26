from flask import Flask, render_template, request, redirect
import pymysql as sql
import os
import sys
import datetime

take_app = Flask(__name__)

role1 = ''
role = ''
result = []
username = ''
login = 0
timetable = {}
dat = ''
cname = ''
lec_type = 0
subject = ''
sub = list()
pern = list()
perl = list()
pert = list()
colorn = list()
colorl = list()
colort = list()
colora = list()
lec = list()
tut = list()
lab = list()
avg = list()
all = list()


@take_app.route("/<lecture>/<class_name>/", methods=["GET"])
def take_get(lecture, class_name):
    if 'result' in request.cookies:
        if request.cookies.get('result') != "":
            connection = sql.connect(host='localhost', user='root', password='', db='MAP')
            cursor = connection.cursor()
            query = "SELECT * FROM student;"
            cursor.execute(query)
            result = cursor.fetchall()
            # stu = Student.objects.all()
            stun = []
            if lecture != '-' and class_name != '-':
                length = len(class_name)
                if length == 4:
                    sem = class_name[0]
                    branch = class_name[1:length - 1]
                    batch = class_name[length - 1]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND lab_batch='" + batch + "';"
                    print(find_student_query)
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    # stu = Student.objects.filter(semester=sem, branch=branch, batch=batch)
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
                    # stu = Student.objects.filter(semester=sem, branch=branch, batch=batch)
                    for i in stu:
                        stun.append(i[0])
                elif length == 6:
                    sem = class_name[0]
                    branch = class_name[1:length - 3]
                    cl = class_name[length - 3]
                    batch = class_name[length - 2:]
                    find_student_query = "SELECT * FROM student WHERE semester=" + sem + " AND branch='" + branch + "' AND lab_batch='" + batch + "';"
                    print(find_student_query)
                    cursor.execute(find_student_query)
                    stu = cursor.fetchall()
                    # stu = Student.objects.filter(semester=sem, branch=branch, batch=batch)
                    for i in stu:
                        stun.append(i[0])
                result = request.cookies.get('result')
                print(result)
                # result = ast.literal_eval(result)
                return render_template('take.html', data=result)
            else:
                result = request.cookies.get('result')
                return render_template('home/take_attendance.html', data={'class': class_name, 'subject': lecture, 'role': request.cookies.get('role')})
        else:
            return redirect("http://localhost:9000/", code=302)
    else:
        return redirect("http://localhost:9000/", code=302)


@take_app.route("/<lecture>/<class_name>/", methods=["POST"])
def take_post(lecture, class_name):
    data = dict()
    data["take_api"] = True
    data["lecture"] = lecture
    data["class_name"] = class_name
    data["method"] = "post"
    data["port"] = 3000
    data["returns"] = "dictionary"
    return render_template("take.html", data=data)


if __name__ == "__main__":
    take_app.run(debug=True, port=3000)
