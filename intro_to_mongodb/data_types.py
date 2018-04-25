import pymongo
import pprint
from datetime import datetime
from bson.decimal128 import Decimal128
from notebooks.connect import uri

# =================================
# connect and define the collection

course_cluster_uri = uri('3.4')
course_client = pymongo.MongoClient(course_cluster_uri)

movies = course_client['mflix']['movies_initial']

test = course_client['test']
dates = test['dates']
decimals = test['decimals']

# =================================
# analysis

# insert bson type data
dates.insert_one({ "dt": datetime.utcnow() })
doc = dates.find_one()
pprint.pprint(doc)

decimals.insert_one({ "money": Decimal128("99.99") })
doc = decimals.find_one()
pprint.pprint(doc)

# find doc based on type
doc = movies.find_one({ "year": { "$type": "int" } })
pprint.pprint(doc)

