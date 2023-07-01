#HR_2.py
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as c
#CONNECTING MYSQL
con=c.connect(host='localhost',user='root',passwd='achuadivava@1438',database='airinfo')
x=con.cursor()
#CREATING NEW WINDOW
HR=Tk()
HR.state('zoomed')
HR.config(bg='#191970')
#TO EXIT THE PROGRAM
def end():
    mb=messagebox.askquestion('quit','Are you sure that you want to quit')
    if mb=='yes':
        HR.destroy()
#COMMAND TO GO BACK 
def home():
    HR.destroy()
    import sec_pg       #IMPORTING sec_pg.py
def nxt():
    ch=lb.index(lb.curselection())
    def bck():
        hr.destroy()
        HR.state('zoomed')
#TO ADD AN EMPLOYEE
    if ch==0:
        def nxt():
            def submit():
                u=usern.get()     #USERNAME
                p=passw.get()    #PASSWORD
                if u=='':          #IF NOTHING IS ENTERED 
                    messagebox.showerror('Error','Username not entered')
                elif p=='':
                    messagebox.showerror('Error','Password not entered')
                else:
                    if dpt=="hr":
                        query2="insert into hrpass values('{}','{}','{}')".format(emp_id,u,p)
                        x.execute(query2)
                        con.commit()        #INSERTING THE DATA INTO HRPASS TABLE
                    elif dpt=='sales':
                        query3="insert into salespass values('{}','{}','{}')".format(emp_id,u,p)
                        x.execute(query3)
                        con.commit()        #INSERTING THE DATA INTO SALESPASS TABLE
                    mb=messagebox.showinfo('','Added successfully')
                    HR.state('zoomed')
            emp_id=empid.get()            #EMPLOYEE ID
            emp_nm=empnm.get()       #EMPLOYEE NAME
            dpt=(dept.get()).lower()        #DEPARTMENT
            sly=sal.get()                       #SALARY
            j="select emp_no from employee where emp_no='{}'".format(emp_id)
            x.execute(j)
            k=x.fetchone()
            if k!=None or emp_id=='':   #IF EMPLOYEE ID IS NOT ENTERED OR ALREADY EXIST IN EMPLOYEE TABLE
                messagebox.showerror('Error','Invalid Employee ID')
            elif emp_nm=='':        #IF EMPLOYEE NAME IS NOT ENTERED
                messagebox.showerror('Error','Invalid Employee Name')
            elif sly=='':                 #IF SALARY IS NOT ENTERED       
                messagebox.showerror('Error','Invalid Salary')
            elif dpt not in ('hr','sales'):    #IF DEPARTMENT ENTERED IS NEITHER HR NOR SALES
                messagebox.showerror('Error','Invalid Department')
            else:
                query1="insert into employee values('{}','{}','{}',{})".format(emp_id,emp_nm,dpt,int(sly))
                x.execute(query1)
                con.commit()
                LABEL.destroy(),empid_label.destroy(),empnm_label.destroy(),dept_label.destroy(),sal_label.destroy()
                empid.destroy(),empnm.destroy(),dept.destroy(),sal.destroy(),nxt.destroy()
                usern_label=Label(hr,text='Username',fg='white',bg='#191970',font=('',25))
                usern_label.place(relx=0.025,rely=0.15)
                usern=Entry(hr,font=('',22))
                usern.pack(anchor='ne',padx=20,pady=95)
                passw_label=Label(hr,text='Password',fg='white',bg='#191970',font=('Times Roman',25))
                passw_label.place(relx=0.027,rely=0.34)
                passw=Entry(hr,font=('',22),show='*')
                passw.pack(anchor='ne',padx=20)
                add=Button(hr,text='ADD',font=('',40),command=submit,relief='solid')
                add.place(relx=0.85,rely=0.8)
        HR.state('withdraw')
        hr=Tk()
        hr.state('zoomed')
        hr.config(bg='#191970')
        LABEL=Label(hr,text='Add Employee',fg='white',bg='#191970',font=('',40))
        LABEL.place(x=0,y=0,relwidth=1)
        empid_label=Label(hr,text='Employee Id',fg='white',bg='#191970',font=('',25))
        empid_label.place(relx=0.025,rely=0.15)
        empid=Entry(hr,font=('',30))
        empid.pack(anchor='nw',padx=350,pady=95)
        empnm_label=Label(hr,text='Name of employee',fg='white',bg='#191970',font=('',25))
        empnm_label.place(relx=0.027,rely=0.34)
        empnm=Entry(hr,font=('',30))
        empnm.pack(anchor='nw',padx=350)
        sal_label=Label(hr,text='Salary',fg='white',bg='#191970',font=('',25))
        sal_label.place(relx=0.0325,rely=0.55)
        sal=Entry(hr,font=('',30))
        sal.pack(anchor='nw',padx=350,pady=95)
        dept_label=Label(hr,text='Department',fg='white',bg='#191970',font=('',25))
        dept_label.place(relx=0.04,rely=0.775)
        l=['HR','Sales']
        txt=StringVar()
        dept=ttk.Combobox(hr,textvariable=txt,font=('',30))
        dept['values']=l
        dept.current(0)
        dept.pack(anchor='nw',padx=350)
        nxt=Button(hr,text='NEXT',font=('',40),command=nxt,relief='solid')
        nxt.place(relx=0.85,rely=0.85)
        back=Button(hr,text='BACK',font=('',40),command=bck,relief='solid')
        back.place(relx=0.02,rely=0.85)
