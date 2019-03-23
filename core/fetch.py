from app import db
from geoalchemy2 import Geometry, func
from app.models import Tracks2


query = db.session.query(Tracks2.gid, Tracks2.lokalid, func.ST_AsGeoJSON(Tracks2.geog, 6)).all()

f = open("../app/static/js/tracks.js", "w")
f.write("var tracks =")
f.write("[")
f.write(query[0][2])
f.write(",")
f.write(query[1][2])
#for i, q in enumerate(query):
#	f.write(query[i][2])
#	f.write(",")
f.write("]")
f.close()

#for row in query:
#	print(row)
