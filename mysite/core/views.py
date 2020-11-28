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

def secret_page(request):
    return render(request,'registration/secret_page.html') 
@login_required
def booking(request):
    return render(request,'booking/bookhere.html')