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
