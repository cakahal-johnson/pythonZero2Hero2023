import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
# pip install mysqlclient
# pip install mysql-connector-python


# definition for clear ends
def Delete(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e1.insert(0, select['stname'])
    e1.insert(0, select['course'])
    e1.insert(0, select['fee'])


# for saving student in our database
def save():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="pydb")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO pydata (id, stname, course, fee) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)

        mycursor.execute(sql, val)
        mysqldb.commit()

        lastid = mycursor.lastrowid
        messagebox.showinfo("Information", "Record inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="pydb")
    mycursor = mysqldb.cursor()

    try:
        sql = "update pydata set stname = %s, course = %s, fee =%s where id= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()

        lastid = mycursor.lastrowid
        messagebox.showinfo("Information", "Record Updated successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="pydb")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from pydata where id=%s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Delete Successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="pydb")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id, stname, course, fee FROM pydata")
    records =mycursor.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()


# we design the app
root = tk.Tk()
root.title("Python database class project")
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Student Registration Records", fg="black", font=(None, 30)).place(x=400, y=5)

tk.Label(root, text="Registration ID: ").place(x=10, y=10)
tk.Label(root, text="Student Name: ").place(x=10, y=40)
tk.Label(root, text="Student Course: ").place(x=10, y=70)
tk.Label(root, text="Student Fee: ").place(x=10, y=100)

e1 = tk.Entry(root)
e1.place(x=140, y=10)

e2 = tk.Entry(root)
e2.place(x=140, y=40)

e3 = tk.Entry(root)
e3.place(x=140, y=70)

e4 = tk.Entry(root)
e4.place(x=140, y=100)

tk.Button(root, text="Save", height=3, width=13, command=save).place(x=30, y=130)     # remember to remove save ""
tk.Button(root, text="Update", height=3, width=13, command=update).place(x=140, y=130)  # remember remove to update ""
tk.Button(root, text="Delete", height=3, width=13, command=delete).place(x=250, y=130)    # remember remove to del ""

cols = ('id', 'stname', 'course', 'fee')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)


show()
listBox.bind('<Double-Button-1>', Delete)  # remember to remove del ""


root.mainloop()
