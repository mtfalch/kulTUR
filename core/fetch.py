from app import db
from geoalchemy2 import Geometry, func
from app.models import Tracks
from geojson import Feature, geometry



query = db.session.query(func.ST_AsGeoJSON(Tracks.geog)).first()



print(query[0])

#for row in query:
#	print(row)
