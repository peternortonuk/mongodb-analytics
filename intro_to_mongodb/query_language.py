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

collection = initial_collection

# string must match exactly; show all columns
projection1 = None
query1 = {'language': 'Korean, English'}

# select some columns to display; define a sort key
projection2 = {'title': 1, 'language': 1, '_id': 0}
query2 = {'language': 'Korean, English'}
sort_key2 = 'languages'

# choose parameters
projection = projection1
query = query1
sort_key = sort_key2

# run the query
results = collection.find(query, projection).sort(sort_key, DESCENDING)


# =========================
# movies_clean

collection = clean_collection

# must contain these values in exactly this order
projection1 = {'_id': 0, 'languages': 1}
query1 = {'languages': ['Korean', 'English']}

# must contain these values but without regard to order or other elements in the array
query2 = {'languages': {'$all': ['Korean', 'English']}}

# must contain two elements but can be in any order
# use implicit logical AND operator when using a comma separated list of expressions
query3 = {'languages': {
    '$all': ['Korean', 'English'], '$size': 2,
    }}

# an explicit AND with the $and operator is necessary when the same field or operator has to be specified in multiple expressions.
# doesnt work; i think this is a bug
query4 = {'&and': [
    {'languages': {'$all': ['English', 'German']}},
    {'languages': {'$size': 2}},
    ]
}

# choose parameters
query = query4
projection = projection2
sort_key = 'languages'

# run the query
results = collection.find(query, projection).sort(sort_key, DESCENDING)
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

