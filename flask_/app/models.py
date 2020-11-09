from app import db


class Employee(db.Document):

    EmpID = db.StringField()
    NamePrefix = db.StringField()
    FirstName = db.StringField()
    MiddleInitial = db.StringField()
    LastName = db.StringField()
    Gender = db.StringField()
    EMail = db.StringField()
    FathersName = db.StringField()
    MothersName = db.StringField()
    MothersMaidenName = db.StringField()
    DateofBirth = db.StringField()
    TimeofBirth = db.StringField()
    AgeinYrs = db.StringField()
    WeightinKgs = db.StringField()
    DateofJoining = db.StringField()
    QuarterofJoining = db.StringField()
    HalfofJoining = db.StringField()
    YearofJoining = db.StringField()
    MonthofJoining = db.StringField()
    MonthNameofJoining = db.StringField()
    ShortMonth = db.StringField()
    DayofJoining = db.StringField()
    DOWofJoining = db.StringField()
    ShortDOW = db.StringField()
    AgeinCompanyinYears = db.StringField()
    Salary = db.StringField()
    LastHikePercentage = db.StringField()
    SSN = db.StringField()
    PhoneNo = db.StringField()
    PlaceName = db.StringField()
    County = db.StringField()
    City = db.StringField()
    State = db.StringField()
    Zip = db.StringField()
    Region = db.StringField()
    UserName = db.StringField()
    Password = db.StringField()
