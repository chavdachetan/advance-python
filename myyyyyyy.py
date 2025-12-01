from tkinter import *
from tkinter import messagebox,ttk 
import mysql.connector as sq
conn = sq.connect(host="localhost",user="root",password="",database="somnath")
cursor = conn.cursor()
def init_db():
    
    cursor.execute(""" 
    CREATE TABLE if not exists  Product_Items(id int primary key auto_increment,
                                name varchar(50),
                                price int)""")
    
init_db()
root=Tk()
gp1=LabelFrame(root,text="For Record Insert",width=500,height=200)
gp1.pack(padx=20,pady=20,fill="x",expand=False)

lbl1=Label(gp1,text="Name")
lbl1.place(x=20,y=30)
e1=Entry(gp1)
e1.place(x=90,y=30)

lbl2=Label(gp1,text="Price")
lbl2.place(x=20,y=80)
e2=Entry(gp1)
e2.place(x=90,y=80)

def Save_Records():
    nm = e1.get()
    pr = e2.get()

    e1.focus()
    if(nm=="" and pr == ""):
        messagebox.showinfo("Error","Please input some values")
    else:
        cursor.execute("insert into Product_Items(name,price)values(%s,%s)",(nm,pr))
        conn.commit()
        tree.insert("",END,values=(cursor.lastrowid,nm,pr))
                
        
          
btn1 = Button(gp1,text="Save",command=Save_Records)
btn1.place(x=90,y=120) 

gp2=LabelFrame(root,text="Show Information",width=500,height=200)
gp2.pack(padx=20,pady=20,fill="x",expand=False)

tree = ttk.Treeview(gp2,columns=("id","name","price"),show="headings")
tree.heading("id",text="Product ID")
tree.heading("name",text="NAme")
tree.heading("price",text="PRice")
tree.column(column=0,width=60,anchor="center")
tree.column(column=1,width=100,anchor="center")
tree.column(column=2,width=100,anchor="center")
tree.pack(padx=10,pady=10,fill="both",expand=False)

def Show_Records():
    
    cursor.execute("select * from Product_Items")
    rows=cursor.fetchall()
    for row in rows:
        
        tree.insert(parent="",index="end",values=row)
   
Show_Records()

gp3=LabelFrame(root,text="Operation Info",width=500,height=100)
gp3.pack(padx=20,pady=20,fill="both",expand=False)

def delete_record():
    get_id = tree.item(tree.focus())
    if(get_id["values"]==""):
        messagebox.showwarning("Warning","Select Record")   
    else:
        record_id = get_id["values"][0]
        dele=messagebox.askquestion("warning","do you want to delete this records")
        if(dele=="yes"):
            cursor.execute("delete from Product_Items where id=%s",(record_id,))
            conn.commit()
                       
            messagebox.showinfo("information","record delete successfully")
            tree.delete(tree.focus())
  

btn2 = Button(gp3,text="Delete",command=delete_record)
btn2.place(x=30,y=10)

def update_record():
    row = tree.item(tree.focus())
    if(row["values"] == ""):
        messagebox.showwarning("Warning","Select Record")
        return 
    else:
        id1 = row["values"][0]
        nm1 = row["values"][1]
        pr1 = row["values"][2]
        
        top = Toplevel(root)
        top.geometry("300x300")
        
        l1 = Label(top,text="Name")
        l1.place(x=20,y=30)
        entry1 = Entry(top)
        entry1.place(x=80,y=30)

        l2 = Label(top,text="Price")
        l2.place(x=20,y=80)
        entry2 = Entry(top)
        entry2.place(x=80,y=80)

        entry1.insert(0,nm1)
        entry2.insert(0,pr1)

        def rec_update():
            nm2 = entry1.get()
            pr2 = entry2.get()
            cursor.execute("update Product_Items set name=%s,price=%s where id=%s",(nm2,pr2,id1))
            conn.commit()
            
            messagebox.showinfo("information","record update successfully")
            tree.item(tree.focus(),values=(id1,nm2,pr2))
        btn4 = Button(top,text="Update",command=rec_update)
        btn4.place(x=80,y=150)


        top.mainloop()
btn3 = Button(gp3,text="Edit",command=update_record)
btn3.place(x=100,y=10)


root.geometry("500x730")
root.mainloop()