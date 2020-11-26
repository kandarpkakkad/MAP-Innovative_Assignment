from flask import Flask, render_template, request, make_response

home_app = Flask(__name__)


@home_app.route("/", methods=['GET'])
def home():
    print("Reached...")
    resp = make_response(render_template("dashboard.html"))
    resp.set_cookie("result", "Hello", max_age=50*50*50)
    return resp


if __name__ == "__main__":
    home_app.run(debug=True, port=7000)
