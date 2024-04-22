#sales_2.py
from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import Calendar
import graphit
import sqlite3

# Connecting to SQLite database
con = sqlite3.connect('airinfo.db')
x = con.cursor()

SALEs = Tk()
SALEs.config(bg='#191970')
SALEs.attributes('-fullscreen',True)

#TO EXIT THE PROGRAM
def end():
    mb=messagebox.askquestion('quit','Are you sure that you want to quit')
    if mb=='yes':
        SALEs.destroy()
def _0():
    def nxt():
        t=trans_no.get()
        f=flt.get()
        i=inc.get()
        def submit():
            d=date.get_date()
            query="select transacnr from sales where transacnr='{}'".format(t)
            x.execute(query)
            e=x.fetchone()
            if e!=None or t=='':
                messagebox.showerror('Error','Transaction no not entered')
            elif f=='':
                messagebox.showerror('Error','Flight Name not entered')
            elif i=='':
                messagebox.showerror('Error','Amount received after transaction not entered')
            elif d=='':
                messagebox.showerror('Error','Date not entered')
            else:
                query1="insert into sales values('{}','{}','{}',{})".format(t,d,f,i)
                x.execute(query1)
                con.commit()
                S.destroy()
                SALEs.attributes('-fullscreen',True)
        transno_label.destroy(),trans_no.destroy(),inc_label.destroy()
        inc.destroy(),flt_label.destroy(),flt.destroy()
        date_label=Label(S,text='Date',fg='white',bg='#191970',font=('',40))
        date_label.pack()
        date=Calendar(S,selectmode='day',date_pattern='y-mm-dd',font=('',30))
        date.pack()
        btn.config(text='Submit',command=submit)
        SALEs.state('withdraw')
    S=Tk()
    S.attributes('-fullscreen',True)
    S.config(bg='#191970')
    transno_label=Label(S,text='Transaction No',fg='white',bg='#191970',font=('',40))
    transno_label.place(relx=0.025,rely=0.02)
    trans_no=Entry(S,font=('',30))
    trans_no.pack(anchor='e',padx=10,pady=30)
    inc_label=Label(S,text='Ticket Amount',fg='white',bg='#191970',font=('',40))
    inc_label.place(relx=0.025,rely=0.18)
    inc=Entry(S,font=('',30))
    inc.pack(anchor='e',padx=10,pady=30)
    flt_label=Label(S,text='Name of Airline',fg='white',bg='#191970',font=('',40))
    flt_label.place(relx=0.025,rely=0.36)
    l=['AirIndia','Emirates','FlyDubai']
    txt=StringVar()
    flt=ttk.Combobox(S,textvariable=txt,font=('',30))
    flt['values']=l
    flt.current(0)
    flt.pack(anchor='e',padx=10,pady=30)
    btn=Button(S,text='CONTINUE',font=('',40),command=nxt,relief='solid')
    btn.place(rely=0.85,relx=0.4)

#Modify the sales of a particular transaction number
def _1():
    def submit():
        i=inc.get()
        t=transacnr.get()
        j="select transacnr from sales where transacnr='{}'".format(t)
        x.execute(j)
        k=x.fetchone()
        if i=='':
            messagebox.showerror('Error','New Income not entered')
        elif t=='' or k==None:
            messagebox.showerror('Error','Invalid Transaction No')
        else:
            query="update sales set SaleAmt={} where TransacNr='{}'".format(i,t)
            x.execute(query)
            con.commit()
            messagebox.showinfo('Success','Modified Successfully')
            modify.destroy()
    modify=Tk()
    modify.attributes('-fullscreen',True)
    modify.config(bg='#191970')
    l2=Label(modify,text='Modify the Sales of a Particular Transaction Number',font=('',40),fg='white',bg='#191970')
    l2.pack(fill='x')
    l1=Label(modify,bg='#191970',fg='white',text='Transaction No',font=('Times Roman',40))
    l1.place(relx=0.1,rely=0.2)
    transacnr=Entry(modify,font=('',22))
    transacnr.pack(anchor='ne',padx=100,pady=95)
    l3=Label(modify,bg='#191970',fg='white',text='New Income',font=('',40))
    l3.place(relx=0.1,rely=0.4)
    inc=Entry(modify,font=('',22))
    inc.pack(anchor='ne',padx=100)
    b=Button(modify,text='SUBMIT',font=('',40),command=submit,relief='solid')
    b.pack(side='bottom')

