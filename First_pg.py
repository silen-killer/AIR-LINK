#First_pg.py
from tkinter import *
from tkinter import messagebox
import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='achuadivava@1438',database='airinfo')
x=con.cursor()
#CREATING TKINTER WINDOW
main=Tk()
main.state('zoomed')
main.config(bg='#191970')
b1=Button(main,text='AirLink InfoTech',font=('Times Roman Bold',60))
b1.pack(pady=100)
#COMMAND FOR NEXT PAGE
def _1():
    def nxt():
        u=user.get()
        p=passw.get()
        query='select emp_no from salespass where usern="{}" and passw="{}"'.format(u,p)
        query1='select emp_no from hrpass where usern="{}" and passw="{}"'.format(u,p)
        x.execute(query)
        f=x.fetchone()
        x.execute(query1)
        g=x.fetchone()
        if u=='':           #IF USERNAME IS NOT ENTERED
            messagebox.showerror('Error','Invalid username')
        elif p=='':         #IF PASSWORD IS NOT ENTERED
            messagebox.showerror('Error','Invalid password')
        elif f==None and g==None:
            messagebox.showerror('Error','Incorrect Username or Password')
        else:
            user_label.destroy(),user.destroy(),pass_label.destroy()
            passw.destroy(),btn.destroy()
            #COMMAND FOR HR PAGE
            def hr_pg():
                m.destroy()
                import HR      #IMPORTING HR.py 
                #COMMAND FOR SALES PAGE
            def sales_pg():
                m.destroy()
                import Sales   #IMPORTING Sales.py 
            Label(m,text='SELECT DEPARTMENT',fg='white',bg='#191970',font=('',50)).pack()
            Button(m,text="HR",command=hr_pg,font=('',40),relief='solid').pack(ipadx=130,pady=150)
            Button(m, text="Sales",command=sales_pg,font=('',40),relief='solid').pack(ipadx=100)
    main.destroy()
    m=Tk()
    m.state('zoomed')
    m.config(bg='#191970')
    user_label=Label(m,text='USERNAME',fg='white',bg='#191970',font=('','20'))
    user_label.pack(pady=30)
    user=Entry(m,font=('',20))
    user.pack(padx=50)
    pass_label=Label(m,text='PASSWORD',fg='white',bg='#191970',font=('',20))
    pass_label.pack(pady=30)
    passw=Entry(m,font=('','20'),show='*')
    passw.pack()
    btn=Button(m,text='NEXT',font=('',40),relief='solid',command=nxt)
    btn.pack(pady=30)
    m.mainloop()
#COMMAND TO QUIT THE PROGRAM
def quit_pg():
    mb=messagebox.askquestion('quit','Are you sure that you want to quit')
    if mb=='yes':
        main.destroy()
#CREATING BUTTONS 
b2=Button(main,text='ENTER',font=('',30),command=_1,relief='solid')
b2.place(relx=0.85,rely=0.8)
b3=Button(main,text='QUIT',font=('',30),command=quit_pg,relief='solid')
b3.place(rely=0.8,relx=0.03)
main.mainloop()
