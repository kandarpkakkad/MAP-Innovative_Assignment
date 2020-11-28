from flask import Flask, render_template, request, redirect
import ast
import pymysql

modify_app = Flask(__name__)


@modify_app.route("/", methods=["GET"])
def take_get():
    global role, result, username, login, dat, cname, subject, lec_type
    role = request.cookies.get('role')
    if request.cookies.get('result') != "":
        result = request.cookies.get('result')
        result = ast.literal_eval(result)
        return render_template('modify.html', data={'role': role, 'result': result['name']})
    else:
        return redirect('http://localhost:9000/')
    # data = dict()
    # data["modify_api"] = True
    # data["method"] = "get"
    # data["port"] = 5000
    # data["returns"] = "dictionary"
    # return render_template("modify.html", data=data)


@modify_app.route("/", methods=["POST"])
def take_post():
    global role, result, username, login, dat, cname, subject, lec_type
    role = request.cookies.get('role')
    if request.cookies.get('result') != "":
        connection = pymysql.connect(host='localhost', user='root', password='', db='MAP')
        cursor = connection.cursor()
        if 'cname' in request.form:
            cname = request.form['cname']
            subject = request.form['subject']
            dat = request.form['date']
            query = "SELECT * FROM attendance;"
            cursor.execute(query)
            stu = cursor.fetchall()
            stun = []
            length = len(cname)
            if length == 4:
                lec_type = 0
                query = "SELECT * FROM attendance WHERE date='" + dat + "' AND lecture='" + subject + "' AND lecture_type=" + str(lec_type) + " AND status='A';"
                cursor.execute(query)
                stu = cursor.fetchall()
                # stu = att.objects.filter(date=dat, lecture=subject, lecture_type=lec_type, status='A')
                for i in stu:
                    stun.append(i[0])
            elif length == 5:
                lec_type = 1
                query = "SELECT * FROM attendance WHERE date='" + dat + "' AND lecture='" + subject + "' AND lecture_type=" + str(lec_type) + " AND status='A';"
                cursor.execute(query)
                stu = cursor.fetchall()
                # stu = att.objects.filter(date=dat, lecture=subject, lecture_type=lec_type, status='A')
                for i in stu:
                    stun.append(i[0])
            elif length == 6:
                lec_type = 2
                query = "SELECT * FROM attendance WHERE date='" + dat + "' AND lecture='" + subject + "' AND lecture_type=" + str(lec_type) + " AND status='A';"
                cursor.execute(query)
                stu = cursor.fetchall()
                # stu = att.objects.filter(date=dat, lecture=subject, lecture_type=lec_type, status='A')
                for i in stu:
                    stun.append(i[0])
            result = request.cookies.get('result')
            result = ast.literal_eval(result)
            return render_template('modify.html', data={'student': stu, 'role': role, 'result': result['name']})
        elif'submit_2' in request.form:
            arr = request.form.getlist('roll')
            for i in arr:
                query = "UPDATE attendance SET status='P' WHERE date='" + dat + "' AND lecture='" + subject + "' AND lecture_type=" + str(lec_type) + " AND status='A' AND roll_number='" + i + "';"
                cursor.execute(query)
                stu = cursor.fetchall()
                # attend = att.objects.get(date=dat, lecture=subject, lecture_type=lec_type, status='A', roll_number=i)
                # attend.status = 'P'
                # attend.save()
            return redirect('http://localhost:2222/dashboard/')
    else:
        return redirect('http://localhost:9000/')
    # data = dict()
    # data["modify_api"] = True
    # data["method"] = "post"
    # data["port"] = 5000
    # data["returns"] = "dictionary"
    # return render_template("modify.html", data=data)


if __name__ == "__main__":
    modify_app.run(debug=True, port=5000)
