from pymongo import MongoClient, DESCENDING
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
initial_collection = client.mflix.movies_initial
clean_collection = client.mflix.movies_clean

# =================================
# projection and filter


# =========================
# movies_initial

projection = {'title': 1, 'language': 1, '_id': 0}
projection = None
query = {'language': 'Korean, English'}

# string must match exactly
projection1 = {'_id': 0, 'language': 1}
filter1 = {'language': 'Korean, English'}


# =========================
# movies_clean

# must contain these values in exactly this order
projection2 = {'_id': 0, 'languages': 1}
filter2 = {'languages': ['Korean', 'English']}

# must contain these values but without regard to order or other elements in the array
filter3 = {'languages': {'$all': ['Korean', 'English']}}

# must contain two elements but can be in any order
# use implicit logical AND operator when using a comma separated list of expressions
filter4 = {'languages': {
    '$all': ['Korean', 'English'], '$size': 2,
    }}

# an explicit AND with the $and operator is necessary when the same field or operator has to be specified in multiple expressions.
# doesnt work; i think this is a bug
filter5 = {'&and': [
    {'languages': {'$all': ['English', 'German']}},
    {'languages': {'$size': 2}},
    ]
}
# =================================
# choose the collection, filter and projection

filter = filter4
projection = projection2
collection = clean_collection
sort_key = 'languages'

# =================================
# run the query

results = collection.find(filter, projection).sort(sort_key, DESCENDING)
length = 20
results = results[:length]
for result in results:
    #print(type(result['language']))
    pprint.pprint(result)

results = collection.find(query, projection).limit(3)
pprint.pprint(list(results))


# =================================
# work with results cursor

titles = []
for row in results:
    titles.append(row['title'])
pprint.pprint(titles)

