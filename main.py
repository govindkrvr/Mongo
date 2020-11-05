from run import SalesService
from utilities import CsvReader, JsonData


class SalesController:

    @staticmethod
    def read_data(path):
        data = CsvReader.read_each(path)
        return data


"read data here"

if __name__ == "__main__":
    obj = SalesController()
    sales_service = SalesService()
    data = obj.read_data(JsonData.get_path())

    print(sales_service.save_sales_data(data))
    print(sales_service.get_num_of_docs())
