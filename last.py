from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox

root=Tk()
root.geometry("500x500")

lb1=LabelFrame(root,text="Insrt Record",height=180,width=300)
lb1.pack(fill="both")

lbl1=Label(lb1,text="Id")
lbl1.place(x=20,y=20)
txt1=Entry(lb1)
txt1.place(x=60,y=20)

lbl2=Label(lb1,text="Name")
lbl2.place(x=20,y=60)
txt2=Entry(lb1)
txt2.place(x=60,y=60)

lbl3=Label(lb1,text="City")
lbl3.place(x=20,y=100)
txt3=Entry(lb1)
txt3.place(x=60,y=100)

def Insertt():
    idd=txt1.get()
    nm=txt2.get()
    ct=txt3.get()

    if(idd=="" or nm=="" or ct==""):
        messagebox.showwarning("Warning","Input Values!")
    else:
        tree.insert("",END,values=(idd,nm,ct))
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt1.focus()
        messagebox.showinfo("Information","Record Inserted.")
        with open("CD.txt","a",newline="")as f:
            row=csv.writer(f)
            rows=row.writerows([idd,nm,ct])
            for i in rows:
                tree.insert("",0,values=i)

btn=Button(lb1,text="Submit",command=Insertt)
btn.place(x=60,y=130)

tree=ttk.Treeview(root,columns=("Id","Name","City"),show="headings")
tree.heading("Id",text="ID",anchor=CENTER)
tree.heading("Name",text="NAME",anchor=CENTER)
tree.heading("City",text="CITY",anchor=CENTER)

tree.column("Id",width=30,anchor=CENTER)
tree.column("Name",width=80,anchor=CENTER)
tree.column("City",width=80,anchor=CENTER)
tree.pack(fill="both")

root.mainloop()