from pymongo import MongoClient
from notebooks.connect import uri
import pprint

'''
=================================
reference:
https://docs.mongodb.com/manual/core/aggregation-pipeline/
=================================
'''


# =================================
# connect and define the collection

client = MongoClient(uri('3.4'))
movies_collection = client.mflix.movies_initial


# =================================
# match and group pipelines

pipeline1 = [
    {
        '$match': {'language': 'Korean, English'}
    }
]

pipeline2 = [
    {
        '$group': {
            '_id': {"language": "$language"},
            'count': {'$sum': 1}
        }
    },
    {
        '$sort': {'count': -1}
    }
]



pipeline3 = [
    {
        '$sortByCount': "$language"
    }
]

# =================================
# choose the pipeline

pipeline = pipeline1


# =================================
# run the query

results = movies_collection.aggregate(pipeline)
pprint.pprint(list(results)[0])


# ==================================================================
# ==================================================================
# reshaping

# pymongo.errors.OperationFailure: Unrecognized expression '$dateFromString'
# when using < mongoDB v3.6

pipeline = [
    {
        '$limit': 100
    },
    {
        '$addFields': {
            'lastupdated': {
                '$arrayElemAt': [
                    {'$split': ["$lastupdated", "."]},
                    0
                ]}
        }
    },
    {
        '$project': {
            'title': 1,
            'year': 1,
            'directors': {'$split': ["$director", ", "]},
            'actors': {'$split': ["$cast", ", "]},
            'writers': {'$split': ["$writer", ", "]},
            'genres': {'$split': ["$genre", ", "]},
            'languages': {'$split': ["$language", ", "]},
            'countries': {'$split': ["$country", ", "]},
            'plot': 1,
            'fullPlot': "$fullplot",
            'rated': "$rating",
            'released': {
                '$cond': {
                    'if': {'$ne': ["$released", ""]},
                    'then': {
                        '$dateFromString': {
                            'dateString': "$released"
                        }
                    },
                    'else': ""}},
            'runtime': 1,
            'poster': 1,
            'imdb': {
                'id': "$imdbID",
                'rating': "$imdbRating",
                'votes': "$imdbVotes"
                },
            'metacritic': 1,
            'awards': 1,
            'type': 1,
            'lastUpdated': {
                '$cond': {
                    'if': {'$ne': ["$lastupdated", ""]},
                    'then': {
                        '$dateFromString': {
                            'dateString': "$lastupdated",
                            'timezone': "America/New_York"
                        }
                    },
                    'else': ""}}
        }
    },
    {
        '$out': "movies_scratch"
    }
]


# =================================
# run the query

results = movies_collection.aggregate(pipeline)
pprint.pprint(list(results))