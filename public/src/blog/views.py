from time import time
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
    return render(request,'index.html')

def singIN(request):
    return render(request,'signin.html')
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
    return render(request,'welcome.html')

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
def create(request):
    return render(request,"post.html")

def post_create(request):
    import time
    from datetime import datetime, timezone
    import pytz
    tz=pytz.timezone('Asia/Kolkata')
    time_now=datetime.now(timezone.utc).astimezone(tz)
    millis= int(time.mktime(time_now.timetuple()))
   
    idtoken=request.session['uid']
    a=authe.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    print(str(a))
    a=a['localId']
    title=request.POST.get('title')
    content=request.POST.get('content')
    url=request.POST.get('url')
    data={
        'title':title,
        'content':content,
        'uid':a,
        'url':url
        
    }
    database.child('users').child('Posts').child(millis).set(data)
    return render(request,"welcome.html")

def check(request):
    import datetime
    user=database.child('users').get()
    a=database.child('users').shallow().get()
    lis_time=[]
    post=[]
    date=[]
    
    timestamps=database.child('users').child('Posts').shallow().get().val()
    for i in timestamps:
        lis_time.append(i)
    lis_time.sort(reverse=True)
    print(lis_time)
    for i in lis_time:
        title=database.child('users').child('Posts').child(i).child('title').get().val()
        post.append(title)
    for i in lis_time:
        i=float(i)
        dat=datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date.append(dat)
    comb_lis=zip(lis_time,date,post)
    return render(request,'check.html',{'comb_lis':comb_lis})
        
def post_check(request):
    import datetime
    time=request.GET.get('z')
    Title=database.child('users').child('Posts').child(time).child('title').get().val()
    Content=database.child('users').child('Posts').child(time).child('content').get().val()
    i= float(time)
    dat=datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
    img_url=database.child('users').child('Posts').child(time).child('url').get().val()
    return render(request,'blog.html',{'t':Title,'c':Content,'d':dat,"i":img_url})