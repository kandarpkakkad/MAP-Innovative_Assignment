from flask import Flask, render_template, request, make_response, redirect
import pymysql
import ast


home_app = Flask(__name__)


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


connection = pymysql.connect(host='localhost', user='root', password='', db='MAP')
cursor = connection.cursor()


def index(array, key):
    if key in array:
        return array.index(key)
    return -1


def calculate_attendance(username):
    global role, cursor
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
    query = "SELECT * FROM student WHERE username='" + username + "';"
    cursor.execute(query)
    result = cursor.fetchall()
    # result = Student.objects.filter(username=username)
    branch = ''
    semester = ''
    roll = ''
    if len(result):
        for i in result:
            branch = i[2]
            semester = i[3]
            roll = i[0]
        query = "SELECT * FROM studentsubject WHERE branch='" + branch + "' AND semester=" + semester + ";"
        cursor.execute(query)
        ss = cursor.fetchall()
        # ss = StudentSubject.objects.filter(branch=branch, semester=semester)
        for i in ss:
            s = ''
            if i[3] == '0':
                s = i[2] + '-N'
            elif i[3] == '1':
                s = i[2] + '-L'
            elif i[3] == '2':
                s = i[2] + '-T'
            sub.append(s)
        sub.sort()
        for i in sub:
            # d1 = att()
            # d2 = att()
            if i[len(i) - 1] == 'N':
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i[:2] + "' AND lecture_type='" + str(0) + "' AND status='P';"
                cursor.execute(query)
                d1 = cursor.fetchall()
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i[:2] + "' AND lecture_type='" + str(0) + "';"
                cursor.execute(query)
                d2 = cursor.fetchall()
                # d1 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='0', status='P')
                # d2 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='0')
                if len(d2) == 0:
                    pern.append(0)
                    colorn.append('red')
                    lec.append(i[:-2])
                else:
                    pern.append(len(d1) / len(d2) * 100)
                    if len(d1) / len(d2) * 100 < 65:
                        colorn.append('red')
                    elif len(d1) / len(d2) * 100 < 75:
                        colorn.append('orange')
                    if len(d1) / len(d2) * 100 < 85:
                        colorn.append('yellow')
                    else:
                        colorn.append('green')
                    lec.append(i[:-2])
            elif i[len(i) - 1] == 'L':
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i[:2] + "' AND lecture_type='" + str(1) + "' AND status='P';"
                cursor.execute(query)
                d1 = cursor.fetchall()
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i[:2] + "' AND lecture_type='" + str(1) + "';"
                cursor.execute(query)
                d2 = cursor.fetchall()
                # d1 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='1', status='P')
                # d2 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='1')
                if len(d2) == 0:
                    perl.append(0)
                    colorl.append('red')
                    lab.append(i[:-2])
                else:
                    perl.append(len(d1) / len(d2) * 100)
                    if len(d1) / len(d2) * 100 < 65:
                        colorl.append('red')
                    elif len(d1) / len(d2) * 100 < 75:
                        colorl.append('orange')
                    if len(d1) / len(d2) * 100 < 85:
                        colorl.append('yellow')
                    else:
                        colorl.append('green')
                    lab.append(i[:-2])
            elif i[len(i) - 1] == 'T':
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i[:2] + "' AND lecture_type='" + str(2) + "' AND status='P';"
                cursor.execute(query)
                d1 = cursor.fetchall()
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i[:2] + "' AND lecture_type='" + str(2) + "';"
                cursor.execute(query)
                d2 = cursor.fetchall()
                # d1 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='2', status='P')
                # d2 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='2')
                if len(d2) == 0:
                    pert.append(0)
                    colort.append('red')
                    tut.append(i[:-2])
                else:
                    pert.append(len(d1) / len(d2) * 100)
                    if len(d1) / len(d2) * 100 < 65:
                        colort.append('red')
                    elif len(d1) / len(d2) * 100 < 75:
                        colort.append('orange')
                    if len(d1) / len(d2) * 100 < 85:
                        colort.append('yellow')
                    else:
                        colort.append('green')
                    tut.append(i[:-2])
            if i[:-2] not in all:
                all.append(i[:-2])
        for i in all:
            cnt = 0
            per = 0
            n = i + '-N'
            l = i + '-L'
            t = i + '-T'
            if n in sub:
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i + "' AND lecture_type='" + str(0) + "' AND status='P';"
                cursor.execute(query)
                d1 = cursor.fetchall()
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i + "' AND lecture_type='" + str(0) + "';"
                cursor.execute(query)
                d2 = cursor.fetchall()
                # d1 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='0', status='P')
                # d2 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='0')
                if len(d2) == 0:
                    per += 0
                    cnt += 1
                else:
                    per += len(d1) / len(d2) * 100
                    cnt += 1
            if l in sub:
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i + "' AND lecture_type='" + str(1) + "' AND status='P';"
                cursor.execute(query)
                d1 = cursor.fetchall()
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i + "' AND lecture_type='" + str(1) + "';"
                cursor.execute(query)
                d2 = cursor.fetchall()
                # d1 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='1', status='P')
                # d2 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='1')
                if len(d2) == 0:
                    per += 0
                    cnt += 1
                else:
                    per += len(d1) / len(d2) * 100
                    cnt += 1
            if t in sub:
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i + "' AND lecture_type='" + str(2) + "' AND status='P';"
                cursor.execute(query)
                d1 = cursor.fetchall()
                query = "SELECT * FROM attendance WHERE roll_number='" + roll + "' AND lecture='" + i + "' AND lecture_type='" + str(2) + "';"
                cursor.execute(query)
                d2 = cursor.fetchall()
                # d1 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='2', status='P')
                # d2 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='2')
                if len(d2) == 0:
                    per += 0
                    cnt += 1
                else:
                    per += len(d1) / len(d2) * 100
                    cnt += 1
            per = per / cnt
            avg.append(per)
            if per < 65:
                colora.append('red')
            elif per < 75:
                colora.append('orange')
            elif per < 85:
                colora.append('yellow')
            else:
                colora.append('green')
        dict = {
            'subsa': all,
            'subsn': lec,
            'subsl': lab,
            'subst': tut,
            'percentagea': avg,
            'percentagen': pern,
            'percentagel': perl,
            'percentaget': pert,
            'clra': colora,
            'clrn': colorn,
            'clrl': colorl,
            'clrt': colort,
        }
        return dict


