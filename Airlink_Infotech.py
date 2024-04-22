import sys
import graphit
import sqlite3

# Connecting to SQLite database
con = sqlite3.connect('airinfo.db')
x = con.cursor()

#User Defined Functions for HR department

#Adding a new employee
def add():
    emp_no=input("Enter the Employee Id: ")
    nm=input("Enter name of the employee: ")
    dept=input("Enter the department of the employee: ")
    sal=int(input("Enter the salary: "))
    usern=input("Please enter the username you to be assigned to this employee: ")
    passw=input("Please enter the password you to be assigned to this employee: ")
    query1="insert into employee values('{}','{}','{}',{})".format(emp_no,nm,dept,sal)
    x.execute(query1)
    con.commit()
    if dept=="HR":
        query2="insert into hrpass values('{}','{}','{}')".format(emp_no,usern,passw)
        x.execute(query2)
        con.commit()
    else:
        query3="insert into salespass values('{}','{}')".format(usern,passw)
        x.execute(query3)
        con.commit()
    print("Data inserted successfully")

#Deleting an existing employee
def delete():
    emp_no=(input("Enter the Employee Id to be deleted: "))
    dept=input("Please enter the department of the employee: ")
    if dept=="HR":
        query="delete from hrpass where emp_no='{}'".format(emp_no)
        x.execute(query)
        con.commit()
        query1="delete from employee where emp_no='{}'".format(emp_no)
        x.execute(query1)
        con.commit()
    else:
        query="delete from salespass where emp_no='{}'".format(emp_no)
        x.execute(query)
        con.commit()
        query1="delete from employee where emp_no='{}'".format(emp_no)
        x.execute(query1)
        con.commit()
    print("Data deleted successfully")

#Displaying the employee database
def display():
    query="select * from employee"
    x.execute(query)
    for i in x:
        print(i)

#Details of a particular employee
def details():
    emp_no=input("Please enter the Employee ID of the employee you would like to view")
    query="select*from employee where emp_no='{}'".format(emp_no)
    x.execute(query)
    for i in x:
        print(i[0]," - Employee ID")
        print(i[1]," - Name of Employee")
        print(i[2]," - Department of the Employee")
        print(i[3]," - Salary of the Employee") 

#Updating the salary package of a particular employee
def update():
    emp_no=input("Please enter the Employee Id of the employee whose salary you would like to update")
    sal=int(input("Please enter the modified salary package for the employee"))
    query="update employee set Salary={} where emp_no='{}'".format(sal,emp_no)
    x.execute(query)
    con.commit()
    print("Salary updated successfully")


#HR Department 
print("Welcome to AIRLINK InfoTech")
print('''Who is using the program?
         1.HR
         2.Sales team''')
ch=int(input("Please enter your choice"))
if ch==1:
    while True:
        usern=input("Please enter your username: ")
        passw=input("Please enter your password: ")
        query='select * from hrpass where username="{}" and password="{}"'.format(usern,passw)
        x.execute(query)
        y=x.fetchall()
        if y:
            for i in y:
                print("Welcome to the HR Department of Airlink Infotech")
                print("Are you using this program for the first time?")
                print('''i.Yes
ii.No''')
                ch1=input("Please enter the roman numeral beside your choice: ")
                if ch1=='i':
                    while True:
                        emp_no=input("Enter the Employee Id: ")
                        nm=input("Enter name of the employee: ")
                        dept=input("Enter the department of the employee: ")
                        sal=int(input("Enter the salary: "))
                        usern=input("Please enter the username you to be assigned to this employee: ")
                        passw=input("Please enter the password you to be assigned to this employee: ")
                        query1="insert into employee values('{}','{}','{}',{})".format(emp_no,nm,dept,sal)
                        x.execute(query1)
                        con.commit()
                        if dept=="HR":
                            query2="insert into hrpass values('{}','{}','{}')".format(emp_no,usern,passw)
                            x.execute(query2)
                            con.commit()
                        else:
                            query3="insert into salespass values('{}','{}')".format(usern,passw)
                            x.execute(query3)
                            con.commit()
                            print("Data entered successfully")
                            print("Do you want to continue adding employees Y/N")
                            ch=input("Please enter your choice: ")
                            if ch=='N':
                                while True:
                                    print('''a.Add an employee
b.Remove an employee using employee id
c.Update salary package
d.Display all employees
e.Display all the employees of a particular department
f.Display employee details of a particular employee
g.Display the names of employees in alphabetical order''')
                                    ch1=input("Please enter the letter beside the function you would like to perform: ")
                                    if ch1=='a':
                                        add()
                                    elif ch1=='b':
                                        delete()
                                    elif ch1=='c':
                                        update()
                                    elif ch1=='d':
                                        display()
                                    elif ch1=='e':
                                        dept=input("Please enter the department you would like to view: ")   #Displaying all the employees of a particular Department
                                        query="select Name from employee where Department='{}'".format(dept)
                                        x.execute(query)
                                        y=x.fetchall()
                                        for i in y:
                                            print(i)
                                    elif ch1=='f':
                                        details()
                                    else:  #Display employee names in alphabetical order
                                        query="select Name from employee order by Name"   
                                        x.execute(query)
                                        y=x.fetchall()
                                        for i in y:
                                            print(i[0])
                else:
                    while True:
                        print('''a.Add an employee
b.Remove an employee using employee id
c.Update salary package
d.Display all employees
e.Display all the employees of a particular department
f.Display employee details of a particular employee
g.Display the names of employees in alphabetical order''')
                        ch1=input("Please enter the letter beside the function you would like to perform")
                        if ch1=='a':
                            add()
                        elif ch1=='b':
                            delete()
                        elif ch1=='c':
                            update()
                        elif ch1=='d':
                            display()
                        elif ch1=='e':
                            dept=input("Please enter the department you would like to view: ")   #Displaying all the employees of a particular Department
                            query="select Name from employee where Department='{}'".format(dept)
                            x.execute(query)
                            y=x.fetchall()
                            for i in y:
                                print(i)
                        elif ch1=='f':
                            details()
                        else:  #Display names in alphabetical order
                            query="select Name from employee order by Name"
                            x.execute(query)
                            y=x.fetchall()
                            for i in y:
                                print(i[0])
        else:
            print("Username and password not recognised")
            again=input("Do you want to try again? (y/n): ")
            if again=="n":
                print("Sorry you will have to log out of Airlink Infotech")
                sys.exit()


