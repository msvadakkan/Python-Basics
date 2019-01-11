import mysql.connector
dbCon=mysql.connector.connect(host="localhost",user="root",password="",database="")
dbCursor=dbCon.cursor()

dbCursor.execute("USE data2")
dbCursor.execute("CREATE TABLE emplyee(empid int AUTO_INCREMENT PRIMARY KEY,empName varch(30))")
dbCursor.execute("Insert Into tabl1 values(3,'aneena')")
dbCursor.execute("Insert Into tabl1 values(4,'keerthy')")
dbCon.commit()


