from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def signin(request):
    return render(request, 'blog/signin.html')


def signout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')
