from pymongo import MongoClient
from notebooks.connect import uri
import pprint

'''
=================================
reference:
https://docs.mongodb.com/manual/reference/method/db.collection.find/
db.collection.find(query, projection)
=================================
'''


# =================================
# connect and define the collection

client = MongoClient(uri('3.4'))
movies_collection = client.mflix.movies_initial

# =================================
# projection and filter

projection = {'title': 1, 'language': 1, '_id': 0}
projection = None
query = {'language': 'Korean, English'}


# =================================
# run the query

results = movies_collection.find(query, projection).limit(3)
pprint.pprint(list(results))


# =================================
# work with results cursor

titles = []
for row in results:
    titles.append(row['title'])
pprint.pprint(titles)



