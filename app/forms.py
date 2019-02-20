from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired()])
    tlf = IntegerField('Tlf', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    @staticmethod
    def validate_tlf(tlf):
        if len(tlf) != 8 and tlf.isdigit() == False:
            raise ValidationError('Please use a correct tlfnr')

    @staticmethod
    def set_password(password):
        if SignUpForm.check_password(password) == False:
            raise ValidationError('The password must be at least 8 characters long, contain at least one uppercase letter and at '
                        'least one number.')

    @staticmethod
    def check_password(password):
        length = False
        uppercase = False
        digit = False

        if len(password) >= 8:
            length = True

        if any(l.isupper() for l in password):
            uppercase = True

        if any(l.isdigit() for l in password):
            digit = True

        if length and uppercase and digit:
            return True
        return False