def colspan(s, e):
    start = {'09:00:00': 0, '09:50:00': 1, '11:15:00': 2, '12:15:00': 3, '14:00:00': 4, '15:00:00': 5, '16:15:00': 6, '17:15:00': 7}
    end = {'09:50:00': 0, '10:50:00': 1, '12:15:00': 2, '13:15:00': 3, '15:00:00': 4, '16:00:00': 5, '17:15:00': 6, '18:05:00': 7}
    st = start[str(s)]
    ed = end[str(e)]
    return ed - st + 1


@home_app.route("/", methods=['GET'])
def home():
    global role, result, username, login, timetable, sub, pern, colorn, perl, pert, avg, colora, colorl, colorn, colort, lec, tut, lab, all, cursor
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
    role = 'professor'
    if role == 'professor':
        username = request.form['username']
        password = request.form['password']
        query = "SELECT * FROM professor WHERE username='" + username + "' AND professor='" + password + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        # result = Professor.objects.filter(username=username, password=password)
        timetable = {
            'name': ['', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'],
            'time': ['9:00 - 9:50', '9:50 - 10:50', '11:15 - 12:15', '12:15 - 1:15', '2:00 - 3:00', '3:00 - 4:00',
                     '4:15 - 5:15', '5:15 - 6:05'],
            'start_time': [[] for i in range(6)],
            'end_time': [[] for i in range(6)],
            'cols': [[] for i in range(6)],
            'subject': [[] for i in range(6)],
            'classes': [[] for i in range(6)],
        }
        days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5}
        if len(result):
            query = "SELECT * FROM professortimetable WHERE prof_username='" + username + "';"
            cursor.execute(query)
            prof_tt = cursor.fetchall()
            # prof_tt = ptt.objects.filter(prof_username=username)
            for i in prof_tt:
                timetable['start_time'][days[i[1]]].append(str(i[5]))
                timetable['end_time'][days[i[1]]].append(str(i[4]))
                timetable['cols'][days[i[1]]].append(colspan(i[5], i[5]))
                timetable['subject'][days[i[1]]].append(str(i[3]))
                timetable['classes'][days[i[1]]].append(str(i[2]))
            x = ""
            for r in result:
                x = str(r[0])
            res = {'name': x}
            response = make_response(render_template('dashboard.html', data={'tt': timetable, 'result': x, 'role': role}))
            response.set_cookie('username', username, max_age=86400*2)
            response.set_cookie('result', res, max_age=86400*2)
            response.set_cookie('role', role, max_age=86400*2)
            response.set_cookie('tt', timetable, max_age=86400 * 2)
            return response
        else:
            return redirect('http://localhost:9000/')
    elif role == 'student':
        username = request.form['username']
        password = request.form['password']
        query = "SELECT * FROM student WHERE username='" + username + "' AND professor='" + password + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        # result = Student.objects.filter(username=username, password=password)
        if len(result):
            dict = calculate_attendance(username)
            x = ""
            y = ""
            for r in result:
                x = r[1]
                y = r[0]
            res = {'name': x, 'roll_number': y}
            response = make_response(render_template('dashboard.html', data={'percentagea': avg, 'subsa':all, 'subst': tut, 'subsl':lab , 'subsn': lec, 'percentagen': pern, 'percentagel': perl, 'percentaget': pert, 'result': x, 'role': role, 'clrn': colorn, 'clrl': colorl,'clrt': colort,'clra': colora}))
            response.set_cookie('username', username, max_age=86400 * 2)
            response.set_cookie('result', res, max_age=86400 * 2)
            response.set_cookie('role', role, max_age=86400 * 2)
            response.set_cookie('dict', dict, max_age=86400 * 2)
            return response
        else:
            return redirect('http://localhost:9000/')
    else:
        return redirect('http://localhost:9000/')


if __name__ == "__main__":
    home_app.run(debug=True, port=7000)
