from flask import Flask, render_template

modify_app = Flask(__name__)


@modify_app.route("/", methods=["GET"])
def take_get():
    data = dict()
    data["modify_api"] = True
    data["method"] = "get"
    data["port"] = 5000
    data["returns"] = "dictionary"
    return render_template("modify.html", data=data)


@modify_app.route("/", methods=["POST"])
def take_post():
    data = dict()
    data["modify_api"] = True
    data["method"] = "post"
    data["port"] = 5000
    data["returns"] = "dictionary"
    return render_template("modify.html", data=data)


if __name__ == "__main__":
    modify_app.run(debug=True, port=5000)
