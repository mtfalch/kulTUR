from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()] )
    mail = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
