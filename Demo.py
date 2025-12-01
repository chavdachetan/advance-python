from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk

def init():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.execute("""create table if not exists product(id integer primary key autoincrement,name text,price integer)""")
    cur.close()
    con.close()
init()

root=Tk()
lb=LabelFrame(root,text="Insert Record",height=180,width=450)
lb.pack(fill="both")

lbl1=Label(lb,text="Name")
lbl1.place(x=20,y=20)
e1=Entry(lb)
e1.place(x=80,y=20)

lbl2=Label(lb,text="Price")
lbl2.place(x=20,y=50)
e2=Entry(lb)
e2.place(x=80,y=50)

lbl2=Label(lb,text="Catagory")
lbl2.place(x=20,y=80)
e110=Entry(lb)
e110.place(x=80,y=80)

def Insert_record():
    nm=e1.get()
    pc=e2.get()
    ca=e110.get()
    if(nm=="" or pc=="" or ca==""):
        messagebox.showinfo("Error","Plese Fill Up...")
    else:
        con=sq.connect("my1.db")
        cur=con.cursor()
        cur.execute("INSERT INTO product(name,price,catagary)values(?,?,?)",(e1.get(),e2.get(),e110.get()))
        con.commit()
        cur.close()
        con.close()
        e1.delete(0,END)
        e2.delete(0,END)
        e1.focus()
        messagebox.showinfo("message","Record Inserted...")
        viewrecord()

btn1=Button(lb,text="Save",command=Insert_record)
btn1.place(x=80,y=110)

lb1=LabelFrame(root,text="Search Record",height=100,width=400)
lb1.pack(fill="both")

lbl3=Label(lb1,text="Name")
lbl3.place(x=20,y=20)
e3=Entry(lb1)
e3.place(x=80,y=20)

def Search_record():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.execute("select * from product where name=?",(e3.get(),))
    row=cur.fetchone()
    lb4=Label(lb1,text=row[0])
    lb4.place(x=20,y=40)

    lb5=Label(lb1,text=row[1])
    lb5.place(x=80,y=40)

    lb6=Label(lb1,text=row[2])
    lb6.place(x=140,y=40)
    con.commit()

    cur.close()
    con.close()
    messagebox.showinfo("information","Record found...")    

btn1=Button(lb1,text="Search",command=Search_record)
btn1.place(x=220,y=17)

lb2=LabelFrame(root,text="View Record",height=150,width=600)
lb2.pack(fill="both")

tree=ttk.Treeview(lb2,columns=("id","price","catagary"))
tree.pack(fill=BOTH)

tree.heading("#0", text="Product Name", anchor=W)
tree.heading("id",text="ID")

tree.heading("price",text="Price")
tree.heading("catagary",text="CATAGORY")

tree.column("#0", width=150, anchor=W)

p1=tree.insert("",END,text="Electronics",open=True)  
p2=tree.insert("",END,text="Furniture",open=True)
p3=tree.insert("",END,text="Stationery",open=True)  

def viewrecord():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.execute("select * from product where catagary=?",("Electronics",))
    perent1=cur.fetchall()

    for row in perent1:
        tree.insert(p1,END,text=row[1],values=[row[0],row[2],row[3]])

    cur.execute("select * from product where catagary=?",("Furniture",))
    perent2=cur.fetchall()
    for row in perent2:
        tree.insert(p2,END,text=row[1],values=[row[0],row[2],row[3]])

    cur.execute("select * from product where catagary=?",("Stationery",))
    perent3=cur.fetchall()
    for row in perent3:
        tree.insert(p3,END,text=row[1],values=[row[0],row[2],row[3]])

    con.commit()
    cur.close()
    con.close()

viewrecord()

def Edit_Record():
    top=Toplevel(root)
    top.title("Edit")
    lb=LabelFrame(top,text="Update Record",height=300,width=450)
    lb.pack(fill="both")

    lbl=Label(lb,text="Id")
    lbl.place(x=20,y=20)
    e=Entry(lb)
    e.place(x=80,y=20)
    
    lbl1=Label(lb,text="Name")
    lbl1.place(x=20,y=50)
    e1=Entry(lb)
    e1.place(x=80,y=50)

    lbl2=Label(lb,text="Price")
    lbl2.place(x=20,y=80)
    e2=Entry(lb)
    e2.place(x=80,y=80)

    def Editt():
        idd=e.get()
        nm=e1.get()
        pc=e2.get()
        if(idd=="" or nm=="" or pc==""):
            messagebox.showinfo("Error","Plese Fill Up...")
        else:
            con=sq.connect("my1.db")
            cur=con.cursor()
            cur.execute("update product set name=?,price=? where id=?",(nm,pc,e.get()))
            con.commit()
            cur.close()
            con.close()
            e.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e1.focus()
            messagebox.showinfo("message","Record Updatad...")
            top.destroy()

    btn1=Button(lb,text="Edit",command=Editt)
    btn1.place(x=80,y=110)

    top.geometry("500x500")
    top.mainloop()

f1=Frame(root,height=50,width=450)
f1.pack(fill="both")

btn2=Button(f1,text="Edit",command=Edit_Record)
btn2.place(x=20,y=20)

def Delete_Record():
    top=Toplevel(root)
    top.title("Edit")
    lb=LabelFrame(top,text="Delete Record",height=300,width=450)
    lb.pack(fill="both")

    lbl=Label(lb,text="Id")
    lbl.place(x=20,y=20)
    e=Entry(lb)
    e.place(x=80,y=20)

    def Deletee():
        idd=e.get()
        if(idd==""):
            messagebox.showinfo("Error","Plese Fill Up...")
        else:
            con=sq.connect("my1.db")
            cur=con.cursor()
            cur.execute("delete from product where id=?",(e.get(),))
            con.commit()
            cur.close()
            con.close()
            e.delete(0,END)
            e.focus()
            messagebox.showinfo("message","Record Deleted...")
            top.destroy()
    btn1=Button(lb,text="Delete",command=Deletee)
    btn1.place(x=80,y=110)

    top.geometry("500x500")
    top.mainloop()

btn2=Button(f1,text="Delete",command=Delete_Record)
btn2.place(x=80,y=20)

btn2=Button(f1,text="Export",command=Edit_Record)
btn2.place(x=160,y=20)

root.geometry("500x580")
root.mainloop()