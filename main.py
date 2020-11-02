import csv
from pymongo import MongoClient


class MongoDB(object):

    def __init__(self, db_name=None, collection_name=None):
        self.db_name = db_name
        self.collection_name = collection_name

        self.client = MongoClient("localhost", 27017)

        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def csv_reader(self):
        with open(r"C:\Users\DELL\Desktop\100000 Sales Records.csv", 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                yield row

    def read_each_doc(self):
        read_obj = self.csv_reader()
        ls = []
        for each in read_obj:
            ls.append(each)
            return ls

    def insert_each_record(self, path):
        try:
            with open(path, 'r') as sales_records:
                read_sales_records = csv.DictReader(sales_records)
                for each in read_sales_records:
                    self.collection.insert_one(each)
                print("successfully inserted each document")
        except Exception as e:
            print(e)

    def total_no_of_records(self):
        doc_count = self.collection.count_documents({})
        print("Total number of documents : ", doc_count)

    def sorting_records_ascend(self, fieldname):
        records_ascend = self.collection.find().sort(fieldname, 1)
        # for each in records_ascend:
        # print(each)

    def sorting_records_descend(self, fieldname):
        records_descend = self.collection.find().sort(fieldname, -1)
        # for each in records_descend:
        # print(each)


if __name__ == "__main__":
    sales_rec = MongoDB(db_name='Sales_DB', collection_name='Sales_Records')
    sales_rec.insert_each_record(path=r"C:\Users\DELL\Desktop\100000 Sales Records.csv")
    # sales_rec.read_each_doc()
    sales_rec.total_no_of_records()
    # sales_rec.sorting_records_ascend('Total Profit')
    # sales_rec.sorting_records_descend('Total Profit')
