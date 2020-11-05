from pymongo import MongoClient
import csv
import json


class JsonData:
    @staticmethod
    def get_path():
        with open('config.json') as file:
            data = json.load(file)
            path = data['path']
            return path


class CsvReader:  # creating class for operations on csv file

    @staticmethod  # method to read the csv file using generators
    def read_each(path):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            list_data = []

            for row in reader:
                list_data.append(row)
            return list_data


class DbConnection:  # creating class for database connection

    @staticmethod
    def db_connection():  # method for database connection
        with open('config.json') as file:
            data = json.load(file)
            port = data['port']
            host = data['host']
            database_name = data['db_name']
            coll_name = data['collection_name']

        mongo_client = MongoClient(host, port)
        db_name = mongo_client[database_name]
        collection_name = db_name[coll_name]
        db_connect = db_name[coll_name]
        return db_connect


class SalesOperations:
    @staticmethod
    def total_docs_in_db(db_conn):
        total_docs = []
        for doc in db_conn.find({}, {'_id': 0}):
            total_docs.append(doc)

            return total_docs

    @staticmethod
    def insert_each_record(db_conn, records):  # method for inserting each record from csv file to mongo database
        db_conn.insert_one(records)
        return "inserted successfully"

    @staticmethod
    def total_no_of_records(db_conn):  # method for getting total number of records in database
        doc_count = db_conn.count_documents({})
        return doc_count

    @staticmethod
    def sorting_records_ascend(db_conn,
                               fieldname):  # method to sort the database in ascending order based on the input field name
        records_ascend = db_conn.find().sort(fieldname, 1)
        return db_conn.find()

    @staticmethod
    def sorting_records_descend(db_conn,
                                fieldname):  # method to sort the database in descending order based on the input field name
        records_descend = db_conn.find().sort(fieldname, -1)
        # for each in records_descend:          # uncomment this if to print the sorted records
        # print(each)
