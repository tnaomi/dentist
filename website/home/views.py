from urllib import request
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request):
    if request.method=="POST":
        #FOr the appointment form
        first_name=request.POST['app_first']
        last_name=request.POST['app_last']
        dept_choice=request.POST['app_dept']
        datee=request.POST['app_date']
        timee=request.POST['app_time']

        return render(request,'index.html',{'first':first_name})
    else:
        return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        eemail=request.POST['eemail']#email address
        subj=request.POST['subj']#subject
        msg=request.POST['msg']#message

        
        return render(request,'contact.html',{'fullname':fullname,})

    else:
        return render(request,'contact.html',{})
        

def blog(request):
    return render(request,'blog.html',{})

def department(request):
    return render(request,'department.html',{})

def doctor(request):
    return render(request,'doctor.html',{})

def blog_single(request,yr=datetime.year,mon=datetime.month,dy=datetime.day):
    return render(request,'blog-single.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def footer_form(request):
    if request.method=="POST":
        email_address=request.POST['email_address']
        return render(request,'partials/footer.html',{'email_address':email_address})
    else:
        return render(request,'partials/footer.html',{})