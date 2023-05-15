from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(req):
    return render(req, "home.html")

def signup(req):
    form = UserCreationForm()
    return render(req, "signup.html", {'form':form})

def login(req):
    return render(req, "login.html")

def contact(req):
    return render(req, "contact.html")