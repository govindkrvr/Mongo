import csv
from pymongo import MongoClient

demo_client = MongoClient()
my_client = MongoClient('localhost', 27017)

my_db = my_client["test2_Sales_DB"]
coll = my_db["Sales_record"]


def get_multiple_records(read_sales_records, limit):
    ls = []
    for i in range(limit):
        ls.append(next(read_sales_records))
        yield ls

limit = int(input('enter number of documents to be uploaded at a time : '))

with open(r'C:\Users\DELL\Desktop\100000 Sales Records.csv', 'r') as sales_records:
    read_sales_records = csv.DictReader(sales_records)

    y = next(get_multiple_records(read_sales_records, limit))

    while y is not None:
        try:
            coll.insert_many(y)
            y = next(get_multiple_records(read_sales_records, limit))
        except Exception as e:
            y = None
