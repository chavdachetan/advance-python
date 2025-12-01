from tkinter import *
from tkinter import ttk
import csv

root=Tk()
root.title("sir exampale ")


name = StringVar(value="yes");
lb1=Label(root,text="file name")
lb1.place(x=20,y=20)
e1=Entry(root)
e1.place(x=80,y=20)

b1=Button(root,text="browse")
b1.place(x=210,y=18)

lb2=Label(root,text="division")
lb2.place(x=20,y=50)
e2=Entry(root)
e2.insert(END,",")
e2.place(x=80,y=50)

lb3=Label(root,text="encoding")
lb3.place(x=20,y=80)
e3=Entry(root)
e3.insert(END,"udf-8")
e3.place(x=80,y=80)

lb4=Label(root,text="heading")
lb4.place(x=20,y=110)
e4=ttk.Combobox(root,textvariable=name,values=("yes","no"))
e4.place(x=80,y=110)

root.geometry("600x600")
root.mainloop()
