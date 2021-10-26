import subprocess as sp
import pymysql
import pymysql.cursors
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime


def CheckAadhar(aadhar_no):
    for c in aadhar_no:
        if c < '0' or c > '9':
            print("Failed to insert into database")
            print(
                ">>>>>>>>>>>>>Aadhar Number should only consist of digits(from 1 to 9)")
            return False
    if len(aadhar_no) != 12:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>Aadhar Number should only have 12 digits")
        return False
    return True


def CheckZipCode(zip_code):
    for c in zip_code:
        if c < '0' or c > '9':
            print("Failed to insert into database")
            print(
                ">>>>>>>>>>>>>Zip Code should only consist of digits(from 1 to 9)")
            return False
    if len(zip_code) > 6:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>Zip Code cannot have more than 6 digits")
        return False
    return True


def CheckCustomerStatus(customer_status):
    if customer_status == "Platinum":
        return True
    if customer_status == "Gold":
        return True
    if customer_status == "Silver":
        return True
    if customer_status == "Bronze":
        return True
    if customer_status == "Normal":
        return True
    else:
        return False


def CheckEmailID(email):
    pos_at = -1
    pos_dot = -1
    valid_email = True
    n = len(email)
    for i in range(n):
        if (email[i] == '@'):
            pos_at = i
        if (email[i] == '.' and pos_at != -1):
            if (i-pos_at) == 1:
                valid_email = False
            pos_dot = i
    if (email[0] == '@' or email[n-1] == '.' or pos_at == -1 or pos_dot == -1):
        valid_email = False
    return valid_email


def CheckContacts(number):
    for c in number:
        if not (c >= '0' and c <= '9') and c != '+' and c != '-':
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid character in the number %s", number)
            return False
    if len(number) < 7 or len(number) > 14:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>Invalid Contact Number format")
        return False
    return True


def GetAge(dob):
    pdob = parse(dob)
    if pdob > datetime.now():
        return -1
    age = relativedelta(datetime.now(), pdob).years
    return age


def CheckTPAId(tpaid):
    if len(tpaid) != 9:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>TPA id has format <first 4 numbers>-<second 4 numbers>")
        return False
    if tpaid[4] != '-':
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>TPA id has format <first 4 numbers>-<second 4 numbers>")
        return False
    for c in tpaid:
        if c == '-':
            continue
        if c < '0' or c > '9':
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>TPA id has format <first 4 numbers>-<second 4 numbers>")
            return False
    return True


def CheckPolicyId(policy_id):
    if len(policy_id) != 11:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>Policy id has format <first 4 numbers/alphabets>#<second 6 numbers>")
        return False
    if policy_id[4] != '#':
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>Policy id has format <first 4 numbers/alphabets>#<second 6 numbers>")
        return False
    for i in range(0, 4):
        if ((policy_id[i] < 'a' or policy_id[i] > 'z')
            and (policy_id[i] < 'A' or policy_id[i] > 'Z')
                and (policy_id[i] < '0' or policy_id[i] > '9')):
            print("Failed to insert into database")
            print(
                ">>>>>>>>>>>>>Policy id has format <first 4 numbers/alphabets>#<second 6 numbers>")
            return False
    for i in range(5, 11):
        if policy_id[i] < '0' or policy_id[i] > '9':
            print("Failed to insert into database")
            print(
                ">>>>>>>>>>>>>Policy id has format <first 4 numbers/alphabets>#<second 6 numbers>")
            return False
    return True


