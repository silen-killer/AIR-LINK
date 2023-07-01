import matplotlib.pyplot as plt
import numpy as np

def bar(AirIndia,Emirates,FlyDubai):
    w=0.2
    x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    bar1=np.arange(len(x))
    bar2=[i+w for i in bar1]
    bar3=[i+w for i in bar2]
    plt.bar(bar1,AirIndia,w,label="AirIndia")
    plt.bar(bar2,Emirates,w,label="Emirates")
    plt.bar(bar3,FlyDubai,w,label="FlyDubai")
    plt.xlabel("Months")
    plt.ylabel("Revenue")
    plt.title("Sales Report")
    plt.xticks(bar1+w,x)
    plt.legend()
    plt.show()

def piechart(list1,list2):
    plt.style.use("fivethirtyeight")
    a=max(list2)
    explode=[0,0,0]
    b=list2.index(a)
    explode[b]=0.3
    plt.pie(list2, labels=list1, explode=explode, shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title("Sales for a particular month")
    plt.tight_layout()
    plt.legend()
    plt.show()

def linegraph(yer,AirIndia,Emirates,FlyDubai):
    plt.title("Sales of three flights for the year",yer)
    x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plt.plot(x,AirIndia)
    plt.plot(x,Emirates)
    plt.plot(x,FlyDubai)
    plt.legen()
    plt.show()

def bargraph(list1,list2):
    ypos=np.arange(len(list1))
    plt.xticks(ypos,list1)
    plt.xlabel("Flight Names")
    plt.ylabel("Revenue Generated")
    plt.bar(ypos,list2,label="Revenue")
    plt.legend()
    plt.show()
