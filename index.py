from flask import Flask, render_template

index_app = Flask(__name__)


@index_app.route("/", methods=['GET'])
def index():
    return render_template("login.html")


if __name__ == "__main__":
    index_app.run(debug=True, port=9000)
