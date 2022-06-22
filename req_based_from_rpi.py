'''
Code to receive data from 2 different zigbees every 5
seconds and store it in different csv file and mail it every 1 minute
'''

import serial
import csv
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

a = open('store.csv', 'w')
c = csv.writer(a)
b = open('store1.csv', 'w')
d = csv.writer(b)
c.writerow(["temperature", "humidity"])
d.writerow(["temperature", "humidity"])
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
            val1 += val
            # print val1
            length = val1.encode("hex")
            val4 = int(length, 16)
            len2 = val4 + 5

            # print len2
        frame_rec += val
        if k == len2:
            k = 0
            if data_num < 23:
                data_num = data_num + 1
            else:
                k = -1
            data_rec += frame_rec[16:len2 - 1]
            if data_rec[0] == "A":
                t = data_rec[data_rec.find("A") + 1:data_rec.find("B")]
                h = data_rec[data_rec.find("C") + 1:data_rec.find("D")]
                a = open('store.csv', 'a')
                c = csv.writer(a)
                c.writerow([t, h])
            else:
                l = data_rec[data_rec.find("E") + 1:data_rec.find("F")]
                m = data_rec[data_rec.find("G") + 1:data_rec.find("H")]
                b = open('store1.csv', 'a')
                d = csv.writer(b)
                d.writerow([l, m])
            val1 = ""
            data_rec = ""
            frame_rec = ""
            time.sleep(2.5)
        k = k + 1
        a.close()
    csv_data = open('store.csv', 'rb').read()
    csv_data1 = open('store1.csv', 'rb').read()
    record = MIMEBase('application', 'octet-stream')
    record.set_payload(csv_data)
    encoders.encode_base64(record)
    record.add_header('Content-Disposition', 'attachment', filename=os.path.basename('store.csv'))
    record1 = MIMEBase('application', 'octet-stream')
    record1.set_payload(csv_data1)
    encoders.encode_base64(record1)
    record1.add_header('Content-Disposition', 'attachment', filename=os.path.basename('store1.csv'))
    msg = MIMEMultipart()
    msg.attach(record)
    msg.attach(record1)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('xyzn@gmail.com', 'abc12345')
    s.sendmail('xyzn@gmail.com', ['pqr@gmail.com', 'xyz@gmail.com'], msg.as_string())
    s.quit()
