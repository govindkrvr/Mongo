

from flask import make_response, jsonify, request
import jwt
import datetime
from functools import wraps

from app import application
from app.models import Employee


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            if not token:
                return jsonify({'message': 'a valid token is missing'})
            try:
                data = jwt.decode(token, application.config['SECRET_KEY'])
            except:
                return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)

    return decorator


def dict_from_obj(employee):
    emp_dict = {
        'EmpID': employee.EmpID,
        'NamePrefix': employee.NamePrefix,
        'FirstName': employee.FirstName,
        'MiddleInitial': employee.MiddleInitial,
        'LastName': employee.LastName,
        'Gender': employee.Gender,
        'EMail': employee.EMail,
        'FathersName': employee.FathersName,
        'MothersName': employee.MothersName,
        'MothersMaidenName': employee.MothersMaidenName,
        'DateofBirth': employee.DateofBirth,
        'TimeofBirth': employee.TimeofBirth,
        'AgeinYrs': employee.AgeinYrs,
        'WeightinKgs': employee.WeightinKgs,
        'DateofJoining': employee.DateofJoining,
        'QuarterofJoining': employee.QuarterofJoining,
        'HalfofJoining': employee.HalfofJoining,
        'YearofJoining': employee.YearofJoining,
        'MonthofJoining': employee.MonthofJoining,
        'MonthNameofJoining': employee.MonthNameofJoining,
        'ShortMonth': employee.ShortMonth,
        'DayofJoining': employee.DayofJoining,
        'DOWofJoining': employee.DOWofJoining,
        'ShortDOW': employee.ShortDOW,
        'AgeinCompanyinYears': employee.AgeinCompanyinYears,
        'Salary': employee.Salary,
        'LastHikePercentage': employee.LastHikePercentage,
        'SSN': employee.SSN,
        'PlaceName': employee.PlaceName,
        'County': employee.County,
        'City': employee.City,
        'State': employee.State,
        'Zip': employee.Zip,
        'Region': employee.Region,
        'UserName': employee.UserName,
        'Password': employee.Password,
    }
    return emp_dict


@application.route('/')
def index():
    return "Welcome to Employee Management System"


@application.route('/login', methods=['GET', 'POST'])
def login():
    """
    for authorization of admin to create, update , delete and retrieve employee from database
    """
    auth = request.form
    if not auth or not auth['username'] or not auth['password']:
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    if auth['username'] == 'admin' and auth['password'] == '123':
        token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)},
                           application.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