#Get the total sales of the year of
#         i.a flight            ii.airlink Infotech
def _2():
    sales=Tk()
    sales.config(bg='#191970')
    sales.attributes('-fullscreen',True)
    def flight():  #Of flight
        F=Tk()
        F.config(bg='#191970')
        F.attributes('-fullscreen',True)
        def nxt():
            f=flt.get()
            ye=yer.get()
            if f not in ('AirIndia','Emirates','FlyDubai'):
                messagebox.showerror('Error','Employee no not entered')
            elif ye not in ('2019','2020','2021'):
                messagebox.showerror('Error','Employee Name not entered')
            else:
                l3.destroy(),l1.destroy(),l2.destroy(),b1.destroy(),yer.destroy(),flt.destroy()
                query="select SaleAmt from sales where year(DateTransac)='{}' and FlightNm='{}'".format(ye,f)
                x.execute(query)
                y=x.fetchall()
                sum1=0
                for i in y:
                    sum1+=i[0]
                L=Label(F,text='The total sales of '+f+' for the year '+ye+' is ₹'+str(sum1),font=('',40),fg='white',bg='#191970')
                L.pack(anchor='center')
        l3=Label(F,text="Total Sales of an Airline for a Year",font=('Times Roman',40),fg='white',bg='#191970')
        l3.pack(fill='x')
        l1=Label(F,text='Name of the airline',fg='white',bg='#191970',font=('',40))
        l1.place(relx=0.1,rely=0.2)
        l=['AirIndia','Emirates','FlyDubai']
        txt=StringVar()
        flt=ttk.Combobox(F,textvariable=txt,font=('',30))
        flt['values']=l
        flt.current(0)
        flt.pack(anchor='ne',padx=100,pady=80)
        l2=Label(F,text='Year to be viewed',fg='white',bg='#191970',font=('',40))
        l2.place(relx=0.1,rely=0.4)
        yer=Entry(F,font=('',30))
        yer.pack(anchor='ne',padx=100,pady=10)
        b1=Button(F,text='NEXT',font=('',40),command=nxt,relief='solid')
        b1.pack(side='bottom',pady=20)
    def airlink():  #Of Airlink Infotech
        airlink=Tk()
        airlink.config(bg='#191970')
        airlink.attributes('-fullscreen',True)
        def nxt():
            year=yer.get()
            if year=='':
                messagebox.showerror('Error','Year to be viewed not entered')
            else:
                l1.destroy(),b1.destroy(),yer.destroy(),l.destroy()
                query="select SaleAmt from sales where year(DateTransac)='{}'".format(year)
                x.execute(query)
                y=x.fetchall()
                sum1=0
                for i in y:
                    sum1+=i[0]
                a=0.3*sum1
                Label(airlink,text="The total sales of Airlink Infotech\nfor the year "+year+" is ₹"+str(a),fg='white',bg='#191970',font=('',50)).pack(anchor='center')
        l=Label(airlink,text="Total sales of Airlink Infotech for a year",font=('',40),fg='white',bg='#191970')
        l.pack()
        l1=Label(airlink,text='Year to be viewed',fg='white',bg='#191970',font=('',40))
        l1.place(relx=0.1,rely=0.5)
        yer=Entry(airlink,font=('',30))
        yer.pack(padx=90,side='right')
        b1=Button(airlink,text='NEXT',font=('',40),command=nxt,relief='solid')
        b1.pack(side='bottom',pady=20)
    l1=Label(sales,text="Total Sales for a Year",fg='white',bg='#191970',font=('',40))
    l1.pack()
    b1=Button(sales,text='Of an airline',font=('',40),command=flight,relief='solid')
    b1.pack(pady=100,ipadx=90)
    b2=Button(sales,text='Of Airlink Infotech',font=('',40),command=airlink,relief='solid')
    b2.pack()

