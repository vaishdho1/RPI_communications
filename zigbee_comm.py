'''
Python code to receive frames from xbee
'''
import serial
ser=serial.Serial('/dev/ttyUSB0',9600)
i=1
j=0
len2=0
val1=""
data=""
frame=""
while 1:
    val=ser.read()
    if i==2:
        val1+=val
    if i==3:
        val1+=val
        length=val1.encode("hex")
        val4=int(length,16)
        len2=val4+5
    frame+=val

    if i==len2:
        i=0
        data+=frame[16:len2-1]
        val1=""
        data=""
        frame=""
    i=i+1
