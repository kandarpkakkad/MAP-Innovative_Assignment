from flask import Flask, render_template, jsonify, json
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
api = Api(app=app)

class Modify(Resource):
    @staticmethod
    def get(self):
        data = []
        response = app.response_class(
            response=json.dumps(data),
            status=302,
            mimetype='application/json'
        )
        return response

    @staticmethod
    def post(self):
        data = []
        response = app.response_class(
            response=json.dumps(data),
            status=302,
            mimetype='application/json'
        )
        return response


api.add_resource(Modify, "/modify")

if __name__ == "__main__":
    app.run(debug=True, port=4000)
