from flask import Flask, render_template

take_app = Flask(__name__)


@take_app.route("/<lecture>/<class_name>/", methods=["GET"])
def take_get(lecture, class_name):
    data = dict()
    data["take_api"] = True
    data["lecture"] = lecture
    data["class_name"] = class_name
    data["method"] = "get"
    data["port"] = 3000
    data["returns"] = "dictionary"
    return render_template("take.html", data=data)


@take_app.route("/<lecture>/<class_name>/", methods=["POST"])
def take_post(lecture, class_name):
    data = dict()
    data["take_api"] = True
    data["lecture"] = lecture
    data["class_name"] = class_name
    data["method"] = "post"
    data["port"] = 3000
    data["returns"] = "dictionary"
    return render_template("take.html", data=data)


if __name__ == "__main__":
    take_app.run(debug=True, port=3000)
