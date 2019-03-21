from app import db
from app.models import Tracks2

res = db.engine.execute('select gid from turstierl')
for row in res:
	print("GID:", row['gid'])
