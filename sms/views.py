from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import datetime
from sms.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser



# Create your views here.

def login(request):
    template = 'pages/examples/login.html'
    context = locals()
    return render(request,template,context)

def dologin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            return HttpResponse("Email : "+request.POST.get('email')+"Password :"+request.POST.get('password'))
        else:
            return HttpResponse("Invalid Login")


def register(request):
    template = 'pages/examples/register.html'
    context = locals()
    return render(request,template,context)

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User :"+request.user.email+" usertype :"+str(request.user.user_type))
    else:
        return HttpResponse("please login first ")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")