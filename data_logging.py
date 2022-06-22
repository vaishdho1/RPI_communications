'''
Python code to store data received from xbee
'''

import csv
import datetime  # To use the datetime
import time
from random import randint  # To get random numbers a=open('store.csv','w')

c = csv.writer(a)
c.writerow(["temperature", "humidity"])
while 1:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    k = 1
    data_num = 0
    len2 = 0
    val1 = ""
    data_rec = ""
    frame_rec = ""
    while k > 0:
        val = ser.read()
        if k == 2:
            val1 += val
            if k == 3:
                val1 += val  # print val1
        length = val1.encode("hex")
        val4 = int(length, 16)
        len2 = val4 + 5
        frame_rec+=val
        if k == len2:
            k = 0
        if data_num < 23:
            data_num = data_num + 1
        else:
            k = -1
        data_rec += frame_rec[16:len2 - 1]
        t = data_rec[data_rec.find("A") + 1:data_rec.find("B")]  # Extracting data between A and B
        h = data_rec[data_rec.find("C") + 1:data_rec.find("D")]  # Extracting data between C and D m= datetime.datetime.now().strftime('H:%M:%S')
        a = open('store.csv', 'a')
        c = csv.writer(a)
        c.writerow([m, t, h])
        val1 = ""
        data_rec = ""
        frame_rec = ""
        time.sleep(2.5)
        k = k + 1
        a.close()

