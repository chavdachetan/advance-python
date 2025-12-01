from tkinter import *
from tkinter import ttk,messagebox,filedialog
import pandas
import csv

root=Tk()
root.title("FILE EXAMPLE")

def insert():
    delimiter = e2.get()
    header = int(e3.get())
    encoding = e4.get()
    filepath = filedialog.askopenfilename(filetypes=[("CSV File","*.csv")])
    df=pandas.read_csv(filepath,delimiter=delimiter,encoding=encoding,header=header)
    tx1.delete("1.0",END)
    tx1.insert(END,df.to_string(index=False))
    tx1.insert(END,df)

   
def write_data():
    delimiter = e2.get()
    encoding = e4.get()
    get_data=tx1.get("1.0",END).split("\n")

    filepath=filedialog.asksaveasfilename(defaultextension=".csv")

    df = pandas.DataFrame(get_data)
    df = df[0].str.split(delimiter, expand=True)
    df.to_csv(filepath, index=False, header=False,encoding=encoding)

abc=IntVar(value=0)
lb1=Label(root,text="pandas")
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
e3=ttk.Combobox(root,values=(0,1),textvariable=abc)
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