'''
PLOTTING A GRAPH FROM THE VALUES PRESENT IN CSV FILE
'''

import csv
from datetime import datetime
import pylab
from pylab import figure
from csv import reader
from matplotlib import pyplot

# j=0
a=open('store3.csv','r')
#Accessing the time column of the csv file
time2=[i[2:10] for i in a ]
if time2[csv_row][0:2]=="16" and time2[csv_row][3:5]=="00" and srf==0:
    print(csv_row)
    print("yes")
#storing the first(0th)column in x
while j<csv_row+1:
    print(time2[j][0:2])
    print(time2[j][3:5])
# The time between which the plot is plotted
if time2[j][0:2]=="14" and time2[j][3:5]=="52":
    if sif==0:
        si=j
        sif=1
#the index of 50 secs is stored in sr
if time2[j][0:2]=="16" and time2[j][3:5]=="00":
    sr=j
    srf=1
j=j+1
a=open('store3.csv','r')
#storing the second(1st)coloumn in y
current =[i[13:17] for i in a ]
print(current)
a=open('store3.csv','r')
#storing the second(1st)coloumn in y
voltage =[i[18:22] for i in a ]

z=[ datetime.strptime(time2[i+1],'%H:%M:%S') for i in range(csv_row)]
c1=[current[i+1] for i in range(csv_row)]
print(z)
#The plot between time and current is plotted
y1=c1[si:sr+1]
z1=z[si:sr+1]
pyplot.plot(z1,y1)
pyplot.gcf().autofmt_xdate()
pyplot.ylabel('Current')
pyplot.savefig('temp.png')
pyplot.show()

def plot_from_csv(file_name,x_para_index,y_para_index,csv_range,time_min,time_max)
    f=list(csv.reader(open(file_name,'r')) )
    y=[i[y_para_index] for i in f ]
    j=0
    z=[ datetime.strptime(x[i],'%Y-%m-%d %H:%M:%S') for i in range(csv_range)] #converting string format to datetime format
    while j<csv_range:
        if (x[j][1:2]==time_min) :
            si=j
            print(si)
    #the index of 50 secs is stored in sr
        if (x[j][1:2]==time_max):
            sr=j
            print(sr)
        j=j+1
    #storing values between si and sr in y1 and z1
    y1=y[si:sr+1]
    z1=z[si:sr+1]
    pyplot.plot(z1,y1)
    pyplot.gcf().autofmt_xdate()
