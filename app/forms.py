from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired()])
    tlf = IntegerField('Tlf', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')
