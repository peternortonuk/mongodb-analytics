from pymongo import MongoClient
import argparse
from notebooks.connect import uri


def copy_collection(client, origin_collection, destination_collection):

    origin = origin_collection.split('.')
    origin_db = origin[0]
    origin_coll = origin[1]

    destination = destination_collection.split('.')
    destination_coll = destination[1]

    pipeline = [ {"$match": {}},
                 {"$out": destination_coll},
    ]

    db = client[origin_db]
    c = db[origin_coll]

    c.aggregate(pipeline)



def drop_collection(client, drop_collection):

    drop_ = drop_collection.split('.')
    drop_db = drop_[0]
    drop_coll = drop_[1]
    db = client[drop_db]
    c = db[drop_coll]
    c.drop()



def main_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--drop", help='collection name')
    parser.add_argument("-c", "--copy", nargs='+', help='origin_collection, destination_collection')
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = main_args()

    if args.drop:
        client = MongoClient(uri('3.4'))
        drop_collection(client, args.drop)

    if args.copy:
        client = MongoClient(uri('3.4'))
        copy_collection(client, args.copy[0], args.copy[1])

'''
origin_collection = 'mflix.movies_initial'
destination_collection = 'mflix.movies_clean'
drop_collection = destination_collection

python collection_utils.py --drop mflix.movies_clean
python collection_utils.py --copy mflix.movies_initial mflix.movies_clean
'''