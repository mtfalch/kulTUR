from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Brukernavn', validators=[DataRequired()])
    password = PasswordField('Passord', validators=[DataRequired()])
    remember_me = BooleanField('Husk meg')
    submit = SubmitField('Logg inn')

class SignUpForm(FlaskForm):

    def validate_tlf(form, field):
        tlf = User.query.filter_by(tlf=field.data).first()
        if tlf is not None:
            flash('Telefonnummer er allerede registrert')
            raise ValidationError('Telefonnummer er allerede registrert')

    def validate_username(form, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            flash('Brukernavn er allerede tatt')
            raise ValidationError('Brukernavn er allerede tatt.')

    def validate_email(form, field):
        email = User.query.filter_by(email=field.data).first()
        if email is not None:
            flash('Email er allerede brukt')
            raise ValidationError('Email er allerede brukt.')

    def validate_password(form, field):
        if form.check_password(field.data):
            flash('Passordet må ha 8 tegn, og inneholde minst en stor bokstav og et tall')
            raise ValidationError('Passordet må ha 8 tegn, og inneholde minst en stor bokstav og et tall.')

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
            return False
        return True

    first_name = StringField('Fornavn', validators=[DataRequired()])
    last_name = StringField('Etternavn', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Insert an real email")])
    tlf = StringField('Telefon', validators=[DataRequired(), Length(max=8), Length(min=8)])
    username = StringField('Brukernavn', validators=[DataRequired()])
    password = PasswordField('Passord', validators=[DataRequired()])
    password2 = PasswordField('Gjenta passord', validators=[DataRequired(), EqualTo('password', message="Passord må være like")])
    sex = SelectField('Kjønn', validators=[DataRequired()], choices=[('male', 'Mann'), ('female', 'Kvinne'), ('other', 'Annet')])
    submit = SubmitField('Registrer deg')

class EditProfileForm(FlaskForm):

    def validate_username(form, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            flash('Brukernavn er allerede tatt')
            raise ValidationError('Brukernavn er allerede tatt.')

    username = StringField('Brukernavn', validators=[DataRequired()])
    submit = SubmitField('Send')

class EditTlfForm(FlaskForm):
    tlf = StringField('Telefon', validators=[DataRequired(), Length(max=8), Length(min=8)])
    submit = SubmitField('Send')

class EditNameForm(FlaskForm):
    first_name = StringField('Fornavn', validators=[DataRequired()])
    last_name = StringField('Etternavn', validators=[DataRequired()])
    submit = SubmitField('Send')

class EditEmailForm(FlaskForm):
    def validate_email(form, field):
        email = User.query.filter_by(email=field.data).first()
        if email is not None:
            flash('Email er allerede brukt')
            raise ValidationError('Email er allerede brukt.')

    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Send')

class EditSexForm(FlaskForm):
    sex = SelectField('Kjønn', validators=[DataRequired()], choices=[('male', 'Mann'), ('female', 'Kvinne'), ('other', 'Annet')])
    sumbit = SubmitField('Send')

class EditPasswordForm(FlaskForm):
    def validate_password(form, field):
        if form.check_password(field.data):
            flash('Passordet må ha 8 tegn, og inneholde minst en stor bokstav og et tall')
            raise ValidationError('Passordet må ha 8 tegn, og inneholde minst en stor bokstav og et tall.')

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
            return False
        return True

    password = PasswordField('Passord', validators=[DataRequired()])
    password2 = PasswordField('Gjenta passord',
                              validators=[DataRequired(), EqualTo('password', message="Passord må være like")])
    sumbit = SubmitField('Send')