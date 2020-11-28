from flask import Flask, render_template, request, redirect


index_app = Flask(__name__)


@index_app.route("/", methods=['GET'])
def index():
    if 'result' in request.cookies:
        if request.cookies.get('result') != "":
            return redirect("http:localhost:2222/dashboard/")
    return render_template("login.html")


if __name__ == "__main__":
    index_app.run(debug=True, port=9000)
