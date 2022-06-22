from Tkinter import *
from time import sleep
from receive import receive#import receive library
from PIL import ImageTk,Image
import Tkinter
root=Tk() # creating window named Tk
cwgt=Canvas(root,height=1000,width=2000) #Creating Canvas in the window
cwgt.pack(expand=True,fill=BOTH)
image1=Image.open('/home/pi/rpi/photo1.jpg') #open background image
image2=ImageTk.PhotoImage(image1)
cwgtimg=image2
temp1=IntVar() #initialising temp1 to hold integer value
temp1.set(0) # setting temp1 to 0
temp2=IntVar()
temp2.set(0)
temp3=IntVar()
temp3.set(0)
temp4=IntVar()
temp4.set(0)
volt=IntVar()
volt.set(0)
amp=IntVar()
amp.set(0)
clock=IntVar()
clock.set(0)
cwgt.create_image(0,0,anchor=NW,image=image2) #set image2 as background
b1=Label(cwgt,text="temperature1",bd=0,bg="white") #create temperature1 label
b2=Label(cwgt,text="temperature2",bd=0,bg="white")
b3=Label(cwgt,text="temperature3",bd=0,bg="white")
b4=Label(cwgt,text="temperature4",bd=0,bg="white")
vol=Label(cwgt,text="voltage",bd=0,bg="white")
cur=Label(cwgt,text="current",bd=0,bg="white")
t_ime=Label(cwgt,text="time",bd=0,bg="white")
l1=Label(cwgt,textvariable=temp1,bd=0)
l1.config(width=15)#configuring width of label l1
l1.config(font=("Courier",20))#configuring font size of label l1 l2=Label(cwgt,textvariable=temp2,bd=0)
l2.config(width=15)
l2.config(font=("Courier",20)) l3=Label(cwgt,textvariable=temp3,bd=0)
l3.config(width=15) l3.config(font=("Courier",20)) l4=Label(cwgt,textvariable=temp4,bd=0)
l4.config(width=15)
l4.config(font=("Courier",20))
vval=Label(cwgt,textvariable=volt,bd=0)
vval.config(width=15)
vval.config(font=("Courier",20))
cval=Label(cwgt,textvariable=amp,bd=0)
cval.config(width=15)
cval.config(font=("Courier",20))
tval=Label(cwgt,textvariable=clock,bd=0)
tval.config(width=15)
tval.config(font=("Courier",20))
b1.config(width=15)
b1.config(font=("Courier",20))
b3.config(width=15)
b3.config(font=("Courier",20))
b2.config(width=15)
b2.config(font=("Courier",20))
b4.config(width=15)
b4.config(font=("Courier",20))
vol.config(width=15)
vol.config(font=("Courier",20))
cur.config(width=15)
cur.config(font=("Courier",20))
t_ime.config(width=15)
t_ime.config(font=("Courier",20)) cwgt.create_window(20,80,window=l1,anchor=NW)#orienting the labels in the window
cwgt.create_window(360,80,window=l2,anchor=NW)
cwgt.create_window(700,80,window=l3,anchor=NW)
cwgt.create_window(20,20,window=b1,anchor=NW)
cwgt.create_window(360,20,window=b2,anchor=NW)
cwgt.create_window(700,20,window=b3,anchor=NW)
cwgt.create_window(20,200,window=b4,anchor=NW)
cwgt.create_window(360,200,window=vol,anchor=NW)
cwgt.create_window(700,200,window=cur,anchor=NW)
cwgt.create_window(20,260,window=l4,anchor=NW)
cwgt.create_window(360,260,window=vval,anchor=NW)
cwgt.create_window(700,260,window=cval,anchor=NW)
cwgt.create_window(360,380,window=t_ime,anchor=NW)
cwgt.create_window(360,440,window=tval,anchor=NW)
cwgt.pack()
while 1:
    data=receive()
    temp1.set(data[data.find("G")+1:data.find("H")])#setting data between G and H in temp1
    temp2.set(data[data.find("I")+1:data.find("J")])
    temp3.set(data[data.find("K")+1:data.find("L")])
    temp4.set(data[data.find("C") + 1:data.find("D")])
    volt.set(data[data.find("E") + 1:data.find("F")])
    amp.set(data[data.find("C") + 1:data.find("D")])
    clock.set(data[data.find("A") + 1:data.find("B")])
    root.update_idletasks()
    root.mainloop()

