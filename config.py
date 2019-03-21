import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	SQLALCHEMY_DATABASE_URI = 'postgres://vmewlvproubfvc:3fcf73c0763ae68782d5059c9a61b64a2a7493cb18ed64d8c53ee6a2d31393d9@ec2-50-19-109-120.compute-1.amazonaws.com:5432/d8rso2b0c8pjmv' or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False