#Compare year's sales of different flights through graphs
def _3():
    YR=Tk()
    YR.config(bg='#191970')
    YR.attributes('-fullscreen',True)
    def nxt():
        yr=yer.get()
        if yr=='':
            messagebox.showerror('Error','Year to be viewed not entered')            
        else:
            query="select FlightNm, month(DateTransac),SaleAmt from sales where year(DateTransac)='{}'".format(yr)
            x.execute(query)
            y=x.fetchall()
            dict1={}
            for i in y:
                dict1[(i[0],i[1])]=i[2]
            A={}
            E={}
            F={}
            month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
            for i in month.values():
                A.setdefault(i,0)
                E.setdefault(i,0)
                F.setdefault(i,0)
            for i,j in dict1:
                if i=="AirIndia":
                    A[month[j]]+=dict1[(i,j)]
                elif i=='Emirates':
                    E[month[j]]+=dict1[(i,j)]
                else:
                    F[month[j]]+=dict1[(i,j)]
            AirIndia=list(A.values())
            Emirates=list(E.values())
            FlyDubai=list(F.values())
            graphit.bar(AirIndia,Emirates,FlyDubai)
    l1=Label(YR,text="Monthly sales comparison of\nairlines through graphs",fg='white',bg='#191970',font=('',40))
    l1.pack()
    l2=Label(YR,text='Year to be viewed',font=('Times Roman',40),fg='white',bg='#191970')
    l2.pack(pady=100)
    yer=Entry(YR,font=('',22))
    yer.pack()
    b1=Button(YR,text='SUBMIT',font=('',40),command=nxt,relief='solid')
    b1.pack(side='bottom',pady=20)

#Dispaly the sales database
def _4():
    db=Tk()
    db.attributes('-fullscreen',True)
    query="select * from sales"
    x.execute(query)
    y=x.fetchall()
    L=Label(db,text='Sales Database',font=('',40))
    L.place(relwidth=1)
    L1=Label(db,text='Transaction No',font=('',30),borderwidth=2,relief='ridge')
    L1.place(rely=0.1,relx=0.01)
    L2=Label(db,text='Date of Transaction',font=('',30),borderwidth=2,relief='ridge')
    L2.place(rely=0.1,relx=0.225,relwidth=0.3)
    L3=Label(db,text='Flight Name',font=('',30),borderwidth=2,relief='ridge')
    L3.place(rely=0.1,relx=0.527,relwidth=0.25)
    L4=Label(db,text='Sales Amount',font=('',30),borderwidth=2,relief='ridge')
    L4.place(rely=0.1,relx=0.78,relwidth=0.21)
    j=0.18
    for i in y:
        l1=Label(db,text=i[0],font=('',20),borderwidth=2,relief='ridge')
        l1.place(rely=j,relx=0.01,relwidth=0.21)
        l2=Label(db,text=i[1],font=('',20),borderwidth=2,relief='ridge')
        l2.place(rely=j,relx=0.225,relwidth=0.3)
        l3=Label(db,text=i[2],font=('',20),borderwidth=2,relief='ridge')
        l3.place(rely=j,relx=0.527,relwidth=0.25)
        l4=Label(db,text=i[3],font=('',20),borderwidth=2,relief='ridge')
        l4.place(rely=j,relx=0.78,relwidth=0.21)
        j+=0.06

#Review the sales of a particular month
def _5():
    m=Tk()
    def show():
        lst=['AirIndia','Emirates','Fly Dubai']
        a=l.index(month.get())
        b=yr.get()
        c=l1[box.curselection()[0]]
        query="select SaleAmt from sales where FlightNm='{}' and year(DateTransac)='{}' and month(DateTransac)='{}'".format(c,b,a+1)
        x.execute(query)
        y=x.fetchall()
        sum1=0
        new=Tk()
        new.attributes('-fullscreen',True)
        new.config(bg='#191970')
        for i in y:
            sum1+=i[0]
        Label(new,text="The sale made by "+str(c)+" in "+str(l[a])+" of\n"+str(b)+" is ₹"+str(sum1),font=('',40),fg='white',bg='#191970').pack()
    m.attributes('-fullscreen',True)
    m.config(bg='#191970')
    mon=Label(m,text='Select the month',fg='white',bg='#191970',font=('',30))
    mon.place(relx=0.2)
    l=['January','February','March','April','May','June','July','August','September','October','November','December']
    txt=StringVar()
    month=ttk.Combobox(m,textvariable=txt,font=('',30))
    month['values']=l
    month.current(0)
    month.pack(padx=200,pady=10,anchor='ne')
    yr_label=Label(m,text='Select year',fg='white',bg='#191970',font=('',30))
    yr_label.place(relx=0.2,rely=0.15)
    yr=Spinbox(m,from_=2019,to=2021,textvariable='enter year',font=('',30))
    yr.pack(padx=200,pady=20,anchor='ne')
    box_label=Label(m,text='Airline Name',fg='white',bg='#191970',font=('',30))
    box_label.place(relx=0.2,rely=0.45)
    box=Listbox(m,font=('',20))
    box.pack(pady=30,anchor='ne',padx=200)
    l1=['AirIndia','Emirates','FlyDubai']
    box.insert(0,l1[0])
    box.insert(1,l1[1])
    box.insert(2,l1[2])
    cont=Button(m,text='CONTINUE',font=('',40),command=show,relief='solid')
    cont.pack(side='bottom')

