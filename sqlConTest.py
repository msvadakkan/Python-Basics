import mysql.connector
dbCon=mysql.connector.connect(host="localhost",user="root",password="",database="")
dbQry=dbCon.cursor()
db.dbQry.execute("USE data2")
db=dbCursor.execute("Insert Into tabl1 values(3,'aneena')")
db=dbCursor.execute("Insert Into tabl1 values(4,'keerthy')")
dbCon.commit()


