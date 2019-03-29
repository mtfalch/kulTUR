from app import db
from geoalchemy2 import func
from app.models import Tracks
from json import loads
from geojson import Feature, FeatureCollection

'''''
query = db.session.query(Tracks.lokalid, func.ST_AsGeoJSON(Tracks.geog)).all()

first = Feature(properties={"LOKALID": query[0][0]}, geometry=loads(query[0][1]))
second = Feature(properties={"LOKALID": query[1][0]}, geometry=loads(query[1][1]))
res = FeatureCollection([])

for i, q in enumerate(query):
	new = Feature(properties={"LOKALID": q[0]}, geometry=loads(q[1]))
	res['features'].append(new)

print(res.features[1].properties['LOKALID'])
'''''

query = db.session.query(Tracks.gid).all()
for q in query:
	print(q)