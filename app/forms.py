from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Brukernavn', validators=[DataRequired()])
    password = PasswordField('Passord', validators=[DataRequired()])
    remember_me = BooleanField('Husk meg')
    submit = SubmitField('Logg inn')

class SignUpForm(FlaskForm):
    first_name = StringField('Fornavn', validators=[DataRequired()])
    last_name = StringField('Etternavn', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    tlf = StringField('Telefon', validators=[DataRequired(),Length(max=8), Length(min=8)])
    username = StringField('Brukernavn', validators=[DataRequired()] )
    password = PasswordField('Passord', validators=[DataRequired()])
    password2 = PasswordField('Gjenta passord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrer deg')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Brukernavn er allerede tatt.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email er allerede brukt.')


    @staticmethod
    def set_password(password):
        if SignUpForm.check_password(password) == False:
            raise ValidationError('Passordet må ha 8 tegn, og inneholde minst en stor bokstav og et tall.')

# denne fungerer ikke tror jeg
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


class EditProfileForm(FlaskForm):
    username = StringField('Brukernavn', validators=[DataRequired()])
    submit = SubmitField('Send')