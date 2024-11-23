from datetime import timedelta

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

"""Generate a secret key with
$ python -c 'import secrets; print(secrets.token_hex()) """
app.secret_key = "supersecretkey"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get("email")
        flash("Login successful", "info")
        print(email, "has logged in")
        return redirect(url_for("home"))


@app.route("/logout", methods=["GET"])
def logout():
    flash("Logout sucessful", "info")
    return redirect(url_for("home"))


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        flash("Account created successful", "info")
        email = request.form.get("email")
        print(email, "has signed up")
        return redirect(url_for("home"))


if __name__ == "__main__":
    """The default port is 5000, I use a different one
    when running another flask app"""
    app.run(debug=True)
