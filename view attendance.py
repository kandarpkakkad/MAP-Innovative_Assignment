from flask import Flask, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class ViewAttendance(Resource):
    @staticmethod
    def get():
        return render_template("view_attendance.html")

    @staticmethod
    def post():
        return render_template("view_attendance.html")


api.add_resource(ViewAttendance, '/view_attendance')

if __name__ == "__main__":
    app.run(debug=True, port=3002)
