from utilities import SalesOperations

import json

from utilities import DbConnection


class SalesService:  # creating class for database operations

    """def __init__(self, host, port, db_name, coll_name, path, db_conn):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.coll_name = coll_name
        self.path = path
        self.db_conn = db_conn"""

    def __init__(self):
        self.conn = DbConnection.db_connection()

    def save_sales_data(self, data):
        inserted_recs = []

        for row in data:
            if row not in SalesOperations.total_docs_in_db(self.conn):
                recs = SalesOperations.insert_each_record(self.conn, row)
                inserted_recs.append(recs)
            else:
                return "document already exists "

    def get_num_of_docs(self):
        return SalesOperations.total_no_of_records(self.conn)


    def sort_docs(self):
        pass

