from flask import Flask, render_template, request, redirect
import pymysql as sql
import os
import sys
import datetime
import ast

view_app = Flask(__name__)


@view_app.route("/", methods=["GET"])
def view_get():
    global role, result, username, login
    typ = 0
    rol = ''
    at = []
    sear_sub = ''
    role = request.cookies.get('role')
    if 'result' in request.cookies:
        result = request.cookies.get('result')
        result = ast.literal_eval(result)
        return render_template('home/view_attendance.html', data = {'role': role, 'result': result['name'], 'search_set': at})
    else:
        return redirect("http://localhost:9000/", code=302)


@view_app.route("/", methods=["POST"])
def take_post():
    global role, result, username, login
    typ = 0
    rol = ''
    at = []
    sear_sub = ''
    role = request.cookies.get('role')
    if 'result' in request.cookies:
        sear_sub = request.form.get('search_sub')
        lt = request.form.get('ltype')
        result = request.cookies.get('result')
        result = ast.literal_eval(result)
        rol = result['roll_number']
        if lt == 'lecture':
            typ = 0
        elif lt == 'lab':
            typ = 1
        else:
            typ = 2
        #at = att.objects.filter(lecture=sear_sub, lecture_type=typ, roll_number=rol)
        search_att = "SELECT * FROM attendance WHERE lecture='"+sear_sub+"' AND lecture_type='"+typ+"' AND roll_number='"+rol+"';"
        cursor.execute(search_att)
        stu = cursor.fetchall()
        result = request.cookies.get('result')
        result = ast.literal_eval(result)
        return render_template('home/view_attendance.html', data={'role': role, 'result': result['name'], 'search_set': stu})
    else:
        return redirect("http://localhost:9000/", code=302)


if __name__ == "__main__":
    view_app.run(debug=True, port=4000)
