from pymongo import MongoClient
from notebooks.connect import uri
import pprint

client = MongoClient(uri('3.4'))


# =================================
# projection and filter

projection = {}
filter = {'language': 'Korean, English'}


# =================================
# run the query

results = client.mflix.movies_initial.find(projection, filter)
pprint.pprint(list(results))

