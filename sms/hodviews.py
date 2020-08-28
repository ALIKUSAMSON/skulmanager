from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser
from django.contrib import messages


# Create your views here.
def index(request):
    template = 'index.html'
    context = locals()
    return render(request,template,context)

def add_staff(request):
    template = 'pages/add_staff.html'
    context = locals()
    return render(request,template,context)


def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username") 
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        address = request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type_data=2)
            user.staff.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/index")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/add_staff")

def add_students(request):
    template = 'pages/add_students.html'
    context = locals()
    return render(request,template,context)


def profile(request):
    template = 'pages/examples/profile.html'
    context = locals()
    return render(request,template,context)