def AddCustomer():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new customer's details: ")
        row["aadhar_no"] = input("Aadhar Number: ")
        if not CheckAadhar(row["aadhar_no"]):
            return
        row["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        row["age"] = GetAge(row["date_of_birth"])
        if row["age"] == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]
        row["email_id"] = input("Email ID: ")
        if not CheckEmailID(row["email_id"]):
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Email id format")
            return
        row["customer_status"] = input(
            "Customer Status(Platinum, Gold, Silver, Bronze, Normal): ")
        if not CheckCustomerStatus(row["customer_status"]):
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Customer Status")
            return
        row["street_address"] = input("Street Address: ")
        row["zip_code"] = input("Zip Code: ")
        if not CheckZipCode(row["zip_code"]):
            return
        row["city"] = input("City: ")
        row["state"] = input("State: ")
        row["contacts"] = (
            input("Customer contact numbers (space seperated): ")).split(' ')

        query = "INSERT INTO Customer VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                row["aadhar_no"], row["date_of_birth"], row["first_name"], row["middle_name"], row["surname"],
                row["email_id"], row["customer_status"], row["street_address"], row["zip_code"], row["city"], row["state"])

        cur.execute(query)

        query = "INSERT INTO Customer_Age VALUES(%d, '%s')" % (
            row["age"], row["aadhar_no"])

        cur.execute(query)

        for number in row["contacts"]:
            if CheckContacts(number):
                query = "INSERT INTO Customer_Contact VALUES('%s', '%s')" % (
                    number, row["aadhar_no"])

                cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddCustomerDependant():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new customer dependant's details: ")
        row["aadhar_no"] = (
            input("Aadhar Numbers of the Customers they are dependant on: ")).split(' ')
        for number in row["aadhar_no"]:
            if not CheckAadhar(number):
                return
            query = "SELECT * FROM Customer WHERE aadhar_no = '%s'" % (number)
            cur.execute(query)
            if len(cur.fetchall()) == 0:
                print("Failed to insert into database")
                print(
                    ">>>>>>>>>>>>>Customer with Aadhar Number %s does not exist" % (number))
                return
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]
        row["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        row["age"] = GetAge(row["date_of_birth"])
        if row["age"] == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return

        query = "INSERT INTO Customer_Dependant VALUES('%s', '%s', '%s', '%s')" % (
                row["first_name"], row["middle_name"], row["surname"], row["date_of_birth"])

        cur.execute(query)

        query = "INSERT INTO Customer_Dependant_Age VALUES('%s', '%s', '%s', %d)" % (
                row["first_name"], row["middle_name"], row["surname"], row["age"])

        cur.execute(query)

        for number in row["aadhar_no"]:
            query = "INSERT INTO Depends_On VALUES('%s', '%s', '%s', '%s')" % (
                    row["first_name"], row["middle_name"], row["surname"], number)

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddEmployee():
    try:
        row = {}
        print("Enter new employee's details: ")
        row["dept_no"] = int(input("Department Number: "))
        row["sno"] = int(input("Serial Number: "))
        row["aadhar_no"] = input("Aadhar Number: ")
        if not CheckAadhar(row["aadhar_no"]):
            return
        row["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        row["age"] = GetAge(row["date_of_birth"])
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        if row["age"] == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]
        row["email_id"] = input("Email ID: ")
        if not CheckEmailID(row["email_id"]):
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Email id format")
            return
        row["street_address"] = input("Street Address: ")
        row["zip_code"] = input("Zip Code: ")
        if not CheckZipCode(row["zip_code"]):
            return
        row["city"] = input("City: ")
        row["state"] = input("State: ")
        row["contacts"] = (
            input("Employee contact numbers (space seperated): ")).split(' ')
        sdept_no = input(
            "Supervisor Department Number (Leave blank if no supervisor): ")
        ssno = input(
            "Supervisor Serial Number (Leave blank if no supervisor): ")
        if sdept_no == "":
            row["sdept_no"] = "NULL"
        else:
            flag = True
            for c in sdept_no:
                if c < '0' or c > '9':
                    flag = False
            if flag:
                row["sdept_no"] = sdept_no
            else:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>Invalid Supervisor Department Number")
                return
        if ssno == "":
            row["ssno"] = "NULL"
        else:
            flag = True
            for c in ssno:
                if c < '0' or c > '9':
                    flag = False
            if flag:
                row["ssno"] = ssno
            else:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>Invalid Supervisor Serial Number")
                return

        query = "INSERT INTO Employee VALUES(%d, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s)" % (
                row["dept_no"], row["sno"], row["aadhar_no"], row["date_of_birth"], row["first_name"], row["middle_name"], row["surname"],
                row["email_id"], row["street_address"], row["zip_code"], row["city"], row["state"], row["sdept_no"], row["ssno"])

        cur.execute(query)

        query = "INSERT INTO Employee_Age VALUES(%d, %d, %d)" % (
            row["age"], row["sno"], row["dept_no"])

        cur.execute(query)

        for number in row["contacts"]:
            if CheckContacts(number):
                query = "INSERT INTO Employee_Contact VALUES('%s', %d, %d)" % (
                    number, row["sno"], row["dept_no"])

                cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddEmployeeDependant():
    try:
        row = {}
        print("Enter new employee dependant's details: ")
        row["dept_no"] = (
            input("Department Numbers of the Employees who provide them: ")).split(' ')
        row["sno"] = (
            input("Serial Numbers of the Employees who provide them: ")).split(' ')
        if len(row["dept_no"]) != len(row["sno"]):
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Unequal number of Employees")
            return
        for i in range(len(row["sno"])):
            query = "SELECT * FROM Employee WHERE department_no = %d AND serial_no = %d" % (
                int(row["dept_no"][i]), int(row["sno"][i]))
            cur.execute(query)
            if len(cur.fetchall()) == 0:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>Employee with Department Number %d and Serial Number %d does not exist" % (
                    int(row["dept_no"][i]), int(row["sno"][i])))
                return
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]
        row["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        row["age"] = GetAge(row["date_of_birth"])
        if row["age"] == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return

        query = "INSERT INTO Employee_Dependant VALUES('%s', '%s', '%s', '%s')" % (
                row["first_name"], row["middle_name"], row["surname"], row["date_of_birth"])

        cur.execute(query)

        query = "INSERT INTO Employee_Dependant_Age VALUES(%d, '%s', '%s', '%s')" % (
                row["age"], row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)

        for i in range(len(row["sno"])):
            query = "INSERT INTO Provided_By VALUES(%d, %d, '%s', '%s', '%s')" % (
                    int(row["dept_no"][i]), int(row["sno"][i]), row["first_name"], row["middle_name"], row["surname"])

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddPolicy():
    try:
        row = {}
        print("Enter new policy's details: ")
        row["policy_id"] = input("Policy Id: ")
        if not CheckPolicyId(row["policy_id"]):
            return ""
        row["tnc"] = input(
            "Terms and Conditions (Put '-' to seperate between paragraphs): ")
        row["date_of_issue"] = input("Date of Issue (YYYY-MM-DD): ")
        if GetAge(row["date_of_issue"]) == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Issue")
            return ""
        row["duration"] = int(input("Duration in months: "))
        row["premium"] = float(input("Premium value: "))
        row["sum_assured"] = float(input("Sum assured: "))
        row["dept_no"] = int(
            input("Department Number of Employee issuing policy: "))
        row["sno"] = int(input("Serial Number of Employee issuing policy: "))
        row["aadhar_no"] = input("Aadhar Number of Customer buying policy: ")
        if not CheckAadhar(row["aadhar_no"]):
            return ""

        query = "INSERT INTO Policy VALUES('%s', '%s', '%s', %d, %f, %f, '%s', %d, %d)" % (
                row["policy_id"], row["tnc"], row["date_of_issue"], row["duration"],
                row["premium"], row["sum_assured"], row["aadhar_no"], row["dept_no"], row["sno"])

        cur.execute(query)

        con.commit()
        print("Inserted Into Database")
        return row["policy_id"]

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return ""


def AddLifeInsurance(policy_id):
    if policy_id == "":
        return
    try:
        row = {}
        row["dvb"] = float(input("Death Value Benefit Amount: "))
        row["history"] = input(
            "Medical History (Put '-' to seperate between paragraphs): ")
        row["beneficiaries"] = (
            input("Names of Beneficiaries (space seperated): ")).split(' ')

        query = "INSERT INTO Life VALUES('%s', %f, '%s')" % (
            policy_id, row["dvb"], row["history"])

        cur.execute(query)

        for name in row["beneficiaries"]:
            query = "INSERT INTO Beneficiaries VALUES('%s', '%s')" % (
                policy_id, name)

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddVehicleInsurance(policy_id):
    if policy_id == "":
        return
    try:
        row = {}
        row["license_plate_no"] = input("License Plate Number of Car: ")
        row["customer_license_no"] = input("License Number of Customer: ")
        row["colour"] = (input(
            "Colours of Car (space seperated, and use '-' where there is a space in name of colour): ")).split(' ')

        query = "INSERT INTO Vehicle VALUES('%s', '%s')" % (
            policy_id, row["license_plate_no"])

        cur.execute(query)

        query = "INSERT INTO Customer_License_No VALUES('%s', '%s')" % (
            policy_id, row["customer_license_no"])

        cur.execute(query)

        for col in row["colour"]:
            query = "INSERT INTO Vehicle_Colours VALUES('%s', '%s')" % (
                policy_id, col)

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddMedicalInsurance(policy_id):
    if policy_id == "":
        return
    try:
        row = {}
        row["dvb"] = float(input("Death Value Benefit Amount: "))
        row["cashless_hospitals"] = (input(
            "Cashless Hospitals (space seperated, and use '-' where there is a space in the name): ")).split(' ')
        row["condition"] = (input(
            "Medical conditions covered (space seperated, and use '-' where there is a space in name of condition): ")).split(' ')

        query = "INSERT INTO Medical VALUES('%s', %f)" % (
                policy_id, row["dvb"])

        cur.execute(query)

        for name in row["cashless_hospitals"]:
            query = "INSERT INTO Cashless_Hospitals VALUES('%s','%s')" % (
                policy_id, name)

            cur.execute(query)

        for name in row["condition"]:
            query = "INSERT INTO Conditions_Covered VALUES('%s','%s')" % (
                policy_id, name)

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddHouseInsurance(policy_id):
    if policy_id == "":
        return
    try:
        row = {}
        row["replacement_cost"] = float(input("Replacement Cost Value: "))
        row["street_address"] = input("Street Address: ")
        row["zip_code"] = input("Zip Code: ")
        if not CheckZipCode(row["zip_code"]):
            return
        row["city"] = input("City: ")
        row["state"] = input("State: ")

        query = "INSERT INTO House VALUES('%s', %f, '%s', '%s', '%s', '%s')" % (
                policy_id, row["replacement_cost"], row["street_address"], row["zip_code"], row["city"],
                row["state"])

        cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddTravelInsurance(policy_id):
    if policy_id == "":
        return
    try:
        row = {}
        row["itenerary"] = input("Iternerary: ")
        row["airline_and_hotel_bookings"] = input(
            "Airline and Hotel Details: ")
        row["destination"] = (input(
            "Travel Destinations (space seperated, and use '-' where there is a space in name of destination): ")).split(' ')

        query = "INSERT INTO Travel VALUES('%s', '%s', '%s')" % (
                policy_id, row["itenerary"], row["airline_and_hotel_bookings"])

        cur.execute(query)

        for dest in row["destination"]:
            query = "INSERT INTO Travel_Destinations VALUES('%s', '%s')" % (
                policy_id, dest)

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddTPA():
    try:
        row = {}
        print("Enter new TPA's details: ")
        row["TPA_id"] = input("TPA's Id: ")
        if not CheckTPAId(row["TPA_id"]):
            return
        row["TPA_name"] = input("TPA's Name: ")
        row["street_address"] = input("TPA's Street Address: ")
        row["zip_code"] = input("Zip code of TPA's Address: ")
        if not CheckZipCode(row["zip_code"]):
            return
        row["city"] = input("City of TPA's Address: ")
        row["state"] = input("State of TPA's Address: ")
        row["contact_number"] = (
            input("TPA's Contact Numbers (space seperated): ")).split(' ')
        row["type"] = (input(
            "TPA's Investigation Types (space seperated, and use '-' where there is a space in name of type): ")).split(' ')

        query = "INSERT INTO TPA VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
                row["TPA_id"], row["TPA_name"], row["street_address"], row["zip_code"], row["city"],
                row["state"])

        cur.execute(query)

        for number in row["contact_number"]:
            if CheckContacts(number):
                query = "INSERT INTO TPA_Contact_Info VALUES('%s', '%s')" % (
                    number, row["TPA_id"])

                cur.execute(query)

        for types in row["type"]:
            query = "INSERT INTO TPA_Investigations_Conducted VALUES('%s', '%s')" % (
                types, row["TPA_id"])

            cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def ResloveClaim():
    try:
        row = {}
        print("Enter claimed policy's details")
        row["TPA_id"] = input("Monitoring TPA's Id: ")
        if not CheckTPAId(row["TPA_id"]):
            return
        row["dept_no"] = int(
            input("Department Number of the Employee who issued the policy: "))
        row["sno"] = int(
            input("Serial Number of the Employee who issued the policy: "))
        row["policy_id"] = input("Id of the policy being claimed: ")
        if not CheckPolicyId(row["policy_id"]):
            return
        row["aadhar_no"] = input(
            "Aadhar Number of the customer who bought the policy being claimed: ")
        if not CheckAadhar(row["aadhar_no"]):
            return
        row["report"] = input(
            "Report On Policy claim (Put '-' to seperate between paragraphs): ")
        row["date_of_claim"] = input("Date of Claim (YYYY-MM-DD): ")
        if GetAge(row["date_of_claim"]) == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of claim")
            return

        query = "INSERT INTO Resolves_Claims VALUES('%s', %d, %d, '%s', '%s')" % (
                row["TPA_id"], row["dept_no"], row["sno"], row["policy_id"],
                row["aadhar_no"])

        cur.execute(query)

        query = "INSERT INTO Claim_Report VALUES('%s', '%s')" % (
                row["policy_id"], row["report"])

        cur.execute(query)

        query = "INSERT INTO Claim_Date VALUES('%s', '%s')" % (
                row["policy_id"], row["date_of_claim"])

        cur.execute(query)

        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def UpdateCustomerInfo():
    try:
        row = {}
        row["aadhar_no"] = input("Enter Aadhar Number of the Customer: ")

        query = "SELECT * FROM Customer WHERE aadhar_no = '%s'" % (
            row["aadhar_no"])

        cur.execute(query)
        record = cur.fetchall()

        print()

        if len(record) == 0:
            print("No customer with this Aadhar number found")
            return

        print("Enter Customer's updated details: ")
        row["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]
        row["email_id"] = input("Email ID: ")
        if not CheckEmailID(row["email_id"]):
            print("Failed to update database")
            print(">>>>>>>>>>>>>Invalid Email id format")
            return
        row["customer_status"] = input(
            "Customer Status(Platinum, Gold, Silver, Bronze, Normal): ")
        if not CheckCustomerStatus(row["customer_status"]):
            print("Failed to update database")
            print(">>>>>>>>>>>>>Invalid Customer Status")
            return
        row["street_address"] = input("Street Address: ")
        row["zip_code"] = input("Zip Code: ")
        if not CheckZipCode(row["zip_code"]):
            return
        row["city"] = input("City: ")
        row["state"] = input("State: ")
        row["contacts"] = (
            input("Customer contact numbers (space seperated): ")).split(' ')
        row["age"] = GetAge(row["date_of_birth"])
        if row["age"] == -1:
            print("Failed to update database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return

        query = "UPDATE Customer SET date_of_birth = '%s', first_name = '%s', middle_name = '%s', surname = '%s', email_id = '%s', customer_status = '%s', street_address = '%s', zip_code = '%s', city = '%s', state = '%s' WHERE aadhar_no = '%s'" % (
            row["date_of_birth"], row["first_name"], row["middle_name"], row["surname"], row["email_id"], row["customer_status"], row["street_address"], row["zip_code"], row["city"], row["state"], row["aadhar_no"])

        cur.execute(query)

        query = "UPDATE Customer_Age SET age = %d WHERE customer_aadhar_no = '%s' " % (
            row["age"], row["aadhar_no"])

        cur.execute(query)

        query = "DELETE FROM Customer_Contact WHERE customer_aadhar_no = '%s'" % (
            row["aadhar_no"])

        cur.execute(query)

        for number in row["contacts"]:
            if CheckContacts(number):
                query = "INSERT INTO Customer_Contact VALUES('%s', '%s')" % (
                    number, row["aadhar_no"])

                cur.execute(query)

        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def UpdateCustomerDependentInfo():
    try:
        row = {}
        print("Enter customer dependant's details: ")
        row["aadhar_no"] = (
            input("Aadhar Numbers of the Customer they are dependant on (space seperated): ")).split(" ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]

        record1 = {}
        f = 1
        for i in row["aadhar_no"]:
            query = "SELECT * from Depends_On WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s' AND customer_aadhar_no = '%s'" % (
                row["first_name"], row["middle_name"], row["surname"], i)

            cur.execute(query)
            record1 = cur.fetchall()
            if len(record1) == 0:
                f = 0

            print()

        query = "SELECT * from Customer_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        record2 = cur.fetchall()

        print()

        query = "SELECT * from Customer_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        record3 = cur.fetchall()

        print()

        if f == 0 or len(record2) == 0 or len(record3) == 0:
            print("No such record found")
            return

        info = {}
        info["aadhar_no"] = row["aadhar_no"]
        print("Enter updated Customer Dependant Information")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        info["first_name"] = name[0]
        info["middle_name"] = name[1]
        info["surname"] = name[2]
        info["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        info["age"] = GetAge(info["date_of_birth"])

        for i in row["aadhar_no"]:
            query = "DELETE FROM Depends_On WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s' AND customer_aadhar_no = '%s'" % (
                row["first_name"], row["middle_name"], row["surname"], i)

            cur.execute(query)
            print()

        query = "DELETE FROM Customer_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        print()

        query = "DELETE FROM Customer_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        print()

        query = "INSERT INTO Customer_Dependant VALUES('%s', '%s', '%s', '%s')" % (
            info["first_name"], info["middle_name"], info["surname"], info["date_of_birth"])

        cur.execute(query)
        print()

        query = "INSERT INTO Customer_Dependant_Age VALUES('%s', '%s', '%s', %d)" % (
            info["first_name"], info["middle_name"], info["surname"], info["age"])

        cur.execute(query)
        print()

        for i in row["aadhar_no"]:
            query = "INSERT INTO Depends_On VALUES('%s', '%s', '%s', '%s')" % (
                info["first_name"], info["middle_name"], info["surname"], i)

            cur.execute(query)
            print()

        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def UpdateEmployeeInfo():
    try:
        row = {}
        print("Enter employee's details: ")
        row["dept_no"] = int(input("Department Number: "))
        row["sno"] = int(input("Serial Number: "))

        query = "SELECT * from Employee WHERE department_no = %d AND serial_no = %d" % (
            row["dept_no"], row["sno"])

        cur.execute(query)
        record = cur.fetchall()

        print()

        if len(record) == 0:
            print("No employee with this department number and serial found")
            return

        print("Enter update Details")
        row["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]
        row["email_id"] = input("Email ID: ")
        if not CheckEmailID(row["email_id"]):
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Email id format")
            return
        row["street_address"] = input("Street Address: ")
        row["zip_code"] = input("Zip Code: ")
        if not CheckZipCode(row["zip_code"]):
            return
        row["city"] = input("City: ")
        row["state"] = input("State: ")
        row["contacts"] = (
            input("Employee contact numbers (space seperated): ")).split(' ')
        row["age"] = GetAge(row["date_of_birth"])
        if row["age"] == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return
        sdept_no = input(
            "Supervisor Department Number (Leave blank if no supervisor): ")
        ssno = input(
            "Supervisor Serial Number (Leave blank if no supervisor): ")
        if sdept_no == "":
            row["sdept_no"] = "NULL"
        else:
            flag = True
            for c in sdept_no:
                if c < '0' or c > '9':
                    flag = False
            if flag:
                row["sdept_no"] = sdept_no
            else:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>Invalid Supervisor Department Number")
                return
        if ssno == "":
            row["ssno"] = "NULL"
        else:
            flag = True
            for c in ssno:
                if c < '0' or c > '9':
                    flag = False
            if flag:
                row["ssno"] = ssno
            else:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>Invalid Supervisor Serial Number")
                return

        query = "UPDATE Employee SET date_of_birth = '%s', first_name = '%s', middle_name = '%s', surname = '%s', email_id = '%s', street_address = '%s', zip_code = '%s', city = '%s', state = '%s', sup_department_no = %s, sup_serial_no = %s WHERE department_no = %d AND serial_no = %d" % (
            row["date_of_birth"], row["first_name"], row["middle_name"], row["surname"], row["email_id"], row["street_address"], row["zip_code"], row["city"], row["state"], row["sdept_no"], row["ssno"], row["dept_no"], row["sno"])

        cur.execute(query)

        query = "UPDATE Employee_Age SET age = %d WHERE employee_serial_no = %d  AND employee_department_no = %d" % (
            row["age"], row["sno"], row["dept_no"])

        cur.execute(query)

        query = "DELETE FROM Employee_Contact WHERE employee_serial_no = %d  AND employee_department_no = %d" % (
            row["sno"], row["dept_no"])

        cur.execute(query)

        for number in row["contacts"]:
            if CheckContacts(number):
                query = "INSERT INTO Employee_Contact VALUES('%s', %d, %d)" % (
                    number, row["sno"], row["dept_no"])

                cur.execute(query)

        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def UpdateEmployeeDependantInfo():
    try:
        row = {}
        print("Enter employee dependant's details: ")
        row["dept_no"] = (
            input("Department Numbers of the Employees who provide them: ")).split(' ')
        row["sno"] = (
            input("Serial Numbers of the Employees who provide them: ")).split(' ')
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["first_name"] = name[0]
        row["middle_name"] = name[1]
        row["surname"] = name[2]

        record1 = {}
        f = 1
        for i in range(len(row["dept_no"])):
            query = "SELECT * from Provided_By WHERE employee_department_no = %d AND employee_serial_no = %d AND dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
                int(row["dept_no"][i]), int(row["sno"][i]), row["first_name"], row["middle_name"], row["surname"])

            cur.execute(query)
            record1 = cur.fetchall()
            if len(record1) == 0:
                f = 0
            print()

        query = "SELECT * from Employee_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        record2 = cur.fetchall()
        print()

        query = "SELECT * from Employee_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        record3 = cur.fetchall()
        print()

        if f == 0 or len(record2) == 0 or len(record3) == 0:
            print("No such record found")
            return

        info = {}
        info["sno"] = row["sno"]
        info["dept_no"] = row["dept_no"]
        print("Enter updated Employee Dependant Information")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        info["first_name"] = name[0]
        info["middle_name"] = name[1]
        info["surname"] = name[2]
        info["date_of_birth"] = input("Birth Date (YYYY-MM-DD): ")
        info["age"] = GetAge(info["date_of_birth"])
        if info["age"] == -1:
            print("Failed to update database")
            print(">>>>>>>>>>>>>Invalid Date of Birth")
            return

        for i in range(len(row["dept_no"])):
            query = "DELETE FROM Provided_By WHERE employee_department_no = %d AND employee_serial_no = %d AND dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
                int(row["dept_no"][i]), int(row["sno"][i]), row["first_name"], row["middle_name"], row["surname"])

            cur.execute(query)

        query = "DELETE FROM Employee_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        print()

        query = "DELETE FROM Employee_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
            row["first_name"], row["middle_name"], row["surname"])

        cur.execute(query)
        print()

        query = "INSERT INTO Employee_Dependant VALUES('%s', '%s', '%s', '%s')" % (
            info["first_name"], info["middle_name"], info["surname"], info["date_of_birth"])

        cur.execute(query)

        query = "INSERT INTO Employee_Dependant_Age VALUES(%d, '%s', '%s', '%s')" % (
            info["age"], info["first_name"], info["middle_name"], info["surname"])

        cur.execute(query)
        for i in range(len(row["sno"])):
            query = "INSERT INTO Provided_By VALUES(%d, %d, '%s', '%s', '%s')" % (int(info["dept_no"][i]), int(
                info["sno"][i]), info["first_name"], info["middle_name"], info["surname"])

            cur.execute(query)

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def UpdatePolicy():
    try:
        row = {}
        row["policy_id"] = input("Enter Policy Id: ")

        query = "SELECT * from Policy WHERE policy_id = '%s'" % (
            row["policy_id"])

        cur.execute(query)
        record = cur.fetchall()

        print()

        if len(record) == 0:
            print("No policy with this id found")
            return

        print("Enter new policy's details")
        row["tnc"] = input(
            "Terms and Conditions (Put '-' to seperate between paragraphs): ")
        row["date_of_issue"] = input("Date of Issue (YYYY-MM-DD): ")
        if GetAge(row["date_of_issue"]) == -1:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>Invalid Date of Issue")
            return
        row["duration"] = int(input("Duration in months: "))
        row["premium"] = float(input("Premium value: "))
        row["sum_assured"] = float(input("Sum assured: "))
        row["dept_no"] = int(
            input("Department Number of Employee issuing policy: "))
        row["sno"] = int(input("Serial Number of Employee issuing policy: "))
        row["aadhar_no"] = input("Aadhar Number of Customer buying policy: ")
        if not CheckAadhar(row["aadhar_no"]):
            return

        query = "UPDATE Policy SET terms_and_conditions = '%s', date_of_issue = '%s', durantion_in_months = %d, premium_value = %f, sum_assured = %f, customer_aadhar_no = '%s', employee_department_no = %d, employee_serial_no = %d WHERE policy_id = '%s'" % (
                row["tnc"], row["date_of_issue"], row["duration"], row["premium"], row["sum_assured"], row["aadhar_no"], row["dept_no"], row["sno"], row["policy_id"])

        cur.execute(query)

        query = "SELECT * FROM Life WHERE policy_id = '%s'" % (
            row["policy_id"])
        cur.execute(query)
        lifet = cur.fetchall()
        query = "SELECT * FROM Medical WHERE policy_id = '%s'" % (
            row["policy_id"])
        cur.execute(query)
        medt = cur.fetchall()
        query = "SELECT * FROM Vehicle WHERE policy_id = '%s'" % (
            row["policy_id"])
        cur.execute(query)
        veht = cur.fetchall()
        query = "SELECT * FROM House WHERE policy_id = '%s'" % (
            row["policy_id"])
        cur.execute(query)
        hset = cur.fetchall()
        query = "SELECT * FROM Travel WHERE policy_id = '%s'" % (
            row["policy_id"])
        cur.execute(query)
        trat = cur.fetchall()
        if len(lifet) > 0:
            query = "DELETE FROM Beneficiaries WHERE policy_id = '%s'" % (
                row["policy_id"])
            cur.execute(query)
            print("Enter new Life Insurance policy's details")
            row["dvb"] = float(input("Death Value Benefit Amount: "))
            row["history"] = input(
                "Medical History (Put '-' to seperate between paragraphs): ")
            row["beneficiaries"] = (
                input("Names of Beneficiaries (space seperated): ")).split(' ')

            query = "UPDATE Life SET death_value_benefit = %f, medical_history = '%s' WHERE policy_id = '%s'" % (
                row["dvb"], row["history"], row["policy_id"])

            cur.execute(query)

            for name in row["beneficiaries"]:
                query = "INSERT INTO Beneficiaries VALUES('%s', '%s')" % (
                    row["policy_id"], name)

                cur.execute(query)
        elif len(medt) > 0:
            query = "DELETE FROM Cashless_Hospitals WHERE policy_id = '%s'" % (
                row["policy_id"])
            cur.execute(query)
            query = "DELETE FROM Conditions_Covered WHERE policy_id = '%s'" % (
                row["policy_id"])
            cur.execute(query)
            print("Enter new Medical Insurance policy's details")
            row["dvb"] = float(input("Death Value Benefit Amount: "))
            row["cashless_hospitals"] = (input(
                "Cashless Hospitals (space seperated, and use '-' where there is a space in the name): ")).split(' ')
            row["condition"] = (input(
                "Medical conditions covered (space seperated, and use '-' where there is a space in name of condition): ")).split(' ')

            query = "UPDATE Medical SET death_value_benefit = %f WHERE policy_id = '%s'" % (
                    row["dvb"], row["policy_id"])

            cur.execute(query)

            for name in row["cashless_hospitals"]:
                query = "INSERT INTO Cashless_Hospitals VALUES('%s','%s')" % (
                    row["policy_id"], name)

                cur.execute(query)

            for name in row["condition"]:
                query = "INSERT INTO Conditions_Covered VALUES('%s','%s')" % (
                    row["policy_id"], name)

                cur.execute(query)
        elif len(veht) > 0:
            query = "DELETE FROM Vehicle_Colours WHERE policy_id = '%s'" % (
                row["policy_id"])
            cur.execute(query)
            print("Enter new Vehicle Insurance policy's details")
            row["license_plate_no"] = input("License Plate Number of Car: ")
            row["customer_license_no"] = input("License Number of Customer: ")
            row["colour"] = (input(
                "Colours of Car (space seperated, and use '-' where there is a space in name of colour): ")).split(' ')

            query = "UPDATE Vehicle SET license_plate_no = '%s' WHERE policy_id = '%s'" % (
                row["license_plate_no"], row["policy_id"])

            cur.execute(query)

            query = "UPDATE Customer_License_No SET customer_license_no = '%s' WHERE policy_id = '%s'" % (
                row["customer_license_no"], row["policy_id"])

            cur.execute(query)

            for col in row["colour"]:
                query = "INSERT INTO Vehicle_Colours VALUES('%s', '%s')" % (
                    row["policy_id"], col)

                cur.execute(query)
        elif len(hset) > 0:
            print("Enter new House Insurance policy's details")
            row["replacement_cost"] = float(input("Replacement Cost Value: "))
            row["street_address"] = input("Street Address: ")
            row["zip_code"] = input("Zip Code: ")
            if not CheckZipCode(row["zip_code"]):
                return
            row["city"] = input("City: ")
            row["state"] = input("State: ")

            query = "UPDATE House SET replacement_cost = %f, street_address = '%s', zip_code = '%s', city = '%s', state = '%s' WHERE policy_id = '%s'" % (
                    row["replacement_cost"], row["street_address"], row["zip_code"], row["city"], row["state"], row["policy_id"])

            cur.execute(query)
        elif len(trat) > 0:
            query = "DELETE FROM Travel_Destinations WHERE policy_id = '%s'" % (
                row["policy_id"])
            cur.execute(query)
            print("Enter new Travel Insurance policy's details")
            row["itenerary"] = input("Iternerary: ")
            row["airline_and_hotel_bookings"] = input(
                "Airline and Hotel Details: ")
            row["destination"] = (input(
                "Travel Destinations (space seperated, and use '-' where there is a space in name of destination): ")).split(' ')

            query = "UPDATE Travel SET itenerary = '%s', airline_and_hotel_bookings = '%s' WHERE policy_id = '%s'" % (
                    row["itenerary"], row["airline_and_hotel_bookings"], row["policy_id"])

            cur.execute(query)

            for dest in row["destination"]:
                query = "INSERT INTO Travel_Destinations VALUES('%s', '%s')" % (
                    row["policy_id"], dest)

                cur.execute(query)
        else:
            print(">>>>>>>>>>>>>Policy with id %s not of any type" %
                  (row["policy_id"]))
            return

        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return

def UpdateTPAinfo():
    try:
        row = {}
        print("Enter the TPA's details: ")
        row["TPA_id"] = input("TPA's Id: ")
        if not CheckTPAId(row["TPA_id"]):
            return

        query = "SELECT * from TPA WHERE TPA_id = '%s'" % (row["TPA_id"])
         
        cur.execute(query)
        record = cur.fetchall()
        print()

        info = {}
        if len(record) == 0:
            print("No employee with this department number and serial found")
            return

        info["TPA_id"] = row["TPA_id"]
        info["TPA_name"] = input("TPA's Name: ")
        info["street_address"] = input("TPA's Street Address: ")
        info["zip_code"] = input("Zip code of TPA's Address: ")
        if not CheckZipCode(info["zip_code"]):
            return
        info["city"] = input("City of TPA's Address: ")
        info["state"] = input("State of TPA's Address: ")
        info["contact_number"] = (
            input("TPA's Contact Numbers (space seperated): ")).split(' ')
        info["type"] = (input(
            "TPA's Investigation Types (space seperated, and use '-' where there is a space in name of type): ")).split(' ')

        query = "UPDATE TPA SET TPA_name = '%s', street_address = '%s' ,zip_code = '%s', city = '%s', state = '%s' WHERE TPA_id = '%s'" % (
            info["TPA_name"], info["street_address"], info["zip_code"], info["city"], info["state"], info["TPA_id"])
        cur.execute(query)

        query = "DELETE FROM TPA_Contact_Info WHERE TPA_id = '%s'" % (
            info["TPA_id"])
        cur.execute(query)

        for number in info["contact_number"]:
            if CheckContacts(number):
                query = "INSERT INTO TPA_Contact_Info VALUES('%s', '%s')" % (
                    number, info["TPA_id"])
                 
                cur.execute(query)

        query = "DELETE FROM TPA_Investigations_Conducted WHERE TPA_id = '%s'" % (
            info["TPA_id"])
        cur.execute(query)

        for types in info["type"]:
            query = "INSERT INTO TPA_Investigations_Conducted VALUES('%s', '%s')" % (
                types, info["TPA_id"])
             
            cur.execute(query)

        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def DeletePolicy(policy_id):
    try:
        if policy_id == "":
            policy_id = input("Enter Id of the policy you want to delete: ")
            if not CheckPolicyId(policy_id):
                return
        query = "DELETE FROM Beneficiaries WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Cashless_Hospitals WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Conditions_Covered WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Customer_License_No WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Vehicle_Colours WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Travel_Destinations WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Claim_Date WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Claim_Report WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Life WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Medical WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Vehicle WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM House WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Travel WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Resolves_Claims WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)
        query = "DELETE FROM Policy WHERE policy_id = '%s'" % (
            policy_id)
        cur.execute(query)

        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def DeleteCustomerDependant(fname, mname, lname):
    try:
        if fname == None and mname == None and lname == None:
            name = (
                input("Name of Dependant to Delete (Fname Minit Lname): ")).split(' ')
            fname = name[0]
            mname = name[1]
            lname = name[2]
        query = "DELETE FROM Customer_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            fname, mname, lname)
        cur.execute(query)
        query = "DELETE FROM Depends_On WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            fname, mname, lname)
        cur.execute(query)
        query = "DELETE FROM Customer_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
            fname, mname, lname)
        cur.execute(query)

        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def DeleteEmployeeDependant(fname, mname, lname):
    try:
        if fname == None and mname == None and lname == None:
            name = (
                input("Name of Dependant to Delete (Fname Minit Lname): ")).split(' ')
            fname = name[0]
            mname = name[1]
            lname = name[2]
        query = "DELETE FROM Employee_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            fname, mname, lname)
        cur.execute(query)
        query = "DELETE FROM Provided_By WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
            fname, mname, lname)
        cur.execute(query)
        query = "DELETE FROM Employee_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
            fname, mname, lname)
        cur.execute(query)

        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def DeleteCustomer():
    try:
        aadhar_no = input(
            "Enter Aadhar Number of the Customer you want to delete: ")
        if not CheckAadhar(aadhar_no):
            return
        query = "SELECT * FROM Policy WHERE customer_aadhar_no = '%s'" % (
            aadhar_no)
        cur.execute(query)
        result = cur.fetchall()
        for line in result:
            DeletePolicy(line["policy_id"])
        query = "DELETE FROM Customer_Age WHERE customer_aadhar_no = '%s'" % (
            aadhar_no)
        cur.execute(query)
        query = "DELETE FROM Customer_Contact WHERE customer_aadhar_no = '%s'" % (
            aadhar_no)
        cur.execute(query)
        query = "SELECT * FROM Depends_On WHERE customer_aadhar_no = '%s'" % (
            aadhar_no)
        cur.execute(query)
        result = cur.fetchall()
        query = "DELETE FROM Depends_On WHERE customer_aadhar_no = '%s'" % (
            aadhar_no)
        cur.execute(query)
        for line in result:
            query = "SELECT * FROM Depends_On WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
                line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
            cur.execute(query)
            temp = cur.fetchall()
            if len(temp) == 0:
                DeleteCustomerDependant(
                    line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
        query = "DELETE FROM Customer WHERE aadhar_no = '%s'" % (
            aadhar_no)
        cur.execute(query)

        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def DeleteEmployee():
    try:
        dno = int(input(
            "Enter Department Number of the Employee you want to delete: "))
        sno = int(input(
            "Enter Serial Number of the Employee you want to delete: "))
        query = "SELECT * FROM Policy WHERE employee_department_no = %d AND employee_serial_no = %d" % (
            dno, sno)
        cur.execute(query)
        result = cur.fetchall()
        for line in result:
            DeletePolicy(line["policy_id"])
        query = "DELETE FROM Employee_Age WHERE employee_department_no = %d AND employee_serial_no = %d" % (
            dno, sno)
        cur.execute(query)
        query = "DELETE FROM Employee_Contact WHERE employee_department_no = %d AND employee_serial_no = %d" % (
            dno, sno)
        cur.execute(query)
        query = "SELECT * FROM Provided_By WHERE employee_department_no = %d AND employee_serial_no = %d" % (
            dno, sno)
        cur.execute(query)
        result = cur.fetchall()
        query = "DELETE FROM Provided_By WHERE employee_department_no = %d AND employee_serial_no = %d" % (
            dno, sno)
        cur.execute(query)
        for line in result:
            query = "SELECT * FROM Provided_By WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
                line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
            cur.execute(query)
            temp = cur.fetchall()
            if len(temp) == 0:
                DeleteEmployeeDependant(
                    line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
        query = "SELECT * FROM Employee WHERE sup_department_no = %d AND sup_serial_no = %d" % (
            dno, sno)
        cur.execute(query)
        result = cur.fetchall()
        for line in result:
            query = "UPDATE Employee SET sup_department_no = NULL, sup_serial_no = NULL WHERE department_no = %d AND serial_no = %d" % (
                line["department_no"], line["serial_no"])
            cur.execute(query)
        query = "DELETE FROM Employee WHERE department_no = %d AND serial_no = %d" % (
            dno, sno)
        cur.execute(query)

        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def DeleteTPA():
    try:
        tpaid = input(
            "Enter Id of the Third Part Administrator you want to delete: ")
        if not CheckTPAId(tpaid):
            return
        query = "SELECT * FROM Resolves_Claims WHERE TPA_id = '%s'" % (
            tpaid)
        cur.execute(query)
        result = cur.fetchall()
        for line in result:
            DeletePolicy(line["policy_id"])
        query = "DELETE FROM TPA_Contact_Info WHERE TPA_id = '%s'" % (
            tpaid)
        cur.execute(query)
        query = "DELETE FROM TPA_Investigations_Conducted WHERE TPA_id = '%s'" % (
            tpaid)
        cur.execute(query)
        query = "DELETE FROM TPA WHERE TPA_id = '%s'" % (
            tpaid)
        cur.execute(query)

        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetAllCustomers():
    try:
        row = {}
        print("Enter customer's status: ")
        row["customer_status"] = input(
            "Customer Status(Platinum, Gold, Silver, Bronze, Normal): ")

        query = "SELECT * FROM Customer WHERE customer_status = '%s'" % (
            row["customer_status"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            cnums = []
            age = 0
            query = "SELECT * FROM Customer_Contact WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums.append(x["contact_number"])
            query = "SELECT * FROM Customer_Age WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                age = x["age"]
                break
            print("%d:" % (cntr))
            print("Aadhar Number: ", line["aadhar_no"])
            print("Name: %s %s %s" %
                  (line["first_name"], line["middle_name"], line["surname"]))
            print("Date of Birth: ", line["date_of_birth"])
            print("Age: ", age)
            print("Email id: ", line["email_id"])
            print("Contact Numbers: ", cnums)
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetAllPoliciesOfCustomers():
    try:
        row = {}
        print("Enter customer's Aadhar Number: ")
        row["aadhar_no"] = input("Aadhar number: ")

        query = "SELECT * FROM Policy WHERE customer_aadhar_no = '%s'" % (
            row["aadhar_no"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            top = 0
            query = "SELECT * FROM Life WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            lifet = cur.fetchall()

            query = "SELECT * FROM Medical WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            medt = cur.fetchall()

            query = "SELECT * FROM Vehicle WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            veht = cur.fetchall()

            query = "SELECT * FROM House WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            hset = cur.fetchall()

            query = "SELECT * FROM Travel WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            trat = cur.fetchall()

            life = {}
            med = {}
            vehicle = {}
            house = {}
            travel = {}
            if len(lifet) > 0:
                for x in lifet:
                    life = x.copy()
                    break
                top = 1
            elif len(medt) > 0:
                for x in medt:
                    med = x.copy()
                    break
                top = 2
            elif len(veht) > 0:
                for x in veht:
                    vehicle = x.copy()
                    break
                top = 3
            elif len(hset) > 0:
                for x in hset:
                    house = x.copy()
                    break
                top = 4
            elif len(trat) > 0:
                for x in trat:
                    travel = x.copy()
                    break
                top = 5
            if top == 0:
                print("Failed to retrieve from database")
                print(">>>>>>>>>>>>>Policy with id %s not of any type" %
                      (line["policy_id"]))
                continue
            print("%d:" % (cntr))
            print("Policy id: ", line["policy_id"])
            print("Terms and Conditions")
            tnc = line["terms_and_conditions"].split('-')
            for s in tnc:
                print(s)
            print("Date of Issue: ", line["date_of_issue"])
            print("Duration: %d months" % (line["durantion_in_months"]))
            print("Premium: ", line["premium_value"])
            print("Sum assured: ", line["sum_assured"])
            print("Department number of issuing employee: ",
                  line["employee_department_no"])
            print("Serial number of issuing employee: ",
                  line["employee_serial_no"])
            if top == 1:
                query = "SELECT * FROM Beneficiaries WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                ben = cur.fetchall()

                names = ""
                for x in ben:
                    names += (", %s" % (x["name_of_beneficiary"]))
                print("Death Value Benefit: ", life["death_value_benefit"])
                print("Medical History of Customer: ")
                mh = life["medical_history"].split('-')
                for s in mh:
                    print("\t", s)
                if len(names) > 0:
                    print("Names of beneficiaries of Customer: ", names[2:])
                else:
                    print(
                        "Names of beneficiaries of Customer: No beneficiaries mentioned")
            elif top == 2:
                query = "SELECT * FROM Conditions_Covered WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                cond = cur.fetchall()

                cond_names = ""
                for x in cond:
                    words = x["name_of_condition"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    cond_names += (", %s" % (s))
                query = "SELECT * FROM Cashless_Hospitals WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                hosp = cur.fetchall()

                hosp_names = ""
                for x in hosp:
                    words = x["name_of_hospital"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    hosp_names += (", %s" % (s))
                print("Death Value Benefit: ", med["death_value_benefit"])
                if len(cond_names) > 0:
                    print("Conditions Covered by Policy: ", cond_names[2:])
                else:
                    print("Conditions Covered by Policy: No conditions mentioned")
                if len(hosp_names) > 0:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: ", hosp_names[2:])
                else:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: No hospitals mentioned")
            elif top == 3:
                query = "SELECT * FROM Vehicle_Colours WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                colt = cur.fetchall()

                col_names = ""
                for x in colt:
                    words = x["colour"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    col_names += (", %s" % (s))
                query = "SELECT * FROM Customer_License_No WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                lnt = cur.fetchall()

                ln = ""
                for x in lnt:
                    ln = x["customer_license_no"]
                    break
                print("License Plate Number: ", vehicle["license_plate_no"])
                if len(col_names) > 0:
                    print("Colours of Vehicle: ", col_names[2:])
                else:
                    print("Colours of Vehicle: No colours mentioned")
                print("Customer License Number: ", ln)
            elif top == 4:
                print("Replacement Cost of House: ", house["replacement_cost"])
                print("House Address: %s, %s-%s, %s" %
                      (house["street_address"], house["city"], house["zip_code"], house["state"]))
            elif top == 5:
                query = "SELECT * FROM Travel_Destinations WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                destt = cur.fetchall()

                dest_names = ""
                for x in destt:
                    words = x["destination"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    dest_names += (", %s" % (s))
                print("Itenerary of Travel: ", travel["itenerary"])
                print("Airline and Hotel Booking of Travel: ",
                      travel["airline_and_hotel_bookings"])
                if len(dest_names) > 0:
                    print("Travel Destinations: ", dest_names[2:])
                else:
                    print("Travel Destinations: No destinations mentioned")
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetAllDependentsOfCustomers():
    try:
        row = {}
        print("Enter customer's Aadhar Number")
        row["aadhar_number"] = input("Aadhar Number of Customer: ")

        query = "SELECT * FROM Depends_On WHERE customer_aadhar_no = '%s'" % (
            row["aadhar_number"])

        cur.execute(query)
        dependants = cur.fetchall()

        print()

        cntr = 1
        for line in dependants:
            query = "SELECT * FROM Customer_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
                line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
            cur.execute(query)
            dept = cur.fetchall()

            query = "SELECT * FROM Customer_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
                line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
            cur.execute(query)
            depaget = cur.fetchall()

            dep = {}
            age = 0
            for x in dept:
                dep = x.copy()
                break
            for x in depaget:
                age = x["age"]
                break
            print("%d:" % (cntr))
            print("Name: %s %s %s" %
                  (dep["first_name"], dep["middle_name"], dep["surname"]))
            print("Date of Birth: ", dep["date_of_birth"])
            print("Age: ", age)
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetAllDependentsOfEmployee():
    try:
        row = {}
        print("Enter employee's Info")
        row["dept_no"] = int(
            input("Department Number of the Employee: "))
        row["sno"] = int(
            input("Serial Number of the Employee: "))

        query = "SELECT * FROM Provided_By WHERE employee_department_no = %d AND employee_serial_no = %d" % (
            row["dept_no"], row["sno"])

        cur.execute(query)
        dependants = cur.fetchall()

        print()

        cntr = 1
        for line in dependants:
            query = "SELECT * FROM Employee_Dependant WHERE first_name = '%s' AND middle_name = '%s' AND surname = '%s'" % (
                line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
            cur.execute(query)
            dept = cur.fetchall()

            query = "SELECT * FROM Employee_Dependant_Age WHERE dependant_first_name = '%s' AND dependant_middle_name = '%s' AND dependant_surname = '%s'" % (
                line["dependant_first_name"], line["dependant_middle_name"], line["dependant_surname"])
            cur.execute(query)
            depaget = cur.fetchall()

            dep = {}
            age = 0
            for x in dept:
                dep = x.copy()
                break
            for x in depaget:
                age = x["age"]
                break
            print("%d:" % (cntr))
            print("Name: %s %s %s" %
                  (dep["first_name"], dep["middle_name"], dep["surname"]))
            print("Date of Birth: ", dep["date_of_birth"])
            print("Age: ", age)
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetAllTPAsInCity():
    try:
        row = {}
        print("Enter TPA's info")
        row["city"] = input("City (Case sensitive): ")

        query = "SELECT * FROM TPA WHERE city = '%s'" % (row["city"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            cnums = ""
            types = ""
            query = "SELECT * FROM TPA_Contact_Info WHERE TPA_id = '%s'" % (
                line["TPA_id"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums += ", "
                cnums += x["contact_number"]
            query = "SELECT * FROM TPA_Investigations_Conducted WHERE TPA_id = '%s'" % (
                line["TPA_id"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                types += ", "
                types += x["type"]
            print("%d:" % (cntr))
            print("TPA Id: ", line["TPA_id"])
            print("Name: ", line["TPA_name"])
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            if len(cnums) > 0:
                print("Contact Numbers: ", cnums[2:])
            else:
                print("Contact Numbers: No numbers mentioned")
            if len(types) > 0:
                print("Types of Investigations Conducted: ", types[2:])
            else:
                print("Types of Investigations Conducted: No types mentioned")
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetInsurancePolicies():
    try:
        row = {}
        print("Enter policy types (Life, Medical, Vehicle, House, Travel)")
        row["subclass"] = (
            input("Policy types (space seperated and case sensitive): ")).split(' ')
        policy_ids = set()
        for sub in row["subclass"]:
            result = tuple()
            if sub == "Life":
                query = "SELECT policy_id FROM Life"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Medical":
                query = "SELECT policy_id FROM Medical"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Vehicle":
                query = "SELECT policy_id FROM Vehicle"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "House":
                query = "SELECT policy_id FROM House"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Travel":
                query = "SELECT policy_id FROM Travel"
                cur.execute(query)
                result = cur.fetchall()

            else:
                print(">>>>>>>>>>>>>Invalid type of policy")
            for line in result:
                policy_ids.add(line["policy_id"])

        print()

        cntr = 1
        for pid in policy_ids:
            query = "SELECT * FROM Policy WHERE policy_id = '%s'" % (pid)
            cur.execute(query)
            result = cur.fetchall()
            line = {}

            for x in result:
                line = x.copy()
                break
            top = 0
            query = "SELECT * FROM Life WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            lifet = cur.fetchall()

            query = "SELECT * FROM Medical WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            medt = cur.fetchall()

            query = "SELECT * FROM Vehicle WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            veht = cur.fetchall()

            query = "SELECT * FROM House WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            hset = cur.fetchall()

            query = "SELECT * FROM Travel WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            trat = cur.fetchall()

            life = {}
            med = {}
            vehicle = {}
            house = {}
            travel = {}
            if len(lifet) > 0:
                for x in lifet:
                    life = x.copy()
                    break
                top = 1
            elif len(medt) > 0:
                for x in medt:
                    med = x.copy()
                    break
                top = 2
            elif len(veht) > 0:
                for x in veht:
                    vehicle = x.copy()
                    break
                top = 3
            elif len(hset) > 0:
                for x in hset:
                    house = x.copy()
                    break
                top = 4
            elif len(trat) > 0:
                for x in trat:
                    travel = x.copy()
                    break
                top = 5
            if top == 0:
                print("Failed to retrieve from database")
                print(">>>>>>>>>>>>>Policy with id %s not of any type" %
                      (line["policy_id"]))
                continue
            print("%d:" % (cntr))
            print("Policy id: ", line["policy_id"])
            print("Terms and Conditions")
            tnc = line["terms_and_conditions"].split('-')
            for s in tnc:
                print(s)
            print("Date of Issue: ", line["date_of_issue"])
            print("Duration: %d months" % (line["durantion_in_months"]))
            print("Premium: ", line["premium_value"])
            print("Sum assured: ", line["sum_assured"])
            print("Department number of issuing employee: ",
                  line["employee_department_no"])
            print("Serial number of issuing employee: ",
                  line["employee_serial_no"])
            if top == 1:
                query = "SELECT * FROM Beneficiaries WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                ben = cur.fetchall()

                names = ""
                for x in ben:
                    names += (", %s" % (x["name_of_beneficiary"]))
                print("Death Value Benefit: ", life["death_value_benefit"])
                print("Medical History of Customer: ")
                mh = life["medical_history"].split('-')
                for s in mh:
                    print("\t", s)
                if len(names) > 0:
                    print("Names of beneficiaries of Customer: ", names[2:])
                else:
                    print(
                        "Names of beneficiaries of Customer: No beneficiaries mentioned")
            elif top == 2:
                query = "SELECT * FROM Conditions_Covered WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                cond = cur.fetchall()

                cond_names = ""
                for x in cond:
                    words = x["name_of_condition"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    cond_names += (", %s" % (s))
                query = "SELECT * FROM Cashless_Hospitals WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                hosp = cur.fetchall()

                hosp_names = ""
                for x in hosp:
                    words = x["name_of_hospital"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    hosp_names += (", %s" % (s))
                print("Death Value Benefit: ", med["death_value_benefit"])
                if len(cond_names) > 0:
                    print("Conditions Covered by Policy: ", cond_names[2:])
                else:
                    print("Conditions Covered by Policy: No conditions mentioned")
                if len(hosp_names) > 0:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: ", hosp_names[2:])
                else:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: No hospitals mentioned")
            elif top == 3:
                query = "SELECT * FROM Vehicle_Colours WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                colt = cur.fetchall()

                col_names = ""
                for x in colt:
                    words = x["colour"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    col_names += (", %s" % (s))
                query = "SELECT * FROM Customer_License_No WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                lnt = cur.fetchall()

                ln = ""
                for x in lnt:
                    ln = x["customer_license_no"]
                    break
                print("License Plate Number: ", vehicle["license_plate_no"])
                if len(col_names) > 0:
                    print("Colours of Vehicle: ", col_names[2:])
                else:
                    print("Colours of Vehicle: No colours mentioned")
                print("Customer License Number: ", ln)
            elif top == 4:
                print("Replacement Cost of House: ", house["replacement_cost"])
                print("House Address: %s, %s-%s, %s" %
                      (house["street_address"], house["city"], house["zip_code"], house["state"]))
            elif top == 5:
                query = "SELECT * FROM Travel_Destinations WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                destt = cur.fetchall()

                dest_names = ""
                for x in destt:
                    words = x["destination"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    dest_names += (", %s" % (s))
                print("Itenerary of Travel: ", travel["itenerary"])
                print("Airline and Hotel Booking of Travel: ",
                      travel["airline_and_hotel_bookings"])
                if len(dest_names) > 0:
                    print("Travel Destinations: ", dest_names[2:])
                else:
                    print("Travel Destinations: No destinations mentioned")
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetInsuranceCustomers():
    try:
        row = {}
        print("Enter policy types and status")
        print("Policy types - Life, Medical, Vehicle, House, Travel")
        print("Status - Platinum, Gold, Silver, Bronze, Normal")
        row["subclass"] = (
            input("Policy types (space seperated and case sensitive): ")).split(' ')
        row["status"] = (
            input("Status (space seperated and case sensitive): ")).split(' ')
        for stat in row["status"]:
            if not CheckCustomerStatus(stat):
                print(">>>>>>>>>>>>>%s is not a valid Customer status" % (stat))
        policy_ids = set()
        for sub in row["subclass"]:
            result = tuple()
            if sub == "Life":
                query = "SELECT policy_id FROM Life"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Medical":
                query = "SELECT policy_id FROM Medical"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Vehicle":
                query = "SELECT policy_id FROM Vehicle"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "House":
                query = "SELECT policy_id FROM House"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Travel":
                query = "SELECT policy_id FROM Travel"
                cur.execute(query)
                result = cur.fetchall()

            else:
                print(">>>>>>>>>>>>>Invalid type of policy")
            for line in result:
                policy_ids.add(line["policy_id"])

        aadhar_nos = set()
        for pid in policy_ids:
            query = "SELECT * FROM Policy WHERE policy_id = '%s'" % (pid)
            cur.execute(query)
            result = cur.fetchall()
            line = {}

            for x in result:
                line = x.copy()
                break
            no = line["customer_aadhar_no"]
            query = "SELECT * FROM Customer WHERE aadhar_no = '%s'" % (no)
            cur.execute(query)
            result = cur.fetchall()
            line = {}

            for x in result:
                line = x.copy()
                break
            if line["customer_status"] in row["status"]:
                aadhar_nos.add(no)

        print()

        cntr = 1
        for no in aadhar_nos:
            query = "SELECT * FROM Customer WHERE aadhar_no = '%s'" % (no)
            cur.execute(query)
            result = cur.fetchall()
            line = {}

            for x in result:
                line = x.copy()
                break
            cnums = []
            age = 0
            query = "SELECT * FROM Customer_Contact WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums.append(x["contact_number"])
            query = "SELECT * FROM Customer_Age WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                age = x["age"]
                break
            print("%d:" % (cntr))
            print("Aadhar Number: ", line["aadhar_no"])
            print("Name: %s %s %s" %
                  (line["first_name"], line["middle_name"], line["surname"]))
            print("Date of Birth: ", line["date_of_birth"])
            print("Age: ", age)
            print("Email id: ", line["email_id"])
            print("Contact Numbers: ", cnums)
            print("Customer Status: ", line["customer_status"])
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetPoliciesWithPremium():
    try:
        row = {}
        print("Enter Range for Premium")
        row["min"] = float(input("Minimum Premium: "))
        row["max"] = float(input("Maximum Premium: "))

        query = "SELECT * FROM Policy WHERE premium_value <= %f AND premium_value >= %f" % (
            row["max"], row["min"])
        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            top = 0
            query = "SELECT * FROM Life WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            lifet = cur.fetchall()

            query = "SELECT * FROM Medical WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            medt = cur.fetchall()

            query = "SELECT * FROM Vehicle WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            veht = cur.fetchall()

            query = "SELECT * FROM House WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            hset = cur.fetchall()

            query = "SELECT * FROM Travel WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            trat = cur.fetchall()

            life = {}
            med = {}
            vehicle = {}
            house = {}
            travel = {}
            if len(lifet) > 0:
                for x in lifet:
                    life = x.copy()
                    break
                top = 1
            elif len(medt) > 0:
                for x in medt:
                    med = x.copy()
                    break
                top = 2
            elif len(veht) > 0:
                for x in veht:
                    vehicle = x.copy()
                    break
                top = 3
            elif len(hset) > 0:
                for x in hset:
                    house = x.copy()
                    break
                top = 4
            elif len(trat) > 0:
                for x in trat:
                    travel = x.copy()
                    break
                top = 5
            if top == 0:
                print("Failed to retrieve from database")
                print(">>>>>>>>>>>>>Policy with id %s not of any type" %
                      (line["policy_id"]))
                continue
            print("%d:" % (cntr))
            print("Policy id: ", line["policy_id"])
            print("Terms and Conditions")
            tnc = line["terms_and_conditions"].split('-')
            for s in tnc:
                print(s)
            print("Date of Issue: ", line["date_of_issue"])
            print("Duration: %d months" % (line["durantion_in_months"]))
            print("Premium: ", line["premium_value"])
            print("Sum assured: ", line["sum_assured"])
            print("Department number of issuing employee: ",
                  line["employee_department_no"])
            print("Serial number of issuing employee: ",
                  line["employee_serial_no"])
            if top == 1:
                query = "SELECT * FROM Beneficiaries WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                ben = cur.fetchall()

                names = ""
                for x in ben:
                    names += (", %s" % (x["name_of_beneficiary"]))
                print("Death Value Benefit: ", life["death_value_benefit"])
                print("Medical History of Customer: ")
                mh = life["medical_history"].split('-')
                for s in mh:
                    print("\t", s)
                if len(names) > 0:
                    print("Names of beneficiaries of Customer: ", names[2:])
                else:
                    print(
                        "Names of beneficiaries of Customer: No beneficiaries mentioned")
            elif top == 2:
                query = "SELECT * FROM Conditions_Covered WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                cond = cur.fetchall()

                cond_names = ""
                for x in cond:
                    words = x["name_of_condition"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    cond_names += (", %s" % (s))
                query = "SELECT * FROM Cashless_Hospitals WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                hosp = cur.fetchall()

                hosp_names = ""
                for x in hosp:
                    words = x["name_of_hospital"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    hosp_names += (", %s" % (s))
                print("Death Value Benefit: ", med["death_value_benefit"])
                if len(cond_names) > 0:
                    print("Conditions Covered by Policy: ", cond_names[2:])
                else:
                    print("Conditions Covered by Policy: No conditions mentioned")
                if len(hosp_names) > 0:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: ", hosp_names[2:])
                else:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: No hospitals mentioned")
            elif top == 3:
                query = "SELECT * FROM Vehicle_Colours WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                colt = cur.fetchall()

                col_names = ""
                for x in colt:
                    words = x["colour"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    col_names += (", %s" % (s))
                query = "SELECT * FROM Customer_License_No WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                lnt = cur.fetchall()

                ln = ""
                for x in lnt:
                    ln = x["customer_license_no"]
                    break
                print("License Plate Number: ", vehicle["license_plate_no"])
                if len(col_names) > 0:
                    print("Colours of Vehicle: ", col_names[2:])
                else:
                    print("Colours of Vehicle: No colours mentioned")
                print("Customer License Number: ", ln)
            elif top == 4:
                print("Replacement Cost of House: ", house["replacement_cost"])
                print("House Address: %s, %s-%s, %s" %
                      (house["street_address"], house["city"], house["zip_code"], house["state"]))
            elif top == 5:
                query = "SELECT * FROM Travel_Destinations WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                destt = cur.fetchall()

                dest_names = ""
                for x in destt:
                    words = x["destination"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    dest_names += (", %s" % (s))
                print("Itenerary of Travel: ", travel["itenerary"])
                print("Airline and Hotel Booking of Travel: ",
                      travel["airline_and_hotel_bookings"])
                if len(dest_names) > 0:
                    print("Travel Destinations: ", dest_names[2:])
                else:
                    print("Travel Destinations: No destinations mentioned")
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetCustomersOfAge():
    try:
        row = {}
        print("Enter customer's age: ")
        row["age"] = int(input("Customer Age: "))

        query = "SELECT * FROM Customer WHERE aadhar_no IN (SELECT customer_aadhar_no FROM Customer_Age WHERE age = %d)" % (
            row["age"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            cnums = []
            query = "SELECT * FROM Customer_Contact WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums.append(x["contact_number"])
            print("%d:" % (cntr))
            print("Aadhar Number: ", line["aadhar_no"])
            print("Name: %s %s %s" %
                  (line["first_name"], line["middle_name"], line["surname"]))
            print("Date of Birth: ", line["date_of_birth"])
            print("Age: ", row["age"])
            print("Email id: ", line["email_id"])
            print("Contact Numbers: ", cnums)
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetTotalClaim():
    try:
        row = {}
        print("Enter policy types (Life, Medical, Vehicle, House, Travel)")
        row["subclass"] = (
            input("Policy types (space seperated and case sensitive): ")).split(' ')
        sc = set(row["subclass"])
        val = {}
        for sub in sc:
            result = tuple()
            if sub == "Life":
                query = "SELECT policy_id FROM Life WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Medical":
                query = "SELECT policy_id FROM Medical WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Vehicle":
                query = "SELECT policy_id FROM Vehicle WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "House":
                query = "SELECT policy_id FROM House WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Travel":
                query = "SELECT policy_id FROM Travel WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            else:
                print(">>>>>>>>>>>>>Invalid type of policy")
                continue
            value = 0.0
            for line in result:
                query = "SELECT sum_assured FROM Policy WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                sumt = cur.fetchall()

                sumd = {}
                for x in sumt:
                    sumd = x.copy()
                    break
                value += float(sumd["sum_assured"])
            val[sub] = value

        for key, value in val.items():
            print()
            print("Total claim of %s Insurance Policies is %f" % (key, value))
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetMaxClaim():
    try:
        row = {}
        print("Enter policy type (Life, Medical, Vehicle, House, Travel)")
        row["subclass"] = input(
            "Policy types (space seperated and case sensitive): ")
        result = tuple()
        if row["subclass"] == "Life":
            query = "SELECT policy_id FROM Life WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Medical":
            query = "SELECT policy_id FROM Medical WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Vehicle":
            query = "SELECT policy_id FROM Vehicle WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "House":
            query = "SELECT policy_id FROM House WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Travel":
            query = "SELECT policy_id FROM Travel WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        else:
            print("Failed to retrieve from database")
            print(">>>>>>>>>>>>>Invalid type of policy")
            return
        val = 0.0
        for line in result:
            query = "SELECT sum_assured FROM Policy WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            maxt = cur.fetchall()

            maxd = {}
            for x in maxt:
                maxd = x.copy()
                break
            val = max(val, float(maxd["sum_assured"]))

        print("Maximum claim of %s Insurance Policies is %f" %
              (row["subclass"], val))
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetMinClaim():
    try:
        row = {}
        print("Enter policy type (Life, Medical, Vehicle, House, Travel)")
        row["subclass"] = input(
            "Policy types (space seperated and case sensitive): ")
        result = tuple()
        if row["subclass"] == "Life":
            query = "SELECT policy_id FROM Life WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Medical":
            query = "SELECT policy_id FROM Medical WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Vehicle":
            query = "SELECT policy_id FROM Vehicle WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "House":
            query = "SELECT policy_id FROM House WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Travel":
            query = "SELECT policy_id FROM Travel WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        else:
            print("Failed to retrieve from database")
            print(">>>>>>>>>>>>>Invalid type of policy")
            return
        val = 1000000000.0
        for line in result:
            query = "SELECT sum_assured FROM Policy WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            maxt = cur.fetchall()

            maxd = {}
            for x in maxt:
                maxd = x.copy()
                break
            val = min(val, float(maxd["sum_assured"]))
        if len(result) == 0:
            val = 0.0

        print("Minimum claim of %s Insurance Policies is %f" %
              (row["subclass"], val))
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GetAverageClaim():
    try:
        row = {}
        print("Enter policy type (Life, Medical, Vehicle, House, Travel)")
        row["subclass"] = input(
            "Policy types (space seperated and case sensitive): ")
        result = tuple()
        if row["subclass"] == "Life":
            query = "SELECT policy_id FROM Life WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Medical":
            query = "SELECT policy_id FROM Medical WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Vehicle":
            query = "SELECT policy_id FROM Vehicle WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "House":
            query = "SELECT policy_id FROM House WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        elif row["subclass"] == "Travel":
            query = "SELECT policy_id FROM Travel WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
            cur.execute(query)
            result = cur.fetchall()

        else:
            print("Failed to retrieve from database")
            print(">>>>>>>>>>>>>Invalid type of policy")
            return
        val = 0.0
        for line in result:
            query = "SELECT sum_assured FROM Policy WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            maxt = cur.fetchall()

            maxd = {}
            for x in maxt:
                maxd = x.copy()
                break
            val += float(maxd["sum_assured"])
        if len(result) == 0:
            val = 0.0
        else:
            val /= len(result)

        print("Average claim of %s Insurance Policies is %f" %
              (row["subclass"], val))
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def SearchCustomerByName():
    try:
        row = {}
        print("Enter Customer's info")
        row["name"] = input("Name: ")

        query = "SELECT * FROM Customer WHERE MATCH (first_name, middle_name, surname) AGAINST ('%s*' IN BOOLEAN MODE)" % (
            row["name"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            cnums = []
            age = 0
            query = "SELECT * FROM Customer_Contact WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums.append(x["contact_number"])
            query = "SELECT * FROM Customer_Age WHERE customer_aadhar_no = '%s'" % (
                line["aadhar_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                age = x["age"]
                break
            print("%d:" % (cntr))
            print("Aadhar Number: ", line["aadhar_no"])
            print("Name: %s %s %s" %
                  (line["first_name"], line["middle_name"], line["surname"]))
            print("Date of Birth: ", line["date_of_birth"])
            print("Age: ", age)
            print("Email id: ", line["email_id"])
            print("Contact Numbers: ", cnums)
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            print("Customer Status: ", line["customer_status"])
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def SearchEmployeeByName():
    try:
        row = {}
        print("Enter Employee's info")
        row["name"] = input("Name: ")

        query = "SELECT * FROM Employee WHERE MATCH (first_name, middle_name, surname) AGAINST ('%s*' IN BOOLEAN MODE)" % (
            row["name"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            cnums = []
            age = 0
            query = "SELECT * FROM Employee_Contact WHERE employee_department_no = %d AND employee_serial_no = %d" % (
                line["department_no"], line["serial_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums.append(x["contact_number"])
            query = "SELECT * FROM Employee_Age WHERE employee_department_no = %d AND employee_serial_no = %d" % (
                line["department_no"], line["serial_no"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                age = x["age"]
                break
            print("%d:" % (cntr))
            print("Department Number: ", line["department_no"])
            print("Serial Number: ", line["serial_no"])
            print("Aadhar Number: ", line["aadhar_no"])
            print("Name: %s %s %s" %
                  (line["first_name"], line["middle_name"], line["surname"]))
            print("Date of Birth: ", line["date_of_birth"])
            print("Age: ", age)
            print("Email id: ", line["email_id"])
            print("Contact Numbers: ", cnums)
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            print("Supervisor Department Number: ", line["sup_department_no"])
            print("Supervisor Serial Number: ", line["sup_serial_no"])
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def SearchTPAByName():
    try:
        row = {}
        print("Enter TPA's info")
        row["name"] = input("Name: ")

        query = "SELECT * FROM TPA WHERE MATCH (TPA_name) AGAINST ('%s*' IN BOOLEAN MODE)" % (
            row["name"])

        cur.execute(query)
        result = cur.fetchall()

        print()

        cntr = 1
        for line in result:
            cnums = ""
            types = ""
            query = "SELECT * FROM TPA_Contact_Info WHERE TPA_id = '%s'" % (
                line["TPA_id"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                cnums += ", "
                cnums += x["contact_number"]
            query = "SELECT * FROM TPA_Investigations_Conducted WHERE TPA_id = '%s'" % (
                line["TPA_id"])
            cur.execute(query)
            cc = cur.fetchall()

            for x in cc:
                types += ", "
                types += x["type"]
            print("%d:" % (cntr))
            print("TPA Id: ", line["TPA_id"])
            print("Name: ", line["TPA_name"])
            print("Address: %s, %s-%s, %s" %
                  (line["street_address"], line["city"], line["zip_code"], line["state"]))
            if len(cnums) > 0:
                print("Contact Numbers: ", cnums[2:])
            else:
                print("Contact Numbers: No numbers mentioned")
            if len(types) > 0:
                print("Types of Investigations Conducted: ", types[2:])
            else:
                print("Types of Investigations Conducted: No types mentioned")
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GenerateClaimedPolicyReports():
    try:
        row = {}
        print("Enter policy types (Life, Medical, Vehicle, House, Travel)")
        row["subclass"] = (
            input("Policy types (space seperated and case sensitive): ")).split(' ')
        sc = set(row["subclass"])
        val = {}
        for sub in sc:
            result = tuple()
            if sub == "Life":
                query = "SELECT policy_id FROM Life WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Medical":
                query = "SELECT policy_id FROM Medical WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Vehicle":
                query = "SELECT policy_id FROM Vehicle WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "House":
                query = "SELECT policy_id FROM House WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            elif sub == "Travel":
                query = "SELECT policy_id FROM Travel WHERE policy_id IN (SELECT policy_id FROM Resolves_Claims)"
                cur.execute(query)
                result = cur.fetchall()

            else:
                print(">>>>>>>>>>>>>Invalid type of policy")
                continue
            val[sub] = []
            for line in result:
                val[sub].append(line["policy_id"])

        for key, value in val.items():
            print("%s Insurance: " % (key))
            cntr = 1
            for pid in value:
                query = "SELECT claim_report FROM Claim_Report WHERE policy_id = '%s'" % (
                    pid)
                cur.execute(query)
                result = cur.fetchall()

                reportstr = ""
                print(result)
                for x in result:
                    reportstr = x["claim_report"]
                    break
                print("%d:" % (cntr))
                print("Policy Id: ", pid)
                if reportstr != None:
                    print("Report:")
                    report = reportstr.split('-')
                    for s in report:
                        print(s)
                else:
                    print("Report: No report mentioned")
                cntr += 1
            print()

        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def GenerateCustomerReport():
    try:
        row = {}
        print("Enter customer's Aadhar Number: ")
        row["aadhar_no"] = input("Aadhar number: ")

        query = "SELECT * FROM Policy WHERE customer_aadhar_no = '%s' AND policy_id IN (SELECT policy_id FROM Resolves_Claims)" % (
            row["aadhar_no"])

        cur.execute(query)
        result = cur.fetchall()

        val = 0.0
        for line in result:
            val += float(line["sum_assured"])

        query = "SELECT * FROM Policy WHERE customer_aadhar_no = '%s'" % (
            row["aadhar_no"])

        cur.execute(query)
        result = cur.fetchall()

        print()
        print("Total amount claimed by customer is ", val)
        print()

        cntr = 1
        for line in result:
            top = 0
            query = "SELECT * FROM Life WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            lifet = cur.fetchall()

            query = "SELECT * FROM Medical WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            medt = cur.fetchall()

            query = "SELECT * FROM Vehicle WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            veht = cur.fetchall()

            query = "SELECT * FROM House WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            hset = cur.fetchall()

            query = "SELECT * FROM Travel WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            trat = cur.fetchall()

            query = "SELECT * FROM Claim_Date WHERE policy_id = '%s'" % (
                line["policy_id"])
            cur.execute(query)
            claimt = cur.fetchall()

            life = {}
            med = {}
            vehicle = {}
            house = {}
            travel = {}
            doc = datetime.now()
            for x in claimt:
                doc = x["date_of_claim"]
                break
            if len(lifet) > 0:
                for x in lifet:
                    life = x.copy()
                    break
                top = 1
            elif len(medt) > 0:
                for x in medt:
                    med = x.copy()
                    break
                top = 2
            elif len(veht) > 0:
                for x in veht:
                    vehicle = x.copy()
                    break
                top = 3
            elif len(hset) > 0:
                for x in hset:
                    house = x.copy()
                    break
                top = 4
            elif len(trat) > 0:
                for x in trat:
                    travel = x.copy()
                    break
                top = 5
            if top == 0:
                print("Failed to retrieve from database")
                print(">>>>>>>>>>>>>Policy with id %s not of any type" %
                      (line["policy_id"]))
                continue
            print("%d:" % (cntr))
            print("Policy id: ", line["policy_id"])
            print("Terms and Conditions")
            tnc = line["terms_and_conditions"].split('-')
            for s in tnc:
                print(s)
            print("Date of Issue: ", line["date_of_issue"])
            print("Duration: %d months" % (line["durantion_in_months"]))
            print("Premium: ", line["premium_value"])
            print("Sum assured: ", line["sum_assured"])
            print("Department number of issuing employee: ",
                  line["employee_department_no"])
            print("Serial number of issuing employee: ",
                  line["employee_serial_no"])
            if len(claimt) > 0:
                print("Policy Status: Claimed")
                print("Date of Claim: ", doc)
            else:
                print("Policy Status: Not Claimed")
            if top == 1:
                query = "SELECT * FROM Beneficiaries WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                ben = cur.fetchall()

                names = ""
                for x in ben:
                    names += (", %s" % (x["name_of_beneficiary"]))
                print("Death Value Benefit: ", life["death_value_benefit"])
                print("Medical History of Customer: ")
                mh = life["medical_history"].split('-')
                for s in mh:
                    print("\t", s)
                if len(names) > 0:
                    print("Names of beneficiaries of Customer: ", names[2:])
                else:
                    print(
                        "Names of beneficiaries of Customer: No beneficiaries mentioned")
            elif top == 2:
                query = "SELECT * FROM Conditions_Covered WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                cond = cur.fetchall()

                cond_names = ""
                for x in cond:
                    words = x["name_of_condition"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    cond_names += (", %s" % (s))
                query = "SELECT * FROM Cashless_Hospitals WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                hosp = cur.fetchall()

                hosp_names = ""
                for x in hosp:
                    words = x["name_of_hospital"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    hosp_names += (", %s" % (s))
                print("Death Value Benefit: ", med["death_value_benefit"])
                if len(cond_names) > 0:
                    print("Conditions Covered by Policy: ", cond_names[2:])
                else:
                    print("Conditions Covered by Policy: No conditions mentioned")
                if len(hosp_names) > 0:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: ", hosp_names[2:])
                else:
                    print(
                        "Cashless Hospitals having tie-ups with Policy: No hospitals mentioned")
            elif top == 3:
                query = "SELECT * FROM Vehicle_Colours WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                colt = cur.fetchall()

                col_names = ""
                for x in colt:
                    words = x["colour"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    col_names += (", %s" % (s))
                query = "SELECT * FROM Customer_License_No WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                lnt = cur.fetchall()

                ln = ""
                for x in lnt:
                    ln = x["customer_license_no"]
                    break
                print("License Plate Number: ", vehicle["license_plate_no"])
                if len(col_names) > 0:
                    print("Colours of Vehicle: ", col_names[2:])
                else:
                    print("Colours of Vehicle: No colours mentioned")
                print("Customer License Number: ", ln)
            elif top == 4:
                print("Replacement Cost of House: ", house["replacement_cost"])
                print("House Address: %s, %s-%s, %s" %
                      (house["street_address"], house["city"], house["zip_code"], house["state"]))
            elif top == 5:
                query = "SELECT * FROM Travel_Destinations WHERE policy_id = '%s'" % (
                    line["policy_id"])
                cur.execute(query)
                destt = cur.fetchall()

                dest_names = ""
                for x in destt:
                    words = x["destination"].split('-')
                    s = words[0]
                    for i in range(1, len(words)):
                        s += (" %s" % (words[i]))
                    dest_names += (", %s" % (s))
                print("Itenerary of Travel: ", travel["itenerary"])
                print("Airline and Hotel Booking of Travel: ",
                      travel["airline_and_hotel_bookings"])
                if len(dest_names) > 0:
                    print("Travel Destinations: ", dest_names[2:])
                else:
                    print("Travel Destinations: No destinations mentioned")
            print()
            cntr += 1
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    if ch == 1:
        AddCustomer()
    elif ch == 2:
        AddCustomerDependant()
    elif ch == 3:
        AddEmployee()
    elif ch == 4:
        AddEmployeeDependant()
    elif ch == 5:
        AddLifeInsurance(AddPolicy())
    elif ch == 6:
        AddMedicalInsurance(AddPolicy())
    elif ch == 7:
        AddVehicleInsurance(AddPolicy())
    elif ch == 8:
        AddHouseInsurance(AddPolicy())
    elif ch == 9:
        AddTravelInsurance(AddPolicy())
    elif ch == 10:
        AddTPA()
    elif ch == 11:
        ResloveClaim()
    elif ch == 12:
        UpdateCustomerInfo()
    elif ch == 13:
        UpdateCustomerDependentInfo()
    elif ch == 14:
        UpdateEmployeeInfo()
    elif ch == 15:
        UpdateEmployeeDependantInfo()
    elif ch == 16:
        UpdateTPAinfo()
    elif ch == 17:
        UpdatePolicy()
    elif ch == 18:
        DeleteCustomer()
    elif ch == 19:
        DeleteCustomerDependant(None, None, None)
    elif ch == 20:
        DeleteEmployee()
    elif ch == 21:
        DeleteEmployeeDependant(None, None, None)
    elif ch == 22:
        DeletePolicy("")
    elif ch == 23:
        DeleteTPA()
    elif ch == 24:
        GetAllCustomers()
    elif ch == 25:
        GetAllPoliciesOfCustomers()
    elif ch == 26:
        GetAllDependentsOfCustomers()
    elif ch == 27:
        GetAllDependentsOfEmployee()
    elif ch == 28:
        GetAllTPAsInCity()
    elif ch == 29:
        GetInsurancePolicies()
    elif ch == 30:
        GetInsuranceCustomers()
    elif ch == 31:
        GetPoliciesWithPremium()
    elif ch == 32:
        GetCustomersOfAge()
    elif ch == 33:
        GetTotalClaim()
    elif ch == 34:
        GetMaxClaim()
    elif ch == 35:
        GetMinClaim()
    elif ch == 36:
        GetAverageClaim()
    elif ch == 37:
        SearchCustomerByName()
    elif ch == 38:
        SearchEmployeeByName()
    elif ch == 39:
        SearchTPAByName()
    elif ch == 40:
        GenerateClaimedPolicyReports()
    elif ch == 41:
        GenerateCustomerReport()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")
    # print(colored("Type exit to exit the application", 'red'))
    # username = input("Username: ")
    # if(username == "exit"):
    #     break
    # password = input("Password: ")

    # if(password == "exit"):
    #     break

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              port=30306,
                              db='dna_database',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print(
                    "Please enter the number cooresponding to the action you want to perform:")
                print("1. Add a Customer")
                print("2. Add a Customer Dependant")
                print("3. Add an Employee")
                print("4. Add a Employee Dependant")
                print("5. Add a Life Insurance Policy")
                print("6. Add a Medical Insurance Policy")
                print("7. Add a Vehicle Insurance Policy")
                print("8. Add a House Insurance Policy")
                print("9. Add a Travel Insurance Policy")
                print("10. Add a Third Party Administrator")
                print("11. Reslove a Policy Claim")
                print("12. Update the information of an existing Customer")
                print(
                    "13. Update the information of an existing Dependant of an existing Customer")
                print("14. Update the information of an Employee")
                print(
                    "15. Update the information of an existing Dependant of an existing Employee")
                print("16. Update the information of a Third Party Administrator")
                print("17. Update the information of a Policy")
                print("18. Delete the information of a Customer")
                print("19. Delete the information of a Customer's Dependant")
                print("20. Delete the information of an Employee")
                print("21. Delete the information of a Employee's Dependant")
                print("22. Delete the information of a Policy")
                print("23. Delete the information of a Third Party Administrator")
                print("24. Get all Customers of given status")
                print("25. Get all Policies bought by given customer")
                print("26. Get information of all Dependents of a Customer")
                print("27. Get information of all Dependents of an Employee")
                print(
                    "28. Get information of all Third Party Administrators in a given city")
                print("29. Get information of all Policies in a given list")
                print("30. Get information of all Customers with status in a given list and who have bought policies of a type in a given list")
                print(
                    "31. Get information of all Policies with their premium in a given range")
                print("32. Get information of all Customers of a given age")
                print("33. Get total claim value of policy types of a given list")
                print("34. Get Maximum claim value of a given policy type")
                print("35. Get Minimum claim value of a given policy type")
                print("36. Get Average claim value of a given policy type")
                print(
                    "37. Get information of all Customers with partial/complete match to given name")
                print(
                    "38. Get information of all Employees with partial/complete match to given name")
                print(
                    "39. Get information of all Third Party Administrators with partial/complete match to given name")
                print(
                    "40. Generate reports of all claimed policies of a given list of policy types")
                print("41. Generate reports of all policies bought by a given Customer")
                print("0. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 0:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        print(username, password)
        tmp = input("Enter any key to CONTINUE>")
