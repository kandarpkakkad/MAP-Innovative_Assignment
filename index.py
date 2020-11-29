from flask import Flask, render_template, request, redirect, make_response


index_app = Flask(__name__)


@index_app.route("/", methods=['GET'])
def index():
    if 'result' in request.cookies:
        if request.cookies.get('result') != "":
            return redirect("http://localhost:2222/dashboard/")
    return render_template("login.html")


@index_app.route("/logout/", methods=["GET"])
def logout():
    resp = make_response(redirect("http://localhost:9000/", code=302))
    resp.delete_cookie("result")
    resp.delete_cookie("username")
    resp.delete_cookie("role")
    if 'dict' in request.cookies:
        resp.delete_cookie("dict")
    if 'tt' in request.cookies:
        resp.delete_cookie("tt")
    return resp


if __name__ == "__main__":
    index_app.run(debug=True, port=9000)
