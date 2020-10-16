from flask import Flask, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class ModifyAttendance(Resource):
    @staticmethod
    def get():
        return render_template("modify_attendance.html")

    @staticmethod
    def post():
        return render_template("modify_attendance.html")


api.add_resource(ModifyAttendance, '/modify_attendance')

if __name__ == "__main__":
    app.run(debug=True, port=3003)
