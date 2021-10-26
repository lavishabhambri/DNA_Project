# Insurance Company Database

### Team : DEMOLISHERS
Mayank Bhardwaj (2020101068)  
Lavisha Bhambri (2020101088)  
Abhinav Anand   (2020101054)  

---

This is a simple CLI interface database application for a simplified database for an insurance company implemented in python. This CLI supports functions like adding/deleting/updating an employee, customer, policy, customer dependant, employee dependent, Third Party Administrators (TPA), and also functions to get information about all dependents of a customer, finding employee/customer with names each using partial match, etc.

---

- Steps to install docker can be found [here](https://docs.docker.com/engine/install/)
- Steps to install mysql can be found at:
    - [ubuntu users](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
    - [mac users](https://flaviocopes.com/mysql-how-to-install/)
- `python3, pymysql` are required.
    - To install `pymysql` using pip3, do `pip3 install pymysql`
---

## Steps to run:

- `Insurance_Company.sql` creates the database, the necessary tables and also populates the database with some data.

- `Insurance_Company.py` is the actual python implemented CLI code.

### Commands to run before starting:

- Use `sudo mysql -h 127.0.0.1 -u root --port=30306 -p < Insurance_Company.sql` to load the database. Then type the password of the user loading the database.

- `sudo mysql`

- Now a mysql prompt will open and inside that write the dump command mentioned `source Insurance_Company.sql `.

- Connect database in VS CODE using the given below extension 

- Extension Details
    Name: MySQL
    Id: cweijan.vscode-mysql-client2
    Description: Database Client for vscode
    Version: 4.1.7
    Publisher: cweijan
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-mysql-client2.

- Use `python3 Insurance_Company.py` to start the CLI. Then enter 
    `Username: root`
    `Password: <entered_by_you>`
                                
- Follow the instructions on the screen.

## Commands for the user

### 1.Add a Customer 
- Adds the information about a Customer in the given database.

### 2.Add a Customer Dependant
- Adds the information about a Customer Dependant in the given database.

### 3.Add an Employee 
- Adds the information about an Employee in the given database.

### 4.Add an Employee Dependant
- Adds the information about an Employee Dependant in the given database.

### 5. Add a Life Insurance Policy
- Adds a Life Insurance Policy in the given database.

### 6. Add a Medical Insurance Policy
- Adds a Medical Insurance Policy in the given database.

### 7. Add a Vehicle Insurance Policy
- Adds a Vehicle Insurance Policy in the given database.

### 8. Add a House Insurance Policy
- Adds a House Insurance Policy in the given database.

### 9. Add a Travel Insurance Policy
- Adds a Travel Insurance Policy in the given database.

### 10. Add a Third Party Administrator
- Adds the information about a Third Party Administrator in the given database.

### 11. Reslove a Policy Claim
- Resolves a given Policy Claim

### 12. Update the information of an existing Customer
- Updates the information about a given Customer

### 13. Update the information of an existing Dependant of an existing Customer
- Updates the information about an existing Dependant of an existing Customer

### 14. Update the information of an Employee
- Updates the information about a given Employee

### 15. Update the information of an existing Dependant of an existing Employee
- Updates the information about an existing Dependant of an existing Employee

### 16. Update the information of a Third Party Administrator
- Updates the information about a given Third Party Administrator

### 17. Update the information of a Policy
- Updates the information about a given Policy

### 18. Delete the information of a Customer
- Deletes the information about a given Customer

### 19. Delete the information of a Customer's Dependant
- Deletes the information about a given Customer's Dependant

### 20. Delete the information of an Employee
- Deletes the information about a given Employee

### 21. Delete the information of an Employee's Dependant
- Deletes the information about a given Employee's Dependant

### 22. Delete the information of a Policy
- Deletes the information about a given Policy

### 23. Delete the information of a Third Party Administrator
- Deletes the information about a given Third Party Administrator

### 24. Get all Customers of given status
- Displays all the Customers with a given status (platinum,gold,silver...etc.)

### 25. Get all Policies bought by a given Customer 
- Displays all Policies bought by a given Customer 

### 26. Get information of all Dependants of a Customer 
- Displays information about all the Dependants of a Customer

### 27. Get information of all Dependants of an Employee 
- Displays information about all the Dependants of an Employee 

### 28. Get information of all Third Party Administrators in a given city
- Displays information about all Third Party Administrators in a given city

### 29. Get information of all Policies in a given list
- Displays information about all Policies in a given list

### 30. Get information of all Customes with status in a given list and who have bought policies of a type in a given list
- Displays information about all Customes with status in a given list and who have bought policies of a type in a given list

### 31. Get information of all Policies with their premium in a given range
- Displays information about all Policies with their premium in a given range

### 32. Get information of all Customers of a given range
- Displays information about all Customers of a given range

### 33. Get total claim value of policy types of a given list
- Displays Get total claim value of policy types of a given list

### 34. Get Maximum claim value of a given policy type
- Displays Maximum claim value of a given policy type

### 35. Get Minimum claim value of a given policy type
- Displays Minimum claim value of a given policy type

### 36. Get Average claim value of a given policy type
- Displays Average claim value of a given policy type

### 37. Get information of all Customers with partial/complete match to given name
- Displays information of all Customers with partial/complete match to given name

### 38. Get information of all Employees with partial/complete match to given name
- Displays information of all Employees with partial/complete match to given name

### 39. Get information of all Third Party Administrators with partial/complete match to given name
- Displays information of all Third Party Administrators with partial/complete match to given name

### 40. Generate reports of all claimed policies of a given list of policy types
- Displays reports of all claimed policies of a given list of policy types

### 41. Generate reports of all policies bought by a given Customer
- Displays reports of all policies bought by a given Customer

### 42. Logout
- Exits the CLI


## Commands Shown in the video (OrderWise)-

### 1.Add a Customer  
### 2.Add a Customer Dependant
### 12. Update the information of an existing Customer
### 26. Get information of all Dependants of a Customer 
### 24. Get all Customers of given status
### 18. Delete the information of a Customer
### 28. Get information of all Third Party Administrators in a given city
### 37. Get information of all Customers with partial/complete match to given name
### 39. Get information of all Third Party Administrators with partial/complete match to given name