from tkinter import *
from tkinter import ttk, messagebox
import csv
import os

root = Tk()
root.title("Student Attendance System")
root.geometry("700x550")

attendance_file = "attendance.csv"

# ------------------ CREATE CSV FILE IF NOT EXISTS ------------------
if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll No", "Name", "Status"])  # Header


# ------------------ ADD STUDENT FUNCTION ------------------
def add_student():
    roll = e_roll.get()
    name = e_name.get()

    if roll == "" or name == "":
        messagebox.showwarning("Warning", "Please enter Roll No & Name")
        return

    tree.insert("", END, values=(roll, name, "Not Marked"))

    e_roll.delete(0, END)
    e_name.delete(0, END)


# ------------------ MARK ATTENDANCE ------------------
def mark_attendance():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a student")
        return

    status = attendance_var.get()
    values = list(tree.item(selected, "values"))
    values[2] = status
    tree.item(selected, values=values)


# ------------------ SAVE TO CSV ------------------
def save_data():
    rows = tree.get_children()

    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll No", "Name", "Status"])
        
        for row in rows:
            writer.writerow(tree.item(row, "values"))

    messagebox.showinfo("Success", "Attendance Saved Successfully!")


# ------------------ LOAD DATA ------------------
def load_data():
    for item in tree.get_children():
        tree.delete(item)

    with open(attendance_file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            tree.insert("", END, values=row)


# ------------------ GUI DESIGN ------------------

# --- Student Input Frame ---
frame = LabelFrame(root, text="Add Student", padx=10, pady=10)
frame.pack(fill="x", padx=10, pady=10)

Label(frame, text="Roll No:").grid(row=0, column=0)
e_roll = Entry(frame)
e_roll.grid(row=0, column=1, padx=10)

Label(frame, text="Name:").grid(row=0, column=2)
e_name = Entry(frame)
e_name.grid(row=0, column=3, padx=10)

Button(frame, text="Add", command=add_student).grid(row=0, column=4, padx=10)


# --- Attendance Marking ---
attendance_var = StringVar(value="Present")

frame2 = LabelFrame(root, text="Attendance", padx=10, pady=10)
frame2.pack(fill="x", padx=10)

Radiobutton(frame2, text="Present", variable=attendance_var, value="Present").pack(side=LEFT, padx=10)
Radiobutton(frame2, text="Absent", variable=attendance_var, value="Absent").pack(side=LEFT, padx=10)

Button(frame2, text="Mark Attendance", command=mark_attendance).pack(side=LEFT, padx=20)


# --- TreeView Table ---
frame3 = LabelFrame(root, text="Attendance Records", padx=10, pady=10)
frame3.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("roll", "name", "status")
tree = ttk.Treeview(frame3, columns=columns, show="headings")
tree.heading("roll", text="Roll No",anchor=CENTER)
tree.heading("name", text="Name",anchor=CENTER)
tree.heading("status", text="Status",anchor=CENTER)

tree.pack(fill="both", expand=True)


# --- Save & Load Buttons ---
frame4 = Frame(root)
frame4.pack(fill="x", pady=10)

Button(frame4, text="Save", width=15, command=save_data).pack(side=LEFT, padx=50)
Button(frame4, text="Load", width=15, command=load_data).pack(side=RIGHT, padx=50)

root.mainloop()
