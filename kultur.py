from app import app, db
from app.models import User, Trips, Tracks

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Trips': Trips, 'Tracks': Tracks}