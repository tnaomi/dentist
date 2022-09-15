from urllib import request
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def blog(rquest):
    return render(request,'blog.html',{})

def department(request):
    return render(request,'department.html',{})

def doctor(request):
    return render(request,'doctor.html',{})

def blog_single(request,yr=datetime.year,mon=datetime.month,dy=datetime.day):
    return render(request,'blog-single.html',{})

def pricing(request):
    return render(request,'pricing.html',{})