@application.route('/add_employee', methods=['POST'])
@token_required
def add_employee():
    """
    method to create an employee
    :return: checks whether employee exists or not by using employee id which is unique if exists
    returns employee already exists if not creates an employee and stores it in database

    """
    try:
        EmpID = str(request.form.get("EmpID", ""))
        NamePrefix = str(request.form.get("NamePrefix", ""))
        FirstName = str(request.form.get("FirstName", ""))
        MiddleInitial = str(request.form.get("MiddleInitial", ""))
        LastName = str(request.form.get("LastName", ""))
        Gender = str(request.form.get("Gender", ""))
        EMail = str(request.form.get("EMail", ""))
        FathersName = str(request.form.get("FathersName", ""))
        MothersName = str(request.form.get("MothersName", ""))
        MothersMaidenName = str(request.form.get("MothersMaidenName", ""))
        DateofBirth = str(request.form.get("DateofBirth", ""))
        TimeofBirth = str(request.form.get("TimeofBirth", ""))
        AgeinYrs = str(request.form.get("AgeinYrs", ""))
        WeightinKgs = str(request.form.get("WeightinKgs", ""))
        DateofJoining = str(request.form.get("DateofJoining", ""))
        QuarterofJoining = str(request.form.get("QuarterofJoining", ""))
        HalfofJoining = str(request.form.get("HalfofJoining", ""))
        YearofJoining = str(request.form.get("YearofJoining", ""))
        MonthofJoining = str(request.form.get("MonthofJoining", ""))
        MonthNameofJoining = str(request.form.get("MonthNameofJoining", ""))
        ShortMonth = str(request.form.get("ShortMonth", ""))
        DayofJoining = str(request.form.get("DayofJoining", ""))
        DOWofJoining = str(request.form.get("DOWofJoining", ""))
        ShortDOW = str(request.form.get("ShortDOW", ""))
        AgeinCompanyinYears = str(request.form.get("AgeinCompanyinYears", ""))
        Salary = str(request.form.get("Salary", ""))
        LastHikePercentage = str(request.form.get("LastHikePercentage", ""))
        SSN = str(request.form.get("SSN", ""))
        PhoneNo = str(request.form.get("PhoneNo", ""))
        PlaceName = str(request.form.get("PlaceName", ""))
        County = str(request.form.get("County", ""))
        City = str(request.form.get("City", ""))
        State = str(request.form.get("State", ""))
        Zip = str(request.form.get("Zip", ""))
        Region = str(request.form.get("Region", ""))
        UserName = str(request.form.get("UserName", ""))
        Password = str(request.form.get("Password", ""))

        if EmpID == '' or EMail == '' or UserName == '':
            return_data = {
                'Success': False,
                'Status': 'Aborted',
                'Result': 'EmpID, EMAil, UserName Must Not be Empty'
            }
            return make_response(jsonify(return_data), 500)

        employee = Employee.query.filter_by(EmpID=EmpID).all()
        if employee:
            return_data = {
                'Success': False,
                'Status': 'Aborted',
                'Result': 'Employee Id is already exist'
            }
            return make_response(jsonify(return_data), 500)

        employee = Employee.query.filter_by(EMail=EMail).all()
        if employee:
            return_data = {
                'Success': False,
                'Status': 'Aborted',
                'Result': 'E-Mail Id is already exist'
            }
            return make_response(jsonify(return_data), 500)

        employee = Employee.query.filter_by(UserName=UserName).all()
        if employee:
            return_data = {
                'Success': False,
                'Status': 'Aborted',
                'Result': 'User Name is already exist'
            }
            return make_response(jsonify(return_data), 500)

        employee = Employee(EmpID=EmpID,
                            NamePrefix=NamePrefix,
                            FirstName=FirstName,
                            MiddleInitial=MiddleInitial,
                            LastName=LastName,
                            Gender=Gender,
                            EMail=EMail,
                            FathersName=FathersName,
                            MothersName=MothersName,
                            MothersMaidenName=MothersMaidenName,
                            DateofBirth=DateofBirth,
                            TimeofBirth=TimeofBirth,
                            AgeinYrs=AgeinYrs,
                            WeightinKgs=WeightinKgs,
                            DateofJoining=DateofJoining,
                            QuarterofJoining=QuarterofJoining,
                            HalfofJoining=HalfofJoining,
                            YearofJoining=YearofJoining,
                            MonthofJoining=MonthofJoining,
                            MonthNameofJoining=MonthNameofJoining,
                            ShortMonth=ShortMonth,
                            DayofJoining=DayofJoining,
                            DOWofJoining=DOWofJoining,
                            ShortDOW=ShortDOW,
                            AgeinCompanyinYears=AgeinCompanyinYears,
                            Salary=Salary,
                            LastHikePercentage=LastHikePercentage,
                            SSN=SSN,
                            PhoneNo=PhoneNo,
                            PlaceName=PlaceName,
                            County=County,
                            City=City,
                            State=State,
                            Zip=Zip,
                            Region=Region,
                            UserName=UserName,
                            Password=Password)
        employee.save()
        emp_dict = dict_from_obj(employee)

        return_data = {
            'Success': True,
            'Status': 'Created Successfully',
            'Result': emp_dict
        }
        return make_response(jsonify(return_data), 200)

    except Exception as e:
        return_data = {
            'Success': False,
            'Status': 'Aborted',
            'Result': 'Server Error'
        }
        return make_response(jsonify(return_data), 500)


