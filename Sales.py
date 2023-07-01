#Sales.py
from tkinter import *
from tkinter import messagebox,ttk
from tkcalendar import Calendar
import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='achuadivava@1438',database='airinfo')
x=con.cursor()
SALES=Tk()
SALES.config(bg='#191970')
def back():
    SALES.destroy()
    import First_pg
SALES.state('zoomed')
user_label=Label(SALES,text='USERNAME',fg='white',bg='#191970',font=('Times Roman','20'))
user_label.pack(pady=30)
user=Entry(SALES,font=('','20'))
user.pack(padx='50')
pass_label=Label(SALES,text='PASSWORD',fg='white',bg='#191970',font=('Times Roman','20'))
pass_label.pack(pady=30)
passw=Entry(SALES,font=('','20'),show='*')
passw.pack()
def check():
    n=user.get()
    p=passw.get()
    query='select * from salespass where usern="{}" and passw ="{}"'.format(n,p)
    x.execute(query)
    y=x.fetchone()
    if n=='' or y==None:
        messagebox.showwarning('Error','Invalid Username')
    elif p=='':
        messagebox.showerror('Error','Invalid Password')
    else:
        import sales_2
r1=Radiobutton(SALES,text='SUBMIT',font=('',30),command=check,relief='solid')
r1.pack(side='right',pady=30,padx=10)
r2=Radiobutton(SALES,text=' HOME ',font=('',30),command=back,relief='solid')
r2.pack(side='left',pady=30,padx=10)
SALES.mainloop()
