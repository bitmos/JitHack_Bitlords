from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib import auth
from firebase_admin import credentials, firestore
config = {
     'apiKey': "AIzaSyAtz2cuDcPHqAuQeWRzwTLhhWTZq_I1_XU",
    'authDomain': "hackathon-e6a4d.firebaseapp.com",
    'databaseURL': "https://hackathon-e6a4d-default-rtdb.firebaseio.com",
    'projectId': "hackathon-e6a4d",
    'storageBucket': "hackathon-e6a4d.appspot.com",
    'messagingSenderId': "147102212882",
    'appId': "1:147102212882:web:668f67aabeda976e5049cb",
    'measurementId': "G-TG8Z8SM65D"
}
firebase =pyrebase.initialize_app(config)
authe= firebase.auth()
database=firebase.database()

def index(request):
    return render(request,'index.html',)
def singIN(request):
    return render(request,'signin.html',{})
def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message='Invalid credentials'
        return render(request, "signin.html",{"messg":message})
    session_id=user['idToken']
    request.session['uid']=(session_id)
    return render(request,'welcome.html',{'e':email})

def logout(request):
    auth.logout(request)
    return render(request, 'signin.html')

def singUP(request):
    return render(request,'signup.html')

def postsignup(request):
    name= request.POST.get('name')
    email= request.POST.get('email')
    passw= request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid=user['localId']
        data={'name':name,'status':'1'}
        database.child('users').child(uid).child('details').set(data)
    except:
        message="unable to create"
        return render(request, "signup.html",{"messg":message})
    
    
    return render(request,"signin.html")
