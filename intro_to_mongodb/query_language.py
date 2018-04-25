from pymongo import MongoClient
from notebooks.connect import uri
import pprint

# =================================
# connect and define the collection

client = MongoClient(uri('3.4'))
movies_collection = client.mflix.movies_initial

# =================================
# projection and filter

projection = {}
filter = {'language': 'Korean, English'}


# =================================
# run the query

results = movies_collection.find(projection, filter)
pprint.pprint(list(results))