@application.route('/update_employee/<id>', methods=['PUT'])
@token_required
def update_employee(employee_id):
    """
    method to update employee details based on employee id
    :param employee_id: for which employee id to update
    :return: checks whether employee exists or not by using employee id which is unique if exists
    update the employee details and stores it in database if not returns employee doesn't exists

    """
    try:
        employee = Employee.query.filter_by(EmpID=employee_id).first()
        if employee:

            EmpID = str(request.form.get("EmpID", ""))
            NamePrefix = str(request.form.get("NamePrefix", ""))
            FirstName = str(request.form.get("FirstName", ""))
            MiddleInitial = str(request.form.get("MiddleInitial", ""))
            LastName = str(request.form.get("LastName", ""))
            Gender = str(request.form.get("Gender", ""))
            EMail = str(request.form.get("EMail", ""))
            FathersName = str(request.form.get("FathersName", ""))
            MothersName = str(request.form.get("MothersName", ""))
            MothersMaidenName = str(request.form.get("MothersMaidenName", ""))
            DateofBirth = str(request.form.get("DateofBirth", ""))
            TimeofBirth = str(request.form.get("TimeofBirth", ""))
            AgeinYrs = str(request.form.get("AgeinYrs", ""))
            WeightinKgs = str(request.form.get("WeightinKgs", ""))
            DateofJoining = str(request.form.get("DateofJoining", ""))
            QuarterofJoining = str(request.form.get("QuarterofJoining", ""))
            HalfofJoining = str(request.form.get("HalfofJoining", ""))
            YearofJoining = str(request.form.get("YearofJoining", ""))
            MonthofJoining = str(request.form.get("MonthofJoining", ""))
            MonthNameofJoining = str(request.form.get("MonthNameofJoining", ""))
            ShortMonth = str(request.form.get("ShortMonth", ""))
            DayofJoining = str(request.form.get("DayofJoining", ""))
            DOWofJoining = str(request.form.get("DOWofJoining", ""))
            ShortDOW = str(request.form.get("ShortDOW", ""))
            AgeinCompanyinYears = str(request.form.get("AgeinCompanyinYears", ""))
            Salary = str(request.form.get("Salary", ""))
            LastHikePercentage = str(request.form.get("LastHikePercentage", ""))
            SSN = str(request.form.get("SSN", ""))
            PhoneNo = str(request.form.get("PhoneNo", ""))
            PlaceName = str(request.form.get("PlaceName", ""))
            County = str(request.form.get("County", ""))
            City = str(request.form.get("City", ""))
            State = str(request.form.get("State", ""))
            Zip = str(request.form.get("Zip", ""))
            Region = str(request.form.get("Region", ""))
            UserName = str(request.form.get("UserName", ""))
            Password = str(request.form.get("Password", ""))

            if EmpID:
                temp = Employee.query.filter_by(EmpID=EmpID).all()
                if temp:
                    return_data = {
                        'Success': False,
                        'Status': 'Aborted',
                        'Result': 'Employee Id already exist'
                    }
                    return make_response(jsonify(return_data), 500)
                else:
                    employee.EmpID = EmpID

            if EMail:
                temp = Employee.query.filter_by(EMail=EMail).all()
                if temp:
                    return_data = {
                        'Success': False,
                        'Status': 'Aborted',
                        'Result': 'E-Mail Id already exist'
                    }
                    return make_response(jsonify(return_data), 500)
                else:
                    employee.EMail = EMail

            if UserName:
                temp = Employee.query.filter_by(UserName=UserName).all()
                if temp:
                    return_data = {
                        'Success': False,
                        'Status': 'Aborted',
                        'Result': 'User Name already exist'
                    }
                    return make_response(jsonify(return_data), 500)
                else:
                    employee.UserName = UserName

            if NamePrefix:
                employee.NamePrefix = NamePrefix
            if FirstName:
                employee.FirstName = FirstName
            if MiddleInitial:
                employee.MiddleInitial = MiddleInitial
            if LastName:
                employee.LastName = LastName
            if Gender:
                employee.Gender = Gender
            if FathersName:
                employee.FathersName = FathersName
            if MothersName:
                employee.MothersName = MothersName
            if MothersMaidenName:
                employee.MothersMaidenName = MothersMaidenName
            if DateofBirth:
                employee.DateofBirth = DateofBirth
            if TimeofBirth:
                employee.TimeofBirth = TimeofBirth
            if AgeinYrs:
                employee.AgeinYrs = AgeinYrs
            if WeightinKgs:
                employee.WeightinKgs = WeightinKgs
            if DateofJoining:
                employee.DateofJoining = DateofJoining
            if QuarterofJoining:
                employee.QuarterofJoining = QuarterofJoining
            if HalfofJoining:
                employee.HalfofJoining = HalfofJoining
            if YearofJoining:
                employee.YearofJoining = YearofJoining
            if MonthofJoining:
                employee.MonthofJoining = MonthofJoining
            if MonthNameofJoining:
                employee.MonthNameofJoining = MonthNameofJoining
            if ShortMonth:
                employee.ShortMonth = ShortMonth
            if DayofJoining:
                employee.DayofJoining = DayofJoining
            if DOWofJoining:
                employee.DOWofJoining = DOWofJoining
            if ShortDOW:
                employee.ShortDOW = ShortDOW
            if AgeinCompanyinYears:
                employee.AgeinCompanyinYears = AgeinCompanyinYears
            if Salary:
                employee.Salary = Salary
            if LastHikePercentage:
                employee.LastHikePercentage = LastHikePercentage
            if SSN:
                employee.SSN = SSN
            if PhoneNo:
                employee.PhoneNo = PhoneNo
            if PlaceName:
                employee.PlaceName = PlaceName
            if County:
                employee.County = County
            if City:
                employee.City = City
            if State:
                employee.State = State
            if Zip:
                employee.Zip = Zip
            if Region:
                employee.Region = Region
            if Password:
                employee.Password = Password

            employee.save()
            emp_dict = dict_from_obj(employee)

            return_data = {
                'Success': True,
                'Status': 'Created Successfully',
                'Result': emp_dict
            }
            return make_response(jsonify(return_data), 200)

        else:
            return_data = {
                'Success': False,
                'Status': 'Update Failed',
                'Result': 'EmpId not exist'
            }
            return make_response(jsonify(return_data), 500)

    except Exception as e:
        return_data = {
            'Success': False,
            'Status': 'Aborted',
            'Result': 'Server Error'
        }
        return make_response(jsonify(return_data), 500)


