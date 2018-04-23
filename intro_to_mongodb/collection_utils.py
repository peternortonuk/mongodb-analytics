from pymongo import MongoClient
from notebooks.connect import uri

client = MongoClient(uri('3.4'))



def copy_collection(origin_collection, destination_collection):

    pipeline = [ {"$match": {}},
                 {"$out": destination_collection},
    ]

    origin_collection.aggregate(pipeline)

    return




if '__name__' == '__main__':

    # drop the new one
    client.mflix.movies_clean.drop()

    # copy again
    origin_collection = client.mflix.movies_initial
    destination_collection = 'movies_clean'

    x = copy_collection(origin_collection, destination_collection)