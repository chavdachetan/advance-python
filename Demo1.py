import sqlite3 as sq
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("COLLAGE WORK")
frame=LabelFrame(root,text="For Record Insert",height=200,width=600)
frame.pack(pady=10)

lbl1=Label(frame,text="NAME")
lbl1.place(x=100,y=30)

txt1=Entry(frame)
txt1.place(x=150,y=30)

lbl2=Label(frame,text="city")
lbl2.place(x=100,y=60)

txt2=Entry(frame)
txt2.place(x=150,y=60)

def save():
    txt1.focus()
    name=txt1.get()
    city=txt2.get()
    if(name=="" or city==""):
        messagebox.showinfo("validation error","please enter the field")
    else:    
        con=sq.connect("MY.db")
        cur=con.cursor()
        cur.execute("insert into stud(name,city)values(?,?)",(txt1.get(),txt2.get()))
        messagebox.showinfo("information","Record Inserted Successfully")
        con.commit()
        tree.insert("",END,values=(name,city))
        txt1.delete(0,END)
        txt2.delete(0,END)
        cur.close()
        con.close()
       


btn1=Button(frame,text="SAVE",command=save)
btn1.place(x=150,y=100)


frame2=LabelFrame(root,text="Search Records",height=200,width=600)
frame2.pack(pady=10)

lbl3=Label(frame2,text="Name")
lbl3.place(x=100,y=30)

txt3=Entry(frame2)
txt3.place(x=150,y=30)

def search():
    name=txt3.get()
    txt3.focus()
    if(name==""):
        messagebox.showinfo("Error","Please enter the Name")
    else:
        con=sq.connect("MY.db")
        cur=con.cursor()
        cur.execute("select * from stud where name=?",(name,))
        rows=cur.fetchone()
        con.commit()
        if rows is None:
            messagebox.showinfo("error","Record not Found")
        else:    
            lbl5=Label(frame2,text=rows[0])
            lbl5.place(x=10,y=140)
            lbl6=Label(frame2,text=rows[1])
            lbl6.place(x=60,y=140)
            lbl7=Label(frame2,text=rows[2])
            lbl7.place(x=120,y=140)
            txt3.delete(0,END)
            cur.close()
            con.close()



btn2=Button(frame2,text="SEARCH",command=search)
btn2.place(x=150,y=60)

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

def viewrecord():
    con=sq.connect("my1.db")
    cur=con.cursor()
    members=cur.execute("select * from stud")
    con.commit()
    for member in members:
        tree.insert("",END,values=member)
    cur.close()
    con.close()

#viewrecord()

frame4=Frame(root,height=80,width=600)
frame4.pack()

def edit():
    form1=Toplevel(root)
    form1.title("EDIT")

    framef1=LabelFrame(form1,text="EDIT Records",height=200,width=600)
    framef1.pack(pady=10)

    lbl13=Label(framef1,text="Rollno")
    lbl13.place(x=100,y=30)

    txt13=Entry(framef1)
    txt13.place(x=150,y=30)


    lbl11=Label(framef1,text="NAME")
    lbl11.place(x=100,y=60)

    txt11=Entry(framef1)
    txt11.place(x=150,y=60)

    lbl12=Label(framef1,text="city")
    lbl12.place(x=100,y=90)

    txt12=Entry(framef1)
    txt12.place(x=150,y=90)

    def edit_info():
        txt13.focus()
        name=txt11.get()
        city=txt12.get()
        rollno=txt13.get()
        con=sq.connect("MY.db")
        cur=con.cursor()
        if(name=="" or city=="" or rollno==""):
            messagebox.showinfo("Error","please enter the field")
        else:
            cur.execute("update stud set name=?,city=? where rollno=?",(name,city,rollno))
            if cur.rowcount==0:
                messagebox.showinfo("Error","Record not found")
                txt13.focus()
            else:
                messagebox.showinfo("information","Record update successfully")
                
                txt11.delete(0,END)
                txt12.delete(0,END)
                txt13.delete(0,END)
                con.commit()
                cur.close()
                con.close()
                form1.destroy()
                refersh_tree()
            
    

    btn11=Button(framef1,text="EDIT",command=edit_info)
    btn11.place(x=150,y=140)

    form1.geometry("800x300")
    

btn4=Button(frame4,text="Edit",command=edit)
btn4.place(x=10,y=30)


def delete():
    form2=Toplevel(root)
    form2.title("delete")

    framef2=LabelFrame(form2,text="DELETE Records",height=200,width=600)
    framef2.pack(pady=10)

    lbl21=Label(framef2,text="NAME")
    lbl21.place(x=100,y=60)

    txt21=Entry(framef2)
    txt21.place(x=150,y=60)

    
    def delete_info():
        txt21.focus()
        name=txt21.get()
        con=sq.connect("MY.db")
        cur=con.cursor()
        if(name=="" ):
            messagebox.showinfo("Error","please enter the field")
        else:
            cur.execute("delete from stud where name=?",(name,))
            if cur.rowcount==0:
                messagebox.showinfo("Error","Record not found")
                txt21.focus()
            else:
                messagebox.showinfo("information","Record delete successfully")
                
                txt21.delete(0,END)
                con.commit()
                cur.close()
                con.close()
                form2.destroy()
                refersh_tree()
            
    

    btn12=Button(framef2,text="DELETE",command=delete_info)
    btn12.place(x=150,y=140)

    form2.geometry("800x300")


btn5=Button(frame4,text="Delete",command=delete)
btn5.place(x=140,y=30)

btn6=Button(frame4,text="Export")
btn6.place(x=270,y=30)


root.geometry("1200x1200")
root.mainloop()