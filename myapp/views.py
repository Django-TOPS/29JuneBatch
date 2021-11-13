from django.shortcuts import redirect, render
from .forms import SignupForm, UserFormData
from .models import signup_master, userform
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from BatchProject import settings
import random
import requests
import json


# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            signupfrm=SignupForm(request.POST)
            if signupfrm.is_valid():
                signupfrm.save()
                print("Signup Sucessfully!")
               
                otp=random.randint(1111,9999)
                # Sending MAIL

                """
                sub="Success!"
                msg=f"Hello User,\nYour account has been created with us!\nYour one time password is {otp}\nThanks & Regards!\nTOPS Technologies Pvt.Ltd\nRajkot Center\n+91 9724799469 | sanket.chauhan@tops-int.com"
                #from_id='topsdjangoproject@gmail.com'
                from_id=settings.EMAIL_HOST_USER
                #to_id=['fichadia3681@gmail.com','nitinjethava143@yahoo.com','vishalm00005@gmail.com']
                to_id=request.POST['email']
                send_mail(sub,msg,from_id,to_id)
                """
                return redirect('home')
            else:
                print(signupfrm.errors)
               
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            userid=signup_master.objects.get(username=unm)
            print("UserID is:",userid.id)

            user=signup_master.objects.filter(username=unm,password=pas)
            if user:
                print('Login Successfully!')
                request.session['user']=unm
                request.session['userid']=userid.id
                otp=random.randint(1111,9999)
                # SMS Sending
                # mention url
                url = "https://www.fast2sms.com/dev/bulk"
                
                # create a dictionary
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS',
                    # Put your message here!
                    'message': f"Hello User,\nYour account has been login!\nYour one time password is {otp}\nThanks & Regards!\nTOPS Technologies Pvt.Ltd\nRajkot Center",
                    'language': 'english',
                    'route': 'p',
                    # You can send sms to multiple numbers
                    # separated by comma.
                    'numbers': '9724799469'	
                }
                # create a dictionary
                headers = {
                    'authorization': 'kbDD12fyyvfBdZeaKoMturDYkYHpcOyoSclOhboJUsG1GN05Ww5RKQVfnO5C',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }

                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                returned_msg = json.loads(response.text)
                #returned_msg = json.loads(response.text)
                print(returned_msg['message'])
                return redirect('home')
            else:
                print("Login Faild...Try again!") 
    else:
        print('Somthing went wrong....')
    return render(request,'index.html')

def home(request):
    user=request.session.get('user')
    if request.method=='POST':
        userfrm=UserFormData(request.POST,request.FILES)
        if userfrm.is_valid():
            userfrm.save()
            print("Your query has been uploaded!")
            return redirect('home')
        else:
            print(userfrm.errors)
    else:
        userfrm=UserFormData()
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        id=signup_master.objects.get(id=userid)
        if signupfrm.is_valid():
            signupfrm=SignupForm(request.POST,instance=id)
            signupfrm.save()
            print("Your profile data has been updated!")
            return redirect('home')
        else:
            print(signupfrm.errors)
    else:
        print("Error...Somthing went wrong!")    
    return render(request,'updateprofile.html',{'user':user,'userid':signup_master.objects.get(id=userid)})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')