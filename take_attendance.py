from flask import Flask, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class TakeAttendance(Resource):
    @staticmethod
    def get():
        return render_template("take_attendance.html")

    @staticmethod
    def post():
        return render_template("take_attendance.html")


api.add_resource(TakeAttendance, '/take_attendance')

if __name__ == "__main__":
    app.run(debug=True, port=3001)
