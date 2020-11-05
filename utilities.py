"""

"""

from pymongo import MongoClient
import csv
import json


class JsonData:
    """
    class to get the json data of config file
    """

    @staticmethod
    def get_path():
        """
        method to get the path of csv file
        :return: path location wil be returned
        """
        with open('config.json') as file:
            data = json.load(file)
            path = data['path']
            return path


class CsvReader:
    """
    class to read the csv data
    """

    @staticmethod
    def read_each_doc(path):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                yield row

    @staticmethod
    def get_each_doc(path):
        """
        method to read the data from the csv file
        :param path: csv file path
        :return:
        """
        data = CsvReader.read_each_doc(path)
        lst_data = []
        for doc in data:
            lst_data.append(doc)
        return lst_data


class DbConnection:
    """
    creating class for database connection
    """

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
    """
    class for mongodb CRUD operations
    """

    @staticmethod
    def get_total_docs_in_db(db_conn):
        """
        to get all docs from collection
        :param db_conn: database connection
        :return: list of all docs present in collection
        """
        total_docs = []
        for doc in db_conn.find({}, {'_id': 0}):
            total_docs.append(doc)

            return total_docs

    @staticmethod
    def insert_each_record(db_conn, record):
        """
        method for inserting each record from csv file to collection
        :param db_conn: database connection
        :param record: each document in csv file
        :return: inserts each record into collection else throws exception
        """
        try:
            db_conn.insert_one(record)
            return "inserted successfully"
        except Exception as e:
            return e

    @staticmethod
    def total_no_of_records(db_conn):
        """
        method to get total number of records in collection
        :param db_conn: database connection
        :return: total number of records in collection
        """
        try:
            doc_count = db_conn.count_documents({})
            return doc_count
        except Exception as e:
            return e

    @staticmethod
    def sorting_records_ascend(db_conn, fieldname):
        """
        method to sort the database in ascending order based on the input field name
        :param db_conn: database connection
        :param fieldname: based on this field name documents sort in ascending order
        :return: sorted documents in database
        """
        try:
            records_ascend = db_conn.find().sort(fieldname, 1)
            # for each in records_ascend:          # uncomment this to get the sorted records
            # return each
            return db_conn.find()
        except Exception as e:
            return e

    @staticmethod
    def sorting_records_descend(db_conn, fieldname):
        """
        method to sort the database in descending order based on the input field name
        :param db_conn: database connection
        :param fieldname: based on this field name documents sort in ascending order
        :return: sorted documents in database
        """

        try:
            records_descend = db_conn.find().sort(fieldname, -1)
            # for each in records_descend:          # uncomment this to get the sorted records
            # return each
        except Exception as e:
            return e

    @staticmethod
    def delete_one_record(db_conn, field_name, field_value):
        try:
            del_rec = db_conn.delete_one({field_name: field_value})

        except Exception as e:
            return e
