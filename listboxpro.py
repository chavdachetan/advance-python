import sqlite3 as sq
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("COLLAGE WORK")
frame=LabelFrame(root,text="For Record Insert",height=400,width=600)
frame.pack(pady=10)

lbl1=Label(frame,text="NAME")
lbl1.place(x=100,y=30)

txt1=Entry(frame)
txt1.place(x=150,y=30)

lbl2=Label(frame,text="city")
lbl2.place(x=100,y=60)

txt2=Listbox(frame)
txt2.place(x=150,y=60)
txt2.insert(END,"junagadh")
txt2.insert(END,"maliya")
txt2.insert(END,"jamanagar")
txt2.insert(END,"rajkot")
txt2.insert(END,"veraval")
txt2.insert(END,"keshod")
txt2.insert(END,"mangroad")

def init():
    con=sq.connect("my10.db")
    cur=con.cursor()
    cur.execute("create table if not exists stud(id integer primary key autoincrement,name text,city,text)")
    cur.close()
    con.close()
init()

def save():
    txt1.focus()
    name=txt1.get()
    selected=txt2.curselection()
    if(name=="" or not selected):
        messagebox.showinfo("validation error","please enter the field")
    else:   
        city=txt2.get(selected[0]) 
        con=sq.connect("my10.db")
        cur=con.cursor()
        cur.execute("insert into stud(name,city)values(?,?)",(txt1.get(),city))
        messagebox.showinfo("information","Record Inserted Successfully")
        con.commit()
        tree.insert("",END,values=(cur.lastrowid,name,city))
        txt1.delete(0,END)
        cur.close()
        con.close()
        refersh_tree()


btn1=Button(frame,text="SAVE",command=save)
btn1.place(x=150,y=300)


frame3=LabelFrame(root,text="View Record",height=200,width=600)
frame3.pack(pady=10)

tree=ttk.Treeview(frame3,columns=("ROLLNO","NAME","CITY"),show="headings")
tree.heading("ROLLNO",text="ROLLNO")
tree.heading("NAME",text="NAME")
tree.heading("CITY",text="CITY")

tree.column("ROLLNO",width=200)
tree.column("NAME",width=200)
tree.column("CITY",width=200)

tree.pack(fill="both",padx=10,pady=10)

def refersh_tree():
    for row in tree.get_children():
        tree.delete(row)
    con=sq.connect("my10.db")
    cur=con.cursor()
    cur.execute("select * from stud")
    rows=cur.fetchall()
    for row1 in rows:
        tree.insert("",END,values=row1)
    con.commit()
    cur.close()
    con.close()


def viewrecord():
    con=sq.connect("my10.db")
    cur=con.cursor()
    members=cur.execute("select * from stud")
    con.commit()
    for member in members:
        tree.insert("",END,values=member)

    cur.close()
    con.close()
   
viewrecord()



root.geometry("1200x1200")
root.mainloop()