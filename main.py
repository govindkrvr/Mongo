from run import SalesService
from utilities import CsvReader, JsonData

"""
asc_field_name = input("Enter the field name based on which the database has to sort in ascending order : ")
desc_field_name = input("Enter the field name based on which the database has to sort in descending order : ")
field_name = input("Enter the field name of collection which to delete")
field_value = input("Enter the field name of collection which to delete")
"""

if __name__ == "__main__":
    csv_reader_obj = CsvReader()
    sales_service = SalesService()
    data = csv_reader_obj.get_each_doc(JsonData.get_path())

    print(sales_service.save_sales_data(data))
    print(sales_service.get_num_of_docs())

    # print(sales_service.sort_docs_descending(desc_field_name))# uncomment this to sort the records in descending order
    # print(sales_service.sort_docs_ascending(asc_field_name))  # uncomment this to sort the records in descending order
    # print(sales_service.delete_doc(field_name, field_value))  # uncomment this to delete a record from database
