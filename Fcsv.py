from tkinter import *
from tkinter import ttk,messagebox,filedialog
import csv

root=Tk()
root.title("FILE EXAMPLE")

def insert():
    delimiter = e2.get()
    header = e3.get()
    encoding = e4.get()
    filepath = filedialog.askopenfilename(filetypes=[("CSV File","*.csv")])
    
    e1.delete(0, END)
    e1.insert(0, filepath)
    path = e1.get()

    tx1.delete("1.0", END)

    with open(path, "r", encoding=encoding, newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)

        if header == "no":
            next(reader)

        for row in reader:
            tx1.insert(END, str(row)+"\n")

def write_data():
    delimiter = e2.get()
    encoding = e4.get()
    get_data=tx1.get("1.0",END).split("\n")

    filepath=filedialog.asksaveasfilename(defaultextension=".csv")

    with open(filepath,"w",encoding=encoding,newline="") as f:
        writer=csv.writer(f)
        for i in get_data:
            if i.strip():   
                writer.writerow(i.split(","))

abc=StringVar(value="yes")
lb1=Label(root,text="CSV FILE")
lb1.place(x=10,y=20)
e1=Entry(root,width=50)
e1.place(x=80,y=20)

bt1=Button(root,text="BROWSE",command=insert)
bt1.place(x=390,y=17)


lb2=Label(root,text="Delimiter")
lb2.place(x=10,y=60)
e2=Entry(root)
e2.insert(0,",")
e2.place(x=80,y=60)


lb3=Label(root,text="hedding")
lb3.place(x=10,y=100)
e3=ttk.Combobox(root,values=("yes","no"),textvariable=abc)
e3.place(x=80,y=100)


lb4=Label(root,text="encoding")
lb4.place(x=10,y=140)
e4=Entry(root)
e4.insert(0,"utf-8")
e4.place(x=80,y=140)


gp1=LabelFrame(root,text="VIEW RECORDS",height=400,width=680)
gp1.place(x=10,y=190)

tx1=Text(gp1,width=70)
tx1.pack(fill="both",padx=10,pady=10)

bt1=Button(root,text="Write",command=write_data)
bt1.place(x=20,y=620)

root.geometry("700x700")
root.mainloop()
