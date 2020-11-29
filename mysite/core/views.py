from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Banner

# Create your views here.
def home(request):
    context = {
        'banners' : Banner.objects.all()
    }
    return render(request,'home.html', context)

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    
    return render(request,'registration/signup.html',{
        'form':form
    })
@login_required
def secret_page(request):
    return render(request,'registration/secret_page.html') 


def booking(request):
    return render(request,'booking/bookhere.html')

def aboutus(request):
    return render(request,'booking/aboutus.html')

def contactus(request):
    return render(request,'booking/contactus.html')