#HR.py
from tkinter import *
from tkinter import messagebox,ttk
import sqlite3

hr=Tk()
hr.attributes('-fullscreen',True)
hr.config(bg='#191970')

# Connecting to SQLite database
con = sqlite3.connect('airinfo.db')
x = con.cursor()

# back
def back():
    hr.destroy()
    from First_pg import _1

#Username
user_label=Label(hr,text='USERNAME',fg='white',bg='#191970',font=('',25))
user_label.pack(pady=30)
user=Entry(hr,font=('',30))
user.pack(padx=50)

#password
pass_label=Label(hr,text='PASSWORD',fg='white',bg='#191970',font=('',25))
pass_label.pack(pady=30)
passw=Entry(hr,font=('',30),show='*')
passw.pack()

#next page
def check():
    n=user.get()       #USERNAME
    p=passw.get()   #PASSWORD
    if n=='':           #IF USERNAME IS NOT ENTERED
        messagebox.showerror('Error','Invalid username')
    elif p=='':         #IF PASSWORD IS NOT ENTERED
        messagebox.showerror('Error','Invalid password')
    else:
        query='select * from hrpass where usern="{}" and passw="{}"'.format(n,p)
        x.execute(query)
        y=x.fetchone()
        if y==None:  #IF USERNAME OR PASSWORD DOESN'T EXIST IN TABLE
            messagebox.showerror('Error','Incorrect Username or Password')
        else:
            hr.destroy()
            import HR_2  #IMPORTING HR_2.py

submit_btn=Radiobutton(hr,text='SUBMIT',font=('',20),command=check,relief='solid')
submit_btn.pack(side='right',pady=10,ipady=30)
back_btn=Radiobutton(hr,text=' HOME ',font=('',20),command=back,relief='solid')
back_btn.pack(side='left',pady=10,ipady=30)
hr.mainloop()
