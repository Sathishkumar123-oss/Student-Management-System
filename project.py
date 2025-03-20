#----------Create new Database and new Table in python
'''
import pymysql.cursors

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "sathish81!@.",
    database = "Student_Records"
    )

cursor = conn.cursor()

#--Create new database--#
cursor.execute("create database if not exists Student_Records")
print("Database 'Student_Records' created succesfully!")

#--Create new table--#
cursor.execute("""
    create table if not exists Student_Info(
        Student_Id int auto_increment primary key,
        Student_Name varchar(200) not null,
        DOB date not null,
        Phone_No bigint unique not null,
        Address varchar(200) not null
        )
    """)
print("Table 'Student_Info' created successfully!")

#--close the connection--#
cursor.close()
conn.close()
'''

#-----------------

import pymysql.cursors

#--Database connection--#
try:
    conn = pymysql.connect(
        host = "localhost",
        user="root",
        password = "sathish81!@.",
        database = "Student_Records"
        )
    cursor = conn.cursor()
except pymysql.MySQLError as e:
    print(f"Error connecting to Database: {e}")

#--Create Student Information--#
def create_stud_info(Student_Id, Student_Name, Age, Phone_No, Address):
    try:
        sql="Insert into Student_Info(Student_Id, Student_Name, Age, Phone_No, Address) values (%s,%s,%s,%s,%s)"
        stud_info_values=(Student_Id, Student_Name, Age, Phone_No, Address)
        cursor.execute(sql,stud_info_values)
        conn.commit()
        print("Student Information Added Succesfully!")
    except pymysql.MySQLError as e:
        print(f"Error creating Student Information: {e}")

#--Show the Student Information--#
def show_stud_info():
    try:
        cursor.execute("select * from Student_Info")
        Student_info_values = cursor.fetchall()
        print("Student Informations")
        print("\nStud_Id -> Student_Name -> Age -> Phone_No -> Stud_Address\n")
        for user in Student_info_values:
            print(user)
    except pymysql.MySQLError as e:
        print(f"Error showing Student Information: {e}")

#--Modify in Studentt Information--#
def modify_stud_info(Student_Id, Student_Name, Age, Phone_No, Address):
    try:
        sql = "update Student_Info set Student_Name = %s, Age = %s, Phone_No = %s, Address = %s where Student_Id = %s"
        stud_info_values=(Student_Name, Age, Phone_No, Address, Student_Id)
        cursor.execute(sql,stud_info_values)
        conn.commit()
        print("Student Information Modify Succerssfuly!")
    except pymysql.MySQLError as e:
        print(f"Erro Modify Student Information: {e}")

#--Remove in Student Information--#
def remove_stud_info(Student_Id):
    try:
        sql = "delete from Student_Info where Student_Id = %s"
        cursor.execute(sql,(Student_Id))
        conn.commit()
        print("Removing Student Information Successfully!")
    except pymysql.MySQLError as e:
        print(f"Error Removing Student Information: {e}")

#--Choosing the Option--#
while True:
    print("\nStudent Information")
    print("1. Create Student Information")
    print("2. Showing Student Information")
    print("3. Modify Student Information")
    print("4. Removing Student Information")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        try:
            Student_Id = int(input("Enter Id: "))
            Student_Name = input("Enter Name: ")
            Age = input("Enter Age:")
            Phone_No = int(input("Enter Mobile number: "))
            Address = input("Enter Address: ")
            create_stud_info(Student_Id, Student_Name, Age, Phone_No, Address)
        except ValueError:
            print("Invalid input! Enter Correct Value.")

    elif choice == '2':
        show_stud_info()

    elif choice == '3':
        try:
            Student_Id = int(input("Enter Student Information ID to Modify: "))
            Student_Name = input("Enter new Name: ")
            Age = input("Enter New Age: ")
            Phone_No = int(input("Enter New Phone Number: "))
            Address = input("Enter New Address: ")
            modify_stud_info(Student_Id, Student_Name, Age, Phone_No, Address)
        except ValueError:
            print("Invalid input! Enter Correct Value.")

    elif choice == '4':
        try:
            Student_Id = int(input("Enter Student ID to Remove: "))
            remove_stud_info(Student_Id)
        except ValueError:
            print("Invalid input! Enter Correct Value.")
    elif choice == '5':
        print("Exit Program...")
        break

    else:
        print("Invalid choice! Choose Correct choice..")

#--Close the connection--#
try:
    cursor.close()
    conn.close()

except pymysql.MySQLError as e:
    print(f"Error closing the database connection: {e}")


#-----------------Modify column names or drop any
'''
import pymysql
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "sathish81!@.",
    database = "Student_Records")

try:
    with conn.cursor() as cursor:
        sql = """
              alter table Student_Info
              change DOB Age int;
              """
        cursor.execute(sql)
        conn.commit()
        print("Rename succesfully!")
finally:
    conn.close()
'''
        





























