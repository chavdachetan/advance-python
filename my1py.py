from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk

def init():
    con=sq.connect("first1.db")
    cur=con.cursor()
    cur.execute("create table if not exists rano(id integer primary key autoincrement,name text,price real)")
    con.commit()
    cur.close()
    con.close()
init()