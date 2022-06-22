'''
Upload date to firebase cloud
'''
import firebase
from firebase import firebase
#open the database using the url
firebase=firebase.FirebaseApplication('https://rashmi-513a1.firebaseio.com/')
while 1:
    # upload data to the temperature 1 label
    result=firebase.patch('/Time', {'temperature 1':data})
