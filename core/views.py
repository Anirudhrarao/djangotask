from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import DoctorForm, PatientForm, DoctorLogin, PatientLogin, BlogFormCreations
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User,DoctoBlog
# Create your views here.
def home(request):
    return render(request,'home.html')

def drsign(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(drlogin)
    else:
        form = DoctorForm()
    return render(request,'drsign.html',{'form':form})

def ptsign(request):
    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(ptlogin)
    else:
        form = PatientForm()
    return render(request,'ptsign.html',{'form':form})


def drlogin(request):
    if request.method == 'POST':
        form = DoctorLogin(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(profile)
    else:
        form = DoctorLogin()
    return render(request,'drlogin.html',{'form':form})


def ptlogin(request):
    if request.method == 'POST':
        form = PatientLogin(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(profile)
    else:
        form = PatientLogin()
    return render(request,'ptlogin.html',{'form':form})
@login_required(login_url=home)
def profile(request):
    blogs = DoctoBlog.objects.filter(status=1)
    return render(request,'profile.html',{'blog':blogs})


def logout_view(request):
    logout(request)
    return redirect(home)

def blog_create(request):
    if request.method == 'POST':
        b_form = BlogFormCreations(request.POST,request.FILES)
        if b_form.is_valid():
            blogger = b_form.save(commit=False)
            blogger.user = request.user
            blogger.save()
            return redirect(profile)
    else:
        b_form = BlogFormCreations()
    return render(request,'blog_create.html',{'b_form':b_form})

def blog_post(request):
    blogs = DoctoBlog.objects.filter(status=1)
    return render(request,'blogs.html',{'blog':blogs})

def detail_blog(request,id):
    allblog = DoctoBlog.objects.get(id=id)
    return render(request,'detblog.html',{'blog':allblog})