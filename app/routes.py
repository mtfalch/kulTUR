from flask import render_template, flash, redirect, url_for, request, jsonify
from geoalchemy2 import func
from werkzeug.urls import url_parse
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import SignUpForm, LoginForm, EditProfileForm, EditTlfForm, EditNameForm, EditEmailForm, EditSexForm
from app.models import User, Tracks, Trips
from json import loads
from datetime import datetime
from geojson import FeatureCollection, Feature
from sqlalchemy import text

@app.route('/')
@app.route('/index')
@app.route('/mainpage')

def mainpage():
	return render_template('mainpage.html', title='Main Page')

@app.route('/map')
def map():
	return render_template('map.html', title='Map')

@app.route('/tracks')
def get_tracks():
	query = db.session.query(Tracks.lokalid, Tracks.rutenavn, Tracks.objtype, func.ST_AsGeoJSON(Tracks.geog)).all()
	res = FeatureCollection([])

	for i, q in enumerate(query):
		new = Feature(properties={"LOKALID": q[0], "RUTENAVN": q[1], "OBJTYPE": q[2]}, geometry=loads(q[3]))
		res['features'].append(new)

	return jsonify(res)

@app.route('/usertrips')
def get_user_trips():
	query = db.session.query(
		Tracks
	).join(
		Trips
	).join(
		User
	).filter(
		User.id == current_user.get_id()
	).with_entities(
		Tracks.lokalid, Tracks.rutenavn, Tracks.objtype, func.ST_AsGeoJSON(Tracks.geog)
	).all()

	res = FeatureCollection([])
	for i, q in enumerate(query):
		new = Feature(properties={"LOKALID": q[0], "RUTENAVN": q[1], "OBJTYPE": q[2]}, geometry=loads(q[3]))
		res['features'].append(new)

	return jsonify(res)

@app.route('/tracks/summer')
def summer():
	query = db.session.query(Tracks.lokalid, Tracks.rutenavn, Tracks.objtype, func.ST_AsGeoJSON(Tracks.geog)).filter(Tracks.objtype == 'Fotrute').all();
	res = FeatureCollection([])
	for i, q in enumerate(query):
		new = Feature(properties={"LOKALID": q[0], "RUTENAVN": q[1], "OBJTYPE": q[2]}, geometry=loads(q[3]))
		res['features'].append(new)
	return jsonify(res)

@app.route('/tracks/winter')
def winter():
	query = db.session.query(Tracks.lokalid, Tracks.rutenavn, Tracks.objtype, func.ST_AsGeoJSON(Tracks.geog)).filter(Tracks.objtype != 'Fotrute').all();
	res = FeatureCollection([])
	for i, q in enumerate(query):
		new = Feature(properties={"LOKALID": q[0], "RUTENAVN": q[1], "OBJTYPE": q[2]}, geometry=loads(q[3]))
		res['features'].append(new)
	return jsonify(res)

@app.route('/usertrips', methods=['POST'])
@login_required
def usertrips():
	if current_user.is_authenticated:
		data = request.data.decode('UTF-8')
		variabel = data.split('&')

		datedata = variabel[0]
		liddata = variabel[1]

		datedata = datedata.replace('date=','')
		today = datetime.strptime(datedata, '%d%m%Y').date()

		liddata = liddata.replace('lid=', '')
		gid = db.session.query(Tracks.gid).filter(Tracks.lokalid == liddata) # dette er riktig

		user = current_user.get_id()
		usertrip = Trips(comment = ' ',
							 time = today,
							 user_id = user,
							 track_id = gid)
		db.session.add(usertrip)
		db.session.commit()
		flash('Turen er registrert')
		return render_template('map.html', title='map')
	else:
		flash('Du må logge inn for å registrere tur')
		return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Ugyldig brukernavn eller passord')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('mainpage')
		return redirect(next_page)
	return render_template('login_html.html', title='Log In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('mainpage'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	if current_user.is_authenticated:
		return redirect(url_for('mainpage'))
	form = SignUpForm()
	if form.validate_on_submit():
		user = User(first_name=form.first_name.data,
					last_name=form.last_name.data,
					tlf=form.tlf.data,
					username=form.username.data,
					email=form.email.data, sex = form.sex.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Gratulerer, du er nå en registrert bruker!')
		return redirect(url_for('mainpage'))
	return render_template('registration.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):

	tuser = current_user
	trips = db.session.query(
		Tracks
	).	join(
		Trips
	).join(
		User
	).filter(
		User.id == current_user.get_id()
	).with_entities (
		Trips.id, Trips.time, Tracks.objtype, Tracks.rutenavn, func.ST_AsGeoJSON(Tracks.geog)
	).all()
	return render_template('user.html', user=tuser, trips=trips)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		db.session.commit()
		flash('Endringene dine er lagret.')
		return redirect(url_for('user', username=current_user.username))
	elif request.method == 'GET':
		form.username.data = current_user.username
	return render_template('edit.html', title='Edit profile', form = form)

@app.route('/edit_tlf', methods=['GET', 'POST'])
@login_required
def edit_tlf():
	form = EditTlfForm()
	if form.validate_on_submit():
		current_user.tlf = form.tlf.data
		db.session.commit()
		flash('Endringene dine er lagret.')
		return redirect(url_for('user', username=current_user.username))
	elif request.method == 'GET':
		form.tlf.data = current_user.tlf
	return render_template('edit_tlf.html', title='Edit tlf', form = form)

@app.route('/edit_name', methods=['GET', 'POST'])
@login_required
def edit_name():
	form = EditNameForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		db.session.commit()
		flash('Endringene dine er lagret.')
		return redirect(url_for('user', username=current_user.username))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
	return render_template('edit_name.html', title='Edit name', form = form)


@app.route('/edit_mail', methods=['GET', 'POST'])
@login_required
def edit_mail():
	form = EditEmailForm()
	if form.validate_on_submit():
		current_user.email = form.email.data
		db.session.commit()
		flash('Endringene dine er lagret.')
		return redirect(url_for('user', username=current_user.username))
	elif request.method == 'GET':
		form.email.data = current_user.email
	return render_template('edit_mail.html', title='Edit mail', form = form)


@app.route('/edit_sex', methods=['GET', 'POST'])
@login_required
def edit_sex():
	form = EditSexForm()
	if form.validate_on_submit():
		current_user.sex = form.sex.data
		db.session.commit()
		flash('Endringene dine er lagret.')
		return redirect(url_for('user', username=current_user.username))
	elif request.method == 'GET':
		form.sex.data = current_user.sex
	return render_template('edit_sex.html', title='Edit sex', form = form)
