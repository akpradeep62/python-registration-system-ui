import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def add():
    studid = t1.get()
    studname = t2.get()
    coursename = t3.get()
    fee   = t4.get()

    mysql = mysql.connector.connect(host= "sql113.epizy.com",user="	epiz_31736917",password="3Ln4AeGLnqjIv",database="epiz_31736917_student")
    mydb = mysql.cursor()
    try:
       sql = "INSERT INTO  records (stdid,stdname,course,fee) VALUES(%s, %s, %s, %s)"
       val = (studid,studname,coursename,fee)
       mysql.execute(sql, val)
       mydb.commit()
       lastid = mydb.lastrowid
       messagebox.showinfo("information", "Employee inserted successfully...")
       t1.delete(0, END)
       t2.delete(0, END)
       t3.delete(0, END)
       t4.delete(0, END)
       t1.focus_set()
    except Exception as e:
       print(e)
       mydb.rollback()
       mydb.close()
root = Tk()
root.geometry("800x500")
global t1
global t2
global t3


tk.Label(root,text="student registration",fg="black",font=(None,30)).place(x=400,y=5)

tk.Label(root,text="student ID").place(x=10,y=10)
Label(root,text="student name").place(x=10,y=40)
Label(root,text="course").place(x=10,y=70)
Label(root,text="fee").place(x=10,y=100)


t1= Entry(root)
t1.place(x=140,y=10)


t2= Entry(root)
t2.place(x=140,y=40)

t3= Entry(root)
t3.place(x=140,y=70)

t4 = Entry(root)
t4.place(x=140,y=100)

Button(root,text="add",height=3 ,width=13).place(x=30,y=130)
Button(root,text="update",height=3,width=13).place(x=140,y=130)
Button(root,text="Delete",height=3,width=13).place(x=250,y=130)


cols =('id','stdname','course','fee')
listBox = ttk.Treeview(root,columns=cols,show="headings")


for col in cols:
    listBox.heading(col,text=col)
    listBox.grid(row=1,column=0,columnspan=2)
    listBox.place(x=10,y=200)
root.mainloop()








