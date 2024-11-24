from flask import flash, redirect, render_template, url_for

from noobIMS import app

from .forms import LoginForm, SignupForm


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        """Getting the form inputs based on variable name"""
        email = form.email.data
        password = form.password.data

        flash("Login successful", "success")
        print(f"{email} has logged in")
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET"])
def logout():
    flash("Logged out sucessfully", "success")
    return redirect(url_for("home"))


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        """Getting them to make a user"""
        fName = form.firstname.data
        lName = form.lastname.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        flash(f"Account created for {email} successful", "success")
        print(f"{email} has signed up")
        return redirect(url_for("home"))
    return render_template("signup.html", form=form)
