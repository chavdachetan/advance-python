from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox

root=Tk()
root.geometry("500x500")

lb1=LabelFrame(root,text="Insrt Record",height=180,width=300)
lb1.pack(fill="both")

tree=ttk.Treeview(lb1,columns=("Id","Name","City"),show="headings")
tree.heading("Id",text="ID",anchor=CENTER)
tree.heading("Name",text="NAME",anchor=CENTER)
tree.heading("City",text="CITY",anchor=CENTER)

tree.column("Id",width=30,anchor=CENTER)
tree.column("Name",width=80,anchor=CENTER)
tree.column("City",width=80,anchor=CENTER)
tree.pack(fill="both")


with open("CD.txt","r",newline="")as f:
    row=csv.reader(f)
    for i in row:tree.insert("",END,values=[i])

root.mainloop()