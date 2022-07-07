'''
Upload date to firebase cloud
'''
import firebase
from firebase import firebase
#open the database using the url
firebase=firebase.FirebaseApplication('https://xxx.firebaseio.com/')
while 1:
    # upload data to the temperature 1 label
    result=firebase.patch('/Time', {'temperature 1':data})
