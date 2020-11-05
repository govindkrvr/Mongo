from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017)
db_name = mongo_client["Sales_DB"]
collection_name = db_name["Sales_records"]
db_connect = db_name["Sales_records"]


def total_docs_in_db(db_conn):
    total_docs = []
    for doc in db_conn.find({}, {'_id': 0}):
        total_docs.append(doc)

        return total_docs


print(total_docs_in_db(db_connect))
