from flask import Flask, render_template

home_app = Flask(__name__)


@home_app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    home_app.run(debug=True, port=7000)
