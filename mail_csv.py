'''
MAILING THE CSV
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
img_data = open('temp.png', 'rb').read()
csv_data = open('temp.csv', 'rb').read()
record = MIMEBase('application','octet-stream')
record.set_payload(csv_data)
encoders.encode_base64(record) record.add_header('Content-Disposition','attachment',filename=os.path.basename('temp.csv')) msg = MIMEMultipart()
image = MIMEImage(img_data, name=os.path.basename('temp.png')) msg.attach(image) #attach image
msg.attach(record) #attach csv file
s = smtplib.SMTP('smtp.gmail.com', 587) #open gmail.com
s.ehlo()
s.starttls()
s.ehlo()
s.login('xyz@gmail.com', 'abcdefgf') #login details
s.sendmail('xyz@gmail.com',['pqr@gmail.com','xyz@gmail .com'], msg.as_string()) #to address and mail message
s.quit()