#Sales Department        
elif ch==2:
    while True:
        usern=input("Please enter your username: ")
        passw=input("Please enter your password: ")
        query='select * from salespass where username="{}" and password="{}"'.format(usern,passw)
        x.execute(query)
        y=x.fetchall()
        if y:
            for i in y:
                print("Welcome to the Sales Department of Airlink Infotech")
                print("Are you using this program for the first time?")
                print('''i.Yes
ii.No''')
                ch1=input("Please enter the roman numeral beside your choice: ")
                if ch1=='i':
                    transnr=input("Please enter the transaction number of the sale made: ")
                    date=input("Please enter the date of transaction in the format YYYY/MM/DD: ")
                    flt=input("Please enter the name of the flight from the list[AirIndia,FlyDubai,Emirates]: ")
                    inc=int(input("Please enter the amount recieved after the transaction"))
                    query1="insert into sales values('{}','{}','{}',{})".format(transnr,date,flt,inc)
                    x.execute(query1)
                    con.commit()
                else:
                    while True:
                        print('''a.Modify the sales of a particular transaction number
b.Get the total sales of the year:
                  i.Of a flight
                  ii.Of the company
c.Compare this year's sales of different flights through a graphical representation
d.Dispaly the sales database
e.Review the sales of a particular month:
                  i.Of a flight
f.Display the flight with the highest:
                  i.Monthly sales
                  ii.Yearly sales
g.Compare the monthly sales of the three flights through a graphical representaion of a:
                  i.Pie chart
                  ii.Bar graph''')
                        ch2=input("Please enter the letter beside the function you would like to perform")
                        if ch2=='a':#Modifying the sales of a particular transaction number
                            transacnr=input("Please enter the transaction number to be modified: ")
                            inc=int(input("Please enter the updated income of that particular date: "))
                            query="update sales set SaleAmt={} where TransacNr='{}'".format(inc,transacnr)
                            x.execute(query)
                            con.commit()
                            print("Data updated successfully")
                            
                            
                        elif ch2=='d': #Display sales database
                            query="select*from sales"
                            x.execute(query)
                            y=x.fetchall()
                            for i in y:
                                print(i)

                        elif ch2=='f': #Highest sales of a flight
                            ch3=input("Please enter the roman numeral beside the subdivison you would like to review")
                            if ch3=='i':  #In a month
                                yer=input("Please enter the year you would like to view: ")
                                mon=input("Please enter the month you would like to view as a number (Jan=1,Feb=2...): ")
                                query="select * from sales where year(DateTransac)='{}' and month(DateTransac)='{}'".format(yer,mon)
                                x.execute(query)
                                y=x.fetchall()
                                dict1={'AirIndia':0,'Emirates':0,'FlyDubai':0}
                                for i in y:
                                    dict1[i[2]]+=i[3]
                                a=max(dict1)
                                print(a,"has made the highest sale in the given month with a total sale of",dict1[a],"Rs.")
                            else:  #In a year
                                yer=input("Please enter the year you would like to view: ")
                                query="select * from sales where year(DateTransac)='{}'".format(yer)
                                x.execute(query)
                                y=x.fetchall()
                                dict2={'AirIndia':0,'Emirates':0,'FlyDubai':0}
                                for i in y:
                                    dict2[i[2]]+=i[3]
                                a=max(dict2)
                                print(a,"has made the highest sales for the year",dict2[a],"with a total sale of",a,"Rs.")

                        elif ch2=='g':   #Display the monthly sales of the three flights through a graphical representaion
                            yer=int(input("Please enter the year you would like to view: "))
                            mon=int(input("Please enter the month you would like to view as a number ie.Jan=1,Feb=2.....: "))
                            query="select*from sales where year(DateTransac)={} and month(DateTransac)={}".format(yer,mon)
                            x.execute(query)
                            y=x.fetchall()
                            dict1={'AirIndia':0,'Emirates':0,'FlyDubai':0}
                            for i in y:
                                dict1[i[2]]+=i[3]
                            ch=input("PLease enter the roman numeral beside the choice you would like to execute: ")
                            if ch=='i':    #Pie Chart
                                graphit.piechart(dict1)
                            else:          #Bar Graph
                                graphit.bargraph(dict1)

                        elif ch2=='b':  #Total sales
                            ch3=input("Please enter the subdivision you would like review: ")
                            if ch3=='i':  #Of flight
                                flt=input("Please enter the name of the flight: ")
                                yer=input("Please enter the year you would like to view: ")
                                query="select SaleAmt from sales where year(DateTransac)='{}' and FlightNm='{}'".format(yer,flt)
                                x.execute(query)
                                y=x.fetchall()
                                sum1=0
                                for i in y:
                                    sum1+=i[0]
                                print("The total sales of",flt,"for the year",yer,"is",sum1,"Rs")
                            
                            elif ch3=="ii":  #Of Airlink Infotech
                                yer=input("Please enter the year you would like to view: ")
                                query="select SaleAmt from sales where year(DateTransac)='{}'".format(yer)
                                x.execute(query)
                                y=x.fetchall()
                                sum1=0
                                for i in y:
                                    sum1+=0.3*(i[0])
                                print("The total sales of Airlink Infotech for the year",yer,"is",sum1,"Rs")

                        elif ch2=='e':
                            ch4=input("Please enter the subdivision you would like to review: ")
                            if ch4=="i":  #Reviewing the sales of a flight for a particular month
                                flt=input("Please enter the name of the flight whose data you would like to view: ")
                                mon=input("Please enter the month of the as a number ie.Jan=1,Feb=2....: ")
                                yer=input("Please enter the year: ")
                                query="select SaleAmt from sales where FlightNm='{}' and year(DateTransac)='{}' and month(DateTransac)='{}'".format(flt,yer,mon)
                                x.execute(query)
                                y=x.fetchall()
                                sum1=0
                                for i in y:
                                    sum1+=i[0]
                                print("The sale made by",flt,"in this month is",sum1,"Rs")
                                     
                            elif ch4=="ii":  #Reviewing the sales of Airlink Infotech for a particular month
                               mon=input("Please enter the month of the year as a number ie.Jan=1,Feb=2....: ")
                               yer=input("Please enter the year: ")
                               query="select SaleAmt from sales where year(DateTransac)='{}' and month(DateTransac)='{}'".format(yer,mon)
                               x.execute(query)
                               y=x.fetchall()
                               sum1=0
                               for i in y:
                                   sum1+=0.3*(i[0])
                                   print("The sale made by AirLink Infotech in this month is",sum1,"Rs")
                            
                        elif ch2=='c':  #Creating a graphical representation to compare the sales of different airlines in a particular year
                            yer=input("Please enter the year which you would like to view: ")
                            query="select FlightNm, month(DateTransac),SaleAmt from sales where year(DateTransac)='{}'".format(yer)
                            x.execute(query)
                            y=x.fetchall()
                            dict1={}
                            for i in y:
                                dict1[(i[0],i[1])]=i[2]
                            AirIndia={}
                            Emirates={}
                            FlyDubai={}
                            month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
                            for i in month.values():
                                AirIndia.setdefault(i,0)
                                Emirates.setdefault(i,0)
                                FlyDubai.setdefault(i,0)
                            for i,j in dict1:
                                if i=="AirIndia":
                                    AirIndia[month[j]]+=dict1[(i,j)]
                                elif i=='Emirates':
                                    Emirates[month[j]]+=dict1[(i,j)]
                                else:
                                    FlyDubai[month[j]]+=dict1[(i,j)]
                            graphit.bargraph(AirIndia,Emirates,FlyDubai)
        else:
            print("Username and password not recognised")
            again=input("Do you want to try again? (y/n): ")
            if again=="n":
                print("Sorry you will have to log out of Airlink Infotech")
                sys.exit()
