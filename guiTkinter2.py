#comboBox and RadioButton
from tkinter import *
from tkinter import ttk
window=Tk()
window.title("hello")

cmb=ttk.Combobox(window)
cmb['value']=(1,2,3,4,5,"Text")#combo List 
cmb.current(1)#default selection 
chk=ttk.Checkbutton(window,text="select")
chk_state=BooleanVar()
chk_state.set(True)#set check state
chk=ttk.Checkbutton(window,text="Choose",var=chk_state)

chk.pack()
cmb.pack()
window.mainloop()