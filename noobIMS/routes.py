from flask import flash, redirect, render_template, request, url_for

from noobIMS import app


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """Getting the form inputs based on name or maybe id"""
        email = request.form.get("email")
        password = request.form.get("password")
        flash("Login successful", "info")
        print(email, "has logged in")
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/logout", methods=["GET"])
def logout():
    flash("Logout sucessful", "info")
    return redirect(url_for("home"))


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """Getting them to make a user"""
        fName = request.form.get("fName")
        lName = request.form.get("lName")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        flash("Account created successful", "info")
        print(email, "has signed up")
        return redirect(url_for("home"))
    else:
        return render_template("signup.html")
