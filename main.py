"""
main.py which is a driver script to invoke the program(if __name__ == "__main__":)
"""
import run



if __name__ == "__main__":
    sales_rec = MongoDB(db_name='Sales_DB', collection_name='Sales_Records')
    sales_rec.insert_each_record(path=r"C:\Users\DELL\Desktop\100000 Sales Records.csv")
    # sales_rec.read_each_doc()
    sales_rec.total_no_of_records()
    # sales_rec.sorting_records_ascend('Total Profit')
    # sales_rec.sorting_records_descend('Total Profit')
