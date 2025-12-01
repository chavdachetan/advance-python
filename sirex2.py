import csv
from tkinter import *
from tkinter import ttk,messagebox

root=Tk()
root.title("tree view example")

frame=LabelFrame(root,text="insert record",height=200,width=800)
frame.pack(padx=20,pady=20)

id=Label(frame,text="ID")
id.place(x=20,y=30)
tx1=Entry(frame)
tx1.place(x=70,y=30)

name=Label(frame,text="NAME")
name.place(x=20,y=60)
tx2=Entry(frame)
tx2.place(x=70,y=60)


city=Label(frame,text="CITY")
city.place(x=20,y=90)
tx3=Entry(frame)
tx3.place(x=70,y=90)


def insert():
    idd=tx1.get()
    nm=tx2.get()
    ct=tx3.get()
    row=[idd,nm,ct]
    if(nm=="" or idd=="" or ct==""):
        messagebox.showerror("error","please enter the values")
    else:
        tree.insert("",END,values=(idd,nm,ct))
        tx1.delete(0,END)
        tx2.delete(0,END)
        tx3.delete(0,END)
       

        with open("data1.csv","w",newline="") as f:
            data=csv.writer(f)
            data.writerow(["ID","NAME","CITY"])
            data.writerow(row)
        messagebox.showinfo("information","RECORD INSERTED")     
            


btn1=Button(frame,text="SAVE",command=insert)
btn1.place(x=70,y=130)



tree=ttk.Treeview(root,columns=("id","name","city"),show="headings")

tree.heading("id",text="ID")
tree.heading("name",text="NAME")
tree.heading("city",text="CITY")

tree.column("id",width=30,anchor=CENTER)
tree.column("name",width=120,anchor=CENTER)
tree.column("city",width=120,anchor=CENTER)

tree.pack(padx=10,pady=10,fill="both")

root.geometry("700x700+70+70")
root.mainloop()