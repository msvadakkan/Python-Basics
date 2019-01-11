#form Tkinter
# import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

form=Tk()
form.title("Book Registration")
#____________Form Attributes_________________

b_namL=Label(form,text="Name")
b_namL.grid(column=0,row=0)
NameTxt=Entry(form,width=20)
NameTxt.grid(column=1,row=0)

b_DiscrL=Label(form,text="Description")
b_DiscrL.grid(column=0,row=2)
bDiscr=Entry(form,width=20)
bDiscr.grid(column=1,row=2)

namA=Label(form,text="Author")
namA.grid(column=0,row=3)
AnameTxt=Entry(form,width=20)
AnameTxt.grid(column=1,row=3)

namP=Label(form,text="Publisher")
namP.grid(column=0,row=4)
PnameTxt=Entry(form,width=20)
PnameTxt.grid(column=1,row=4)

cnt=Label(form,text="Count")
cnt.grid(column=0,row=5)
Bcount=Entry(form,width=20)
Bcount.grid(column=1,row=5)
#_________________________________assign to variable_________
def insToDb():
	name1=str(NameTxt.get())
	desc=str(bDiscr.get())
	author=str(AnameTxt.get())
	publisher=str(PnameTxt.get())
	count=str(Bcount.get())
	print(name1,desc,author,publisher,count)

	#_____________________Inserting into Database________connection_________________________

	dbCon=mysql.connector.connect(host="localhost",user="root",password="",database="data2")
	cursor=dbCon.cursor()
	insQ="INSERT INTO book(name,descrp,author,publisher,count) VALUES(%s,%s,%s,%s,%s)"
	datas=(name1,desc,author,publisher,count)
	print(datas)
	cursor.execute(insQ,datas)
	dbCon.commit()
	messagebox.showinfo('successfull','successfully added data')


btn=Button(form,text="Submit",command=insToDb)
btn.grid(column=1,row=6)

form.mainloop()



