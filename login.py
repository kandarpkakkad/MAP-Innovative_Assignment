from flask import Flask, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Login(Resource):
    @staticmethod
    def get():
        return render_template("login.html")

    @staticmethod
    def post():
        return render_template("login.html")


api.add_resource(Login, '/login')

if __name__ == "__main__":
    app.run(debug=True, port=3004)
