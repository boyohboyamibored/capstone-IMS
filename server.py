from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get("email")
        print(email, "has logged in")
        return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form.get("email")
        print(email, "has signed up")
        return render_template("index.html")


if __name__ == "__main__":
    """The default port is 5000, I use a different one
    when running another flask app"""
    app.run(debug=True)