#Deleting an existing employee
    if ch==1:
        def submit():
            emp_id=empid.get()
            dpt=(dept.get()).lower()
            j="select emp_no from employee where emp_no='{}'".format(emp_id)
            x.execute(j)
            k=x.fetchone()
            if k==None or emp_id=='':   #IF EMPLOYEE ID IS NOT ENTERED OR ALREADY EXIST IN EMPLOYEE TABLE
                messagebox.showerror('Error','Invalid Employee ID')
            elif dpt not in ('hr','sales'):
                messagebox.showerror('Error','Invalid Department')
            else:
                if dpt=="hr":
                    query="delete from hrpass where emp_no='{}'".format(emp_id)
                    x.execute(query)
                    con.commit()
                    query1="delete from employee where emp_no='{}'".format(emp_id)
                    x.execute(query1)
                    con.commit()
                    mb=messagebox.showinfo('','Deleted successfully')
                elif dpt=='sales':
                    query="delete from salespass where emp_no='{}'".format(emp_id)
                    x.execute(query)
                    con.commit()
                    query1="delete from employee where emp_no='{}'".format(emp_id)
                    x.execute(query1)
                    con.commit()
                    mb=messagebox.showinfo('','Deleted successfully')
        HR.state('withdraw')
        hr=Tk()
        hr.state('zoomed')
        hr.config(bg='#191970')
        LABEL=Label(hr,text='Delete Employee',fg='white',bg='#191970',font=('Times Roman',40))
        LABEL.place(x=0,y=0,relwidth=1)
        empid_label=Label(hr,text='Employee Id',fg='white',bg='#191970',font=('Times Roman',25))
        empid_label.place(relx=0.025,rely=0.15)
        empid=Entry(hr,font=('',30))
        empid.pack(anchor='nw',padx=350,pady=95)
        dept_label=Label(hr,text='Department',fg='white',bg='#191970',font=('Times Roman',25))
        dept_label.place(relx=0.0325,rely=0.5)
        l=['HR','Sales']
        txt=StringVar()
        dept=ttk.Combobox(hr,textvariable=txt,font=('',30))
        dept['values']=l
        dept.current(0)
        dept.pack(anchor='nw',padx=350,pady=95)
        delete=Button(hr,text='DELETE',font=('',40),command=submit,relief='solid')
        delete.place(relx=0.8,rely=0.8)
        back=Button(hr,text='BACK',font=('',40),command=bck,relief='solid')
        back.place(relx=0.02,rely=0.8)
