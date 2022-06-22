'''
Python code to send query frame and receive the response
'''

import serial #Used for serial communication
import struct  #To convert string to float
import time
#Slave ID
slave=0x01
#Function code to read
fun=0x03
#The address of frequency register is 40157
#Address high is calculated as the hex equivalent of (157-1)
add_h=0x9C
#Lower byte of address is 00
add_l=0x00
#Number of parameters *2
reg_h=0x02
reg_l=0x00
#Error check is calculated using the online calculator
ec_l=0x04
ec_h=0x25
ser=serial.Serial('/dev/ttyUSB0',9600)
#The request frame
frame=([slave,fun,add_l,add_h,reg_l,reg_h,ec_l,ec_h])
f=bytearray (frame)
ser.write(f)
frame_rec=ser.read(9)
t= frame_rec.encode('hex')
p=str(t)
# The last 2 bytes of the data received is stored first
data=p[10:14]
# Followed by the first 2 bytes of the data
data+=p[6:10]
u=struct.unpack('!f', data.decode('hex'))[0]
time.sleep(1)
