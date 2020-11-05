from utilities import SalesOperations, DbConnection


class SalesService:  # creating class for database operations

    """
    class contains sales data operations
    """

    def __init__(self):
        self.conn = DbConnection.db_connection()

    def save_sales_data(self, data):
        """
        method call to insert each record
        :param data: documents
        :return: inserts the doc into collection , if doc already exists else statement returns
        """
        inserted_recs = []
        sales_op_obj = SalesOperations()

        for row in data:
            if row not in sales_op_obj.get_total_docs_in_db(self.conn):
                recs = sales_op_obj.insert_each_record(self.conn, row)
                inserted_recs.append(recs)
            else:
                return "document already exists "

    def get_num_of_docs(self):
        """
        method to get the total docs in collection
        :return: total docs in collection returns
        """
        sales_op_obj = SalesOperations()
        total_docs = sales_op_obj.total_no_of_records(self.conn)
        return total_docs

    def sort_docs_ascending(self, fieldname):
        """
        method to arrange the documents in ascending order based on the field name
        :param fieldname: coloumn name in collection
        :return: docs in ascending order
        """
        sort_sales = SalesOperations()
        sorted_data = sort_sales.sorting_records_ascend(self.conn, fieldname)
        return "sorted documents successfully"

    def sort_docs_descending(self, fieldname):
        """
        method to arrange the documents in descending order based on the field name
        :param fieldname: coloumn name in collection
        :return: docs in descending order
        """
        sort_sales = SalesOperations()
        sorted_data = sort_sales.sorting_records_ascend(self.conn, fieldname)
        return "sorted documents successfully"

    def delete_doc(self, field_name, field_value):
        """
        to delete a single document based on the column name and its value
        :param field_name: column name
        :param field_value: value
        :return: deltes that particular record
        """
        sales_obj = SalesOperations()
        delete_doc = sales_obj.delete_one_record(self.conn, field_name, field_value)
        return "document deleted successfully"
