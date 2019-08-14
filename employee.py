import mysql.connector
user_name = input("user_name: ")
Password = input("password: ")
conn = mysql.connector.connect(user=user_name,password=Password,host="localhost")
cur = conn.cursor(prepared=True)
cur.execute("create database if not exists test_ashish")
conn = mysql.connector.connect(user=user_name,password=Password,host="localhost",database="test_ashish")
cur = conn.cursor(prepared=True)
cur.execute("create database if not exists test_ashish")
cur.execute("create table if not exists Employee(Employee_ID int(10) NOT NULL auto_increment,First_Name varchar(50) NOT NULL, Last_Name varchar(50) NOT NULL,Email varchar(100), PRIMARY KEY (Employee_ID))")
cur.execute("create table if not exists Department(Employee_ID int(10) NOT NULL auto_increment, Department_Name varchar(40) NOT NULL,Basic_Salary int(6) NOT NULL, Dearness_allowance int(5),Travelling_allowance int(4),Conveyance_allowance int(4), Total_salary int(7) NOT NULL,"
            "foreign key (Employee_ID) references Employee(Employee_ID))  ")
what_you_want_to_do = input("""Choose from the following
press 1 for inserting Employee details
press 2 for inserting Employee salary and department details
press 3 to update in Employee table
press 4 to update in Department table
: """)
if int(what_you_want_to_do) == 1:
    F_N = input("First name: ")
    L_N = input("Last name: ")
    E_M = input("Email: ")
    records_to_insert =(F_N,L_N,E_M)
    sql_insert_query ="""INSERT INTO Employee (First_Name,Last_Name,Email) VALUES(%s,%s,%s)"""
    cur.execute(sql_insert_query,records_to_insert)
    conn.commit()
    print("your record inserted successfully in Employee table")
elif int(what_you_want_to_do) == 2:
    De_N = input("Department Name: ")
    B_S = int(input("Basic salary: "))
    D_A = int(input("Dearness allowance: "))
    T_A = int(input("Travelling Allowance: "))
    C_A = int(input("Conveyance Allowance: "))
    To_Sa = int(D_A+ B_S + T_A + C_A)
    records_to_insert = (De_N,B_S,D_A,T_A,C_A,To_Sa)
    insert_in_query = """INSERT INTO Department(Department_Name,Basic_Salary,Dearness_allowance,Travelling_allowance,conveyance_allowance,Total_salary)
    VALUES(%s,%s,%s,%s,%s,%s)"""
    cur.execute(insert_in_query,records_to_insert)
    conn.commit()
    print("your record inserted successfully in Department table")
elif int(what_you_want_to_do) == 3:
    Em_Id = input("Employee Id to be updated: ")
    E_M = input("Email: ")
    insert_in_query = "update Employee set Email = %s where Employee_ID = %s"
    records_to_insert = (E_M,Em_Id)
    cur.execute(insert_in_query,records_to_insert)
    conn.commit()
    print("employee table updated")
elif int(what_you_want_to_do) == 4:
    Em_Id = int(input("Employee id whose salary is updating: "))
    B_S = int(input("Basic salary: "))
    D_A = int(input("Dearness allowance: "))
    T_A = int(input("Travelling Allowance: "))
    C_A = int(input("Conveyance Allowance: "))
    To_Sa = int(D_A + B_S + T_A + C_A)
    records_to_insert = (B_S, D_A, T_A, C_A,To_Sa,Em_Id )
    insert_in_query = "update Department set Basic_salary = %s,Dearness_allowance = %s,Travelling_allowance = %s, conveyance_allowance = %s,Total_salary = %s  where Employee_ID = %s"
    cur.execute(insert_in_query, records_to_insert)
    conn.commit()
    print("Department table updated")