@application.route('/get_employee/<id>', methods=['GET'])
@token_required
def get_employee(id):
    """
    method to get the details of an employee using employee id
    :param id: employee id for which the details required
    :return: checks whether employee exists or not by using employee id which is unique if exists
    then retrieves the employee details if not returns employee doesn't exists

    """
    try:
        employee = Employee.query.filter_by(EmpID=id).first()
        if employee:
            emp_dict = dict_from_obj(employee)

            return_data = {
                'Success': True,
                'Status': 'Fetched Successfully',
                'Result': emp_dict
            }
            return make_response(jsonify(return_data), 200)
        else:
            return_data = {
                'Success': False,
                'Status': 'Fetching Failed',
                'Result': 'EmpId not exist'
            }
            return make_response(jsonify(return_data), 500)
    except Exception as e:
        return_data = {
            'Success': False,
            'Status': 'Aborted',
            'Result': 'Server Error'
        }
        return make_response(jsonify(return_data), 500)


# Delete
@application.route('/delete_employee/<id>', methods=['DELETE'])
@token_required
def delete_employee(id):
    """
    method to delete an employee from database using employee id
    :param id: employee id of the employee of which the record should be deleted
    :return: checks whether employee exists or not by using employee id which is unique if exists
    then deletes that employee details if not returns employee doesn't exists

    """
    try:
        employee = Employee.query.filter_by(EmpID=id).first()
        if employee:
            emp_dict = dict_from_obj(employee)
            employee.remove()

            return_data = {
                'Success': True,
                'Status': 'Deleted Successfully',
                'Result': emp_dict
            }
            return make_response(jsonify(return_data), 200)
        else:
            return_data = {
                'Success': False,
                'Status': 'Deletion Failed',
                'Result': 'EmpId not exist'
            }
            return make_response(jsonify(return_data), 500)
    except Exception as e:
        return_data = {
            'Success': False,
            'Status': 'Aborted',
            'Result': 'Server Error'
        }
        return make_response(jsonify(return_data), 500)