#Display the flight with the highest sales in a
#               i.Month         ii.Year 
def _6():
    sales=Tk()
    sales.config(bg='#191970')
    sales.attributes('-fullscreen',True)
    def flight():  #Month
        F=Tk()
        F.config(bg='#191970')
        F.attributes('-fullscreen',True)
        def nxt():
            f=l.index(month.get())
            ye=yr.get()
            L.destroy(),mon.destroy(),month.destroy(),yr_label.destroy(),yr.destroy(),b1.destroy()
            query="select sum(saleamt),flightnm from sales where year(datetransac)={} and month(datetransac)='{}' group by flightnm".format(ye,f+1)
            x.execute(query)
            y=x.fetchall()
            z=max(y)
            n=Label(F,text=z[1]+' has made the highest sale in '+l[f]+'\nof '+ye+' with a total sale of ₹'+str(z[0]),font=('',40),fg='white',bg='#191970')
            n.pack()
        L=Label(F,text="Airline with highest sales record in a month",font=('',40),fg='white',bg='#191970')
        L.pack(fill='x')
        mon=Label(F,text='Select the month',fg='white',bg='#191970',font=('',30))
        mon.place(relx=0.2,rely=0.1)
        l=['January','February','March','April','May','June','July','August','September','October','November','December']
        txt=StringVar()
        month=ttk.Combobox(F,textvariable=txt,font=('',30))
        month['values']=l
        month.current(0)
        month.pack(padx=200,pady=10,anchor='ne')
        yr_label=Label(F,text='Select year',fg='white',bg='#191970',font=('',30))
        yr_label.place(relx=0.2,rely=0.25)
        yr=Spinbox(F,from_=2019,to=2021,textvariable='enter year',font=('Times Roman',30))
        yr.pack(padx=200,pady=20,anchor='ne')
        b1=Button(F,text='NEXT',font=('',40),command=nxt,relief='solid')
        b1.pack(side='bottom')
    def airlink():  #Year
        F=Tk()
        F.config(bg='#191970')
        F.attributes('-fullscreen',True)
        def nxt():
            ye=yr.get()
            L.destroy(),yr_label.destroy(),yr.destroy(),b1.destroy(),b2.destroy()
            query="select sum(saleamt),flightnm from sales where year(datetransac)={} group by flightnm".format(ye)
            x.execute(query)
            y=x.fetchall()
            z=max(y)
            n=Label(F,text=z[1]+' has made the highest sale in\n'+ye+' with a total sale of ₹'+str(z[0]),font=('',40),fg='white',bg='#191970')
            n.pack()
        L=Label(F,text="Airline with highest sales record in a year",fg='white',bg='#191970',font=('Times Roman',40))
        L.pack(fill='x')
        yr_label=Label(F,text='Select year',fg='white',bg='#191970',font=('',30))
        yr_label.place(relx=0.2,rely=0.1)
        yr=Spinbox(F,from_=2019,to=2021,textvariable='enter year',font=('',30))
        yr.pack(padx=200,pady=20,anchor='ne')
        b1=Button(F,text='NEXT',font=('',40),command=nxt,relief='solid')
        b1.pack(side='bottom')
    l1=Label(sales,text="Highest sales record for a",fg='white',bg='#191970',font=('',40))
    l1.pack()
    b1=Button(sales,text='Month',font=('',40),command=flight,relief='solid')
    b1.pack(pady=100)
    b2=Button(sales,text='Year',font=('',40),command=airlink,relief='solid')
    b2.pack(ipadx=15)

