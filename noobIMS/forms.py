from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
    """Keep attributes consistent with the models"""

    firstname = StringField(
        "Firstname", validators=[DataRequired(), Length(min=2, max=50)]
    )
    lastname = StringField(
        "Lastname", validators=[DataRequired(), Length(min=2, max=50)]
    )
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = StringField(
        "Email address", validators=[DataRequired(), Length(max=100), Email()]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    """Keep attributes consistent with the models"""

    email = StringField("Email address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
