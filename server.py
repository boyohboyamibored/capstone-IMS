from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return "<h1>Feature not yet available</h1>"


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return "<h1>Feature not yet available</h1>"


if __name__ == "__main__":
    """The default port is 5000, I use a different one
    when running another flask app"""
    app.run(debug=True)
