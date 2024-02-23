from django.shortcuts import render,HttpResponse
from registrationapp.models import registration
from registrationapp.forms import rgform

# Create your views here.

from django.contrib.auth.hashers import make_password

from django.conf import settings
from django.core.mail import send_mail 


def reg(request):
    if request.method=='GET':
        var=rgform()
        return render(request,'rg.html',{'var':var})
    elif request.method=='POST':
        form=rgform(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            P=form.password
            enc=make_password(P)
            form.password=enc
            form.save()

            subject='welcome to pyspiders'
            message=f'hi {form.username},thank you for registring and your username :{form.username} password:{P}'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=['chandansgowda59@gmail.com',form.email]
            send_mail(subject,message,email_from,recipient_list)

            return HttpResponse('DATA STORED IN A TABLE and sent mail')

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
def login(request):
    if request.method=='GET':
        var=AuthenticationForm()
        return render(request,'login.html',{'var':var})
    elif request.method=='POST':
        user=request.POST['username']
        pas=request.POST['password']
        v=authenticate(username=user,password=pas)
        print(v)
        if v is not None:
        
                return render(request,'home.html')
        else:
                return HttpResponse('CHECK USERNAME OR PASSWORD')
            