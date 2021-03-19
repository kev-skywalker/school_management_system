#We implement a few functions of students module
#First we import connection and query from queries module
from ..queries.connection import *
from ..queries.query import *
import mysql.connector

class Student:
    def __init__(self, *args):
        #conxDB: instance of connection to the database
        self.username=args[0]
        self.pwd=args[1]
        self.conxDB=self.getConnection(self.username, self.pwd)

    def getConnection(self, username,passwd):
        return connectServer("127.0.0.1", username, passwd, 10)


    #Create a function to add items to table student
    def addStudent(self, attributes, values):
        #attributes: list of attributes name of student table
        #values: list of tuples (value1, value2,..., valueN)
        #        each value is an information about the student profile

        cursor=self.conxDB.cursor()
        tb_query=inserttoTable("student", attributes, values)

        try:
            cursor.execute("USE school")
        except mysql.connector.Error as Er:
            print("Something is wrong with this data! Please check=> ", Er)
            exit(1)

        try:
            cursor.executemany(tb_query, values)
        except mysql.connector.Error as Er:
            print("Can't insert element into table! Please check what's wrong=> ", Er)
        else:
            self.conxDB.commit()
        cursor.close()

    #Create a function selectStudent to search and find student within a MySQL table
    def selectStudent(self, requestedAttr, condition):
        #requestedAttr: list of attributes (string data type)
        #condition: condition on which rows of tables are selected
        #           attribute= or > value

        cursor=self.conxDB.cursor()
        tb_query=select("student", requestedAttr, condition)

        try:
            cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("Something is wrong => ", Er)
        else:
            result=cursor.fetchall()
        return result

    #create a function to change a student's phone and level
    def changevalueStudent(self, tablename, attributes, newvalues, condition):
        #tablename:
        #attributes: list of attributes as tablename.attributes1, tablename.attributes2
        #newvalues: values to replace with the old one.
        #condition: condition on which rows of tables are selected
        #           tablename.attribute = value

        cursor = self.conxDB.cursor()
        tb_query = changeValue(tablename, attributes, newvalues, condition)

        try:
           cursor.execute("USE school")
        except mysql.connector.Error as Er:
            print("Something is wrong with this data! Please check=> ", Er)
            exit(1)

        try:
           cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("Can't change element into table! Please check what's wrong=> ", Er)
        else:
           self.conxDB.commit()
        cursor.close()
    #createUserAccount to create an user account for student
    def createUserAccount(self, usr, pwd):
        #usr: username
        #pwd: password


        cursor = self.conxDB.cursor()
        tb_query = createuserAccount(usr, pwd)

        try:
           cursor.execute("USE school")
        except mysql.connector.Error as Er:
            print("Something is wrong with this data! Please check=> ", Er)
            exit(1)
        try:
           cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("Can't create user account into the database! Please check what's wrong=> ", Er)
        else:
           self.conxDB.commit()
        cursor.close()

     #grantUserAccount to grant privileges to an user account
     def grantUserAccount(self, usr):
         #usr: username

         cursor = self.conxDB.cursor()
         tb_query = grantuserAccount(usr)

         try:
            cursor.execute("USE school")
         except mysql.connector.Error as Er:
             print("Something is wrong with this data! Please check=> ", Er)
             exit(1)

         try:
            cursor.execute(tb_query)
         except mysql.connector.Error as Er:
             print("Can't grant privileges to an user account into the database! Please check what's wrong=> ", Er)
         else:
            self.conxDB.commit()
         cursor.close()
