import sqlite3 as sq
from tkinter import *
from tkinter import messagebox,ttk  

root=Tk()
root.title("LIST BOX EXAMPLE")

def init():
    con=sq.connect("ELCTRIC.db")
    cur=con.cursor()
    cur.execute("create table if not exists elctric(id integer primary key autoincrement,name text,price text,catagary text)")
    cur.close()
    con.close()
init()

fram1=LabelFrame(root,text="INSERT RECORDS",height=400,width=700,font="bold")
fram1.pack()

heading=Label(fram1,text="ELECTRIC ITEMS",font="bold")
heading.place(x=250,y=10)

lb1=Label(fram1,text="COMPANY NAME")
lb1.place(x=30,y=50)
e1=Entry(fram1)
e1.place(x=140,y=50)

lb2=Label(fram1,text="PRICE")
lb2.place(x=30,y=80)
e2=Entry(fram1)
e2.place(x=140,y=80)

abc=StringVar(value="SELECT")
lb3=Label(fram1,text="CATAGARY")
lb3.place(x=30,y=110)
e3=ttk.Combobox(fram1,width=17,values=("MOBILE","TV","LAPTOPS"),textvariable=abc)
e3.place(x=140,y=110)

list1=Listbox(fram1)
list1.insert(END,"MOBILE")
list1.insert(END,"TV")
list1.insert(END,"LAPTOPS")
list1.place(x=400,y=50)

def Insert_Record():
    nm=e1.get()
    ct=e2.get()
    sm=e3.get()

    if(nm=="" or ct=="" or sm=="SELECT"):
        messagebox.showerror("error","please enter the field")
    else:
        con=sq.connect("ELCTRIC.db")
        cur=con.cursor()
        cur.execute("insert into elctric(name,price,catagary) values(?,?,?)",(nm,ct,sm))
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("information","record inserted")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.set("SELECT")
    
btn1=Button(fram1,text="ADD",command=Insert_Record)
btn1.place(x=140,y=170)

fram2=LabelFrame(root,text="VIEW RECORDS",height=400,width=700,font="bold")
fram2.pack(padx=10)

tree=ttk.Treeview(fram2,columns=("ID","COMPANY NAME","PRICE","CATAGARY"),show="headings",)

tree.heading("ID",text="ID",anchor="center")
tree.heading("COMPANY NAME",text="COMPANY NAME",anchor="center")
tree.heading("PRICE",text="PRICE",anchor="center")
tree.heading("CATAGARY",text="CATAGARY",anchor="center")

tree.column("ID",width=100,anchor="center")
tree.column("COMPANY NAME",width=150,anchor="center")
tree.column("PRICE",width=150,anchor="center")
tree.column("CATAGARY",width=150,anchor="center")

tree.pack(fill="both",padx=10,pady=10)

def View_Records():
    select=list1.curselection()
    if not select:
        messagebox.showerror("error","please select data")
    else:
        nm=list1.get(select[0])
        con=sq.connect("ELCTRIC.db")
        cur=con.cursor()
        cur.execute("select * from elctric where catagary=?",(nm,))
        row=cur.fetchall()

        for item in tree.get_children():
            tree.delete(item)

        for rows in row:
            tree.insert("",END,values=rows)
        con.commit()
        cur.close()
        con.close()
        
btn2=Button(fram1,text="VIEW",command=View_Records)
btn2.place(x=410,y=220)

root.geometry("900x700+10+10")
root.mainloop()