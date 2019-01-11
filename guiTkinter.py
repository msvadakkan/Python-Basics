import tkinter 

window=Tk()
window.title("hello")
#setting windowFrameSize 
window.geometry('320x200')
test=Label(window,text="hello")#Label declaration
test.grid(column=0,row=0)#Label alignment using grid_layout
test1=Label(window,text="hello",font=("Arial Bold",50))#tlabel text tize setting
test1.grid(column=0,row=2)
txt=Entry(window,width=10)#textBox or entry box 
txt.grid(column=0,row=5)
# buttonAction function Definition
def btnAction():
	vr=str(txt.get())#read text from text box
	test1.configure(text=vr) #rest label text or configure the label text

btn=Button(window,text="Set",command=btnAction)
btn.grid(column=0,row=3)

btn1=Button(window,text="Set2",bg="orange",fg="red")
btn1.grid(column=0,row=4)

window.mainloop()
