from django.shortcuts import render
import pyrebase
config = {
     'apiKey': "AIzaSyAtz2cuDcPHqAuQeWRzwTLhhWTZq_I1_XU",
    'authDomain': "hackathon-e6a4d.firebaseapp.com",
    'projectId': "hackathon-e6a4d",
    'databaseURL':"https://hackathon-e6a4d.web.app",
    'storageBucket': "hackathon-e6a4d.appspot.com",
    'messagingSenderId': "147102212882",
    'appId': "1:147102212882:web:668f67aabeda976e5049cb",
    'measurementId': "G-TG8Z8SM65D"
}
firebase =pyrebase.initialize_app(config)
auth= firebase.auth()
'''def index(request):
    return render(request,'index.html',{})'''
def singIN(request):
    return render(request,'signin.html')
def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    user = auth.sign_in_with_email_and_password(email, passw)
    return render(request,'welcome.html',{'e':email})