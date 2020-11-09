import pandas as pd
import pymongo

df = pd.read_csv('1000 Records.csv')
df.columns = [
    'EmpID',
    'NamePrefix',
    'FirstName',
    'MiddleInitial',
    'LastName',
    'Gender',
    'EMail',
    'FathersName',
    'MothersName',
    'MothersMaidenName',
    'DateofBirth',
    'TimeofBirth',
    'AgeinYrs',
    'WeightinKgs',
    'DateofJoining',
    'QuarterofJoining',
    'HalfofJoining',
    'YearofJoining',
    'MonthofJoining',
    'MonthNameofJoining',
    'ShortMonth',
    'DayofJoining',
    'DOWofJoining',
    'ShortDOW',
    'AgeinCompanyinYears',
    'Salary',
    'LastHikePercentage',
    'SSN',
    'PhoneNo',
    'PlaceName',
    'County',
    'City',
    'State',
    'Zip',
    'Region',
    'UserName',
    'Password']

df = df.astype(str)
data = df.to_dict('records')

myclient = pymongo.MongoClient("mongodb://localhost:27017/mydb")
mydb = myclient["mydb"]
mycol = mydb["Employee"]

x = mycol.insert(data)
