from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from noobIMS import app, bcrypt
from noobIMS.models.users import User

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
        remember_me = form.remember.data

        found_user = User.query.filter_by(email=email).first()
        if found_user and bcrypt.check_password_hash(found_user.password, password):
            login_user(found_user)
            if remember_me:
                login_user(found_user, remember=True)
            flash("Login successful", "success")
            print(f"{current_user.email} has logged in")
            return redirect(url_for("home"))
        else:
            flash("Invalid email address or password, please try again.", "error")
            return redirect(url_for("login"))
    else:
        if current_user.is_authenticated:
            flash("You are already logged in.", "info")
            return redirect(url_for("home"))
        return render_template("login.html", form=form, title="Login")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Logged out sucessfully", "success")
    print(current_user, "has logged out.")
    return redirect(url_for("home"))


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        from noobIMS import db

        """Getting them to make a user"""
        fName = form.firstname.data
        lName = form.lastname.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        hashed_passwd = bcrypt.generate_password_hash(password)

        email_taken = User.query.filter_by(email=email).first()
        username_taken = User.query.filter_by(username=username).first()

        if email_taken:
            flash(
                "Account with that email address already exists,\
please try another one.",
                "error",
            )
        elif username_taken:
            flash("Username already taken, please try another one.", "error")
        else:
            newUser = User(
                firstname=fName,
                lastname=lName,
                email=email,
                username=username,
                password=hashed_passwd,
            )

            db.session.add(newUser)
            db.session.commit()

            login_user(newUser)
            flash(f"Account created for {email} successful", "success")
            print(f"{email} has signed up")
            return redirect(url_for("home"))
    return render_template("signup.html", form=form, title="Sign up")