#Airline sales comparison with graphs
def _7():
    tot=Tk()
    tot.attributes('-fullscreen',True)
    tot.config(bg='#191970')
    def nxt():
        yer=yr.get()
        mn=l.index(month.get())
        TOT=Tk()
        TOT.attributes('-fullscreen',True)
        TOT.config(bg='#191970')
        def pie():
            graphit.piechart(list1,list2)
        def bar():
            graphit.bargraph(list1,list2)
        query="select * from sales where year(Datetransac)='{}' and month(Datetransac)='{}'".format(yer,mn+1)
        x.execute(query)
        y=x.fetchall()
        list1=['AirIndia','Emirates','FlyDubai']
        list2=[0,0,0]
        for i in y:
            if i[2]=="AirIndia":
                list2[0]+=i[3]
            elif i[2]=="Emirates":
                list2[1]+=i[3]
            else:
                list2[2]+=i[3]
        L1=Label(TOT,text='Compare sales through a',fg='white',bg='#191970',font=('',40))
        L1.pack(fill='x')
        B1=Button(TOT,text='Pie Chart',font=('',40),command=pie,relief='solid')
        B1.pack(pady=50)
        b2=Button(TOT,text='Bar Graph',font=('',40),command=bar,relief='solid')
        b2.pack()
    l1=Label(tot,text="Airline sales comparison with graphs",fg='white',bg='#191970',font=('',40))
    l1.pack()
    mon=Label(tot,text='Select the month',fg='white',bg='#191970',font=('',30))
    mon.place(relx=0.2,rely=0.1)
    l=['January','February','March','April','May','June','July','August','September','October','November','December']
    txt=StringVar()
    month=ttk.Combobox(tot,textvariable=txt,font=('',30))
    month['values']=l
    month.current(0)
    month.pack(padx=200,pady=10,anchor='ne')
    yr_label=Label(tot,text='Select year',fg='white',bg='#191970',font=('',30))
    yr_label.place(relx=0.2,rely=0.35)
    yr=Spinbox(tot,from_=2019,to=2021,textvariable='enter year',font=('',30))
    yr.pack(padx=200,pady=100,anchor='ne')
    b1=Button(tot,text='NEXT',font=('',40),command=nxt,relief='solid')
    b1.pack(side='bottom')

def home():
    SALEs.destroy()
    import First_pg
def nxt():
    a=lb.curselection()
    ind=lb.index(a)
    if ind==0:
        _0()
    elif ind==1:
        _1()
    elif ind==2:
        _2()
    elif ind==3:
        _3()
    elif ind==4:
        _4()
    elif ind==5:
        _5()
    elif ind==6:
        _6()
    else:
        _7()
label=Label(SALEs,text='SELECT FUNCTION',fg='white',bg='#191970',font=('',30))
label.pack(pady=10)
lb=Listbox(SALEs,font=('',30),relief='solid')
lb.pack(pady=5,fill='x',padx=5)
lb.insert(0,'Add transaction data')
lb.insert(1,'Modify the sales of a particular transaction number')
lb.insert(2,'Total sales for a year')
lb.insert(3,"Monthly sales comparison of airlines with a graph")
lb.insert(4,'Dispaly the sales database')
lb.insert(5,'Review the sales for a particular month')
lb.insert(6,'Highest sale record')
lb.insert(7,'Airline sales comparison for a particular month with graphs')
slc=Button(SALEs,text='SELECT',font=('',20),command=nxt,relief='solid')
slc.place(relx=0.9,rely=0.9)
back=Button(SALEs,text='HOME',font=('',20),command=home,relief='solid')
back.place(rely=0.9,relx=0.02,relwidth=0.08)
Quit=Button(SALEs,text='QUIT',font=('',20),command=end,relief='solid')
Quit.place(rely=0.9,relx=0.5,relwidth=0.08)
SALEs.mainloop()