#Displaying the employee database
    if ch==2:
        hr=Tk()
        hr.state('zoomed')
        L=Label(hr,text='EMPLOYEE DATABASE',font=('',40))
        L.place(relwidth=1)
        L1=Label(hr,text='Employee ID',font=('',40),borderwidth=2,relief='solid')
        L1.place(rely=0.1,relx=0.01,relwidth=0.24)
        L2=Label(hr,text='Name',font=('',40),borderwidth=2,relief='solid')
        L2.place(rely=0.1,relx=0.251,relwidth=0.3)
        L3=Label(hr,text='Department',font=('',40),borderwidth=2,relief='solid')
        L3.place(rely=0.1,relx=0.5515,relwidth=0.27)
        L4=Label(hr,text='Salary',font=('',40),borderwidth=2,relief='solid')
        L4.place(rely=0.1,relx=0.823,relwidth=0.165)
        query="select * from employee order by name"
        x.execute(query)
        j=0.2
        for k in x:
            l1=Label(hr,text=k[0],font=('',30),borderwidth=2,relief='solid')
            l1.place(rely=j,relx=0.01,relwidth=0.24)
            l2=Label(hr,text=k[1],font=('',30),borderwidth=2,relief='solid')
            l2.place(rely=j,relx=0.251,relwidth=0.3)
            l3=Label(hr,text=k[2],font=('',30),borderwidth=2,relief='solid')
            l3.place(rely=j,relx=0.5515,relwidth=0.27)
            l4=Label(hr,text=k[3],font=('',30),borderwidth=2,relief='solid')
            l4.place(rely=j,relx=0.823,relwidth=0.165)
            j+=0.08
#Updating the salary package of a particular employee
    if ch==3:
        def submit():
            emp_id=empid.get()
            sly=sal.get()
            j="select emp_no from employee where emp_no='{}'".format(emp_id)
            x.execute(j)
            k=x.fetchone()
            if emp_id=='' or k==None: #IF EMPLOYEE ID IS NOT ENTERED OR ALREADY EXIST IN EMPLOYEE TABLE
                messagebox.showerror('Error','Invalid Employee ID')
            elif sly=='':    
                messagebox.showerror('Error','Invalid Salary')
            else:
                query="update employee set Salary={} where emp_no='{}'".format(int(sly),emp_id)
                x.execute(query)
                con.commit()
                mb=messagebox.showinfo('','Upadated successfully')
        HR.state('withdraw')
        hr=Tk()
        hr.state('zoomed')
        hr.config(bg='#191970')
        LABEL=Label(hr,text='Update Salary Package',fg='white',bg='#191970',font=('Times Roman',40))
        LABEL.place(x=0,y=0,relwidth=1)
        empid_label=Label(hr,text='Employee Id',fg='white',bg='#191970',font=('',25))
        empid_label.place(relx=0.025,rely=0.15)
        empid=Entry(hr,font=('',30))
        empid.pack(anchor='nw',padx=350,pady=95)
        sal_label=Label(hr,text='New Salary',fg='white',bg='#191970',font=('',25))
        sal_label.place(relx=0.04,rely=0.35)
        sal=Entry(hr,font=('',30))
        sal.pack(anchor='nw',padx=350)
        Button(hr,text='UPDATE',font=('',40),command=submit,relief='solid').place(relx=0.75,rely=0.8)
        back=Button(hr,text='BACK',font=('',40),command=bck,relief='solid')
        back.place(relx=0.02,rely=0.8)
#MAIN
label=Label(HR,text='SELECT FUNCTION',fg='white',bg='#191970',font=('',40))
label.pack()
lb=Listbox(HR,font=('',40),relief='solid')
lb.place(rely=0.2,relx=0.25,relheight=0.4)
lb.insert(0,' Add employee')
lb.insert(1,' Remove employee')
lb.insert(3," Update salary package")
lb.insert(2,' Display all employees')
slc=Button(HR,text='SELECT',font=('',30),command=nxt,relief='solid')
slc.place(relx=0.85,rely=0.8)
back=Button(HR,text='HOME',font=('',30),command=home,relief='solid')
back.place(rely=0.8,relx=0.03,relwidth=0.12)
Quit=Button(HR,text='QUIT',font=('',30),command=end,relief='solid')
Quit.place(rely=0.8,relx=0.4,relwidth=0.12)
HR.mainloop()
