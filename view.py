from flask import Flask, render_template

view_app = Flask(__name__)


@view_app.route("/", methods=["GET"])
def take_get():
    data = dict()
    data["view_api"] = True
    data["method"] = "get"
    data["port"] = 4000
    data["returns"] = "dictionary"
    return render_template("view.html", data=data)


@view_app.route("/", methods=["POST"])
def take_post():
    data = dict()
    data["view_api"] = True
    data["method"] = "post"
    data["port"] = 4000
    data["returns"] = "dictionary"
    return render_template("view.html", data=data)


if __name__ == "__main__":
    view_app.run(debug=True, port=4000)
