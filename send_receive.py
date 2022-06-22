'''
Python Code to send request and receive the data from zigbee
'''

import binascii
import serial
from binascii import hexlify

ser=serial.Serial('/dev/ttyUSB2',9600)
#The destination address and the frame format is specified while 1:
data_hex=""
i=0
j=0
d=0
len2=0
val1=""
data_rec=""
rec_frame=""
val=""
k=1
std=0x7E
adr_64_8=0x00
adr_64_7=0x00
adr_64_6=0x00
adr_64_5=0x00
adr_64_4=0x00
adr_64_3=0x00
adr_64_2=0xFF
adr_64_1=0xFF
frame_id=0x01
frame_type=0x10
adr_16_1=0xFF
adr_16_2=0xFF
broadcast_radius=0x00
options=0x00
data=input("Enter :")
data1=[]
data_hex=data.encode("hex")
data_l=len(data_hex) length_int=(data_l/2)+14 #integer length
a= "0x%04x"%length_int
l_1 =int(a[2:4],16)
l_2 =int(a[4:6],16)#removing 0x while i<=data_l-2:
data1.append(int(data_hex[i:i+2],16))
d=d+int(data_hex[i:i+2],16)
i=i+2
SUM=frame_id+frame_type+adr_64_1+adr_64_2+adr_64_3+adr_64_4+adr_64_5+adr_64_6+adr_64 _7+adr_64_8+adr_16_1+adr_16_2+options+broadcast_radius+d
C_S= 255-(SUM& int("0x00FF",16))
f=bytearray([std])
frame=([std,l_1,l_2,frame_type,frame_id,adr_64_8,adr_64_7,adr_64_6,adr_64_5,adr_64_4,adr_64_ 3,adr_64_2,adr_64_1,adr_16_1,adr_16_2,broadcast_radius,options,C_S])
f_frame=frame[0:17]+data1+frame[17:18]
f=bytearray(f_frame)
ser.write(f) #The request is sent

#Receiving
while k>0:
    val=ser.read()
    if k==2:
        val1+=val
    if k==3:
        val1+=val
        length=val1.encode("hex")
        val4=int(length,16)
        len2=val4+5
        rec_frame+=val rec_frame.encode("hex")
    if k==len2:
        k=-1
    data_rec+=rec_frame[16:len2-1]
    print(data_rec) #The data received is displayed on the rpi val=""
    val1=""
    data_rec=""
    rec_frame=""
    k=k+1
