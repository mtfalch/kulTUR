from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SignUpForm

@app.route('/')
@app.route('/index')
def index():
    return "Main page"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('SignUp requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign up', form=form)


