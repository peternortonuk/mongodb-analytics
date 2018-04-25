from pymongo import MongoClient
import argparse
from notebooks.connect import uri


def copy_collection(client, origin_collection, destination_collection):

    origin = split_db_name(origin_collection)
    origin_db = client[origin['database']]
    origin_coll = origin_db[origin['collection']]

    destination = split_db_name(destination_collection)

    pipeline = [{"$match": {}},
                {"$out": destination['collection']},
                ]

    origin_coll.aggregate(pipeline)


def drop_collection(client, drop_collection):
    drop = split_db_name(drop_collection)
    db = client[drop['database']]
    c = db[drop['collection']]
    c.drop()


def split_db_name(collection_name):
    collection_list = collection_name.split('.')
    return {'database': collection_list[0],
            'collection': collection_list[1]}


def main_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--drop", help='collection name')
    parser.add_argument("-c", "--copy", nargs='+', help='origin_collection, destination_collection')
    return parser.parse_args()


if __name__ == '__main__':

    args = main_args()
    client = MongoClient(uri('3.4'))

    if args.drop:
        drop_collection(client, args.drop)

    if args.copy:
        copy_collection(client, args.copy[0], args.copy[1])

'''
origin_collection = 'mflix.movies_initial'
destination_collection = 'mflix.movies_clean'
drop_collection = destination_collection

python collection_utils.py --drop mflix.movies_clean
python collection_utils.py --copy mflix.movies_initial mflix.movies_clean
'''