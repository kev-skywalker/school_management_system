#Import module
import school.queries.connection
from ..queries.connection import *

#inserttoTable to insert one or several items into a table
def inserttoTable(tablename, attributes, values):
    #tablename: name of the table
    #attributes: list of attributes (string data type)
    #values: list of tuples (value1, value2,..., valueN)
    #        value: data type corresponds to database attribute type
    #        N=len(attributes)

    if len(attributes)==len(values[-1]):
        atr="("
        val="VALUES("

        for i in range(len(attributes)-1):
            atr=atr+str(attributes[i])+","
            val=val+"%s,"
        atr=atr+str(attributes[-1])+")"
        val=val+"%s)"

    else:
        raise Exception("Number of values should correspond to number of attributes: len(values[i])==len(attributes)")
    tb_query="INSERT INTO "+tablename+atr+" "+val

    return tb_query


#select items from a table
def select(tablename, attributes, *args):
    #tablename: name of the table
    #attributes: list of attributes (string data type)

    atr=attributes[0]
    for item in attributes[1:]:
        atr=atr+","+item

    if len(args)>0:
        tb_query="SELECT "+atr+" FROM "+tablename+" WHERE "+args[0]
    else:
        tb_query="SELECT "+atr+" FROM "+tablename

    return tb_query

#selectJoin to select items from several tables with INNER JOIN
def selectJoin(tables, attr, condition):
    #tables:
    #attr: list of attributes as tablename1.attribute, tablename2.attribute
    #condition: condition on which rows of tables are selected
    #           tablename1.attribute= or > tablename2.attribute


    if len(tables)>2:
        atr=attr[0]
        for item in attr[1:]:
            atr=atr+","+item
    else:
        raise Exception("The number of expected tables is: 02")

    tb_query="SELECT "+atr+" FROM "+tables[0]+" INNER JOIN "+tables[1]+" ON "+condition

    return tb_query
#changeValue to change an attribute value into a table
def changeValue(tablename, attributes, newvalues, condition):
    #tablename:
    #attributes: list of attributes as tablename.attributes1, tablename.attributes2
    #newvalues: values to replace with the old one.
    #condition: condition on which rows of tables are selected
    #           tablename.attribute = value

    tb_query = ("UPDATE "+tablename+" SET ("+attributes[0] = newvalues[0]+","+attributes[1] = newvalue[1]+") WHERE "+condition")

    return tb_query

#createuserAccount to create an user accountfor student or teacher
def createuserAccount(usr, pwd):
    #usr: usrname
    #pwd: password

    user_account = "CREATE USER '"+usr+"''@'127.0.0.1' IDENTIFIED BY '"+pwd+"' "

    tb_query = user_account

    return tb_query

##grantUserAccount to grant privileges to an user account
def grantuserAccount(usr):
    #usr: username

    user_privilege = "GRANT ALL ON school.* To '"+usr+"''@'127.0.0.1' "

    tb_query = user_privilege

    return tb_query
