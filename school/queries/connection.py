#We implement a few functions of queries module
#First we import connect, Error and pooling from mysql connector module
import mysql
import mysql.connector
import mysql.connector.errors
from mysql.connector.errors import Error as error
#from mysql.connector import pooling 
#from mysql.connector import connect 

#Create a function to connect to a MySQL server
#connectServer returns a pool of connections
def connectServer(hostname, username, passwd, poolsize):
    config={"host":hostname, "user":username, "password":passwd}
    try:
        conPool=mysql.connector.connect(pool_name="conPool", pool_size=poolsize, **config)
    except error as Er:
        print("Impossible to connect to the sever! Please check what's wrong: ", Er)
    else:
        return conPool

#Create a function to connect to a MySQL database
#connectDB returns a pool of connections
def connectDB(hostname, dbname, username, passwd, poolsize):
    config={"host":hostname, "host":hostname, "user":username, "password":passwd}
    try:
        conPool=mysql.connector.connect(pool_name="conPool", pool_size=poolsize, **config)
    except error as Er:
        print("Impossible to connect to the database! Please check what's wrong: ", Er)
    else:
        #conList=[conPool.get_connection() for i in range(poolsize)]
        return conPool

