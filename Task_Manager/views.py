from django.shortcuts import render

def home(req):
    return render(req, "base.html")

def signup(req):
    return render(req, "signup.html")

def login(req):
    return render(req, "login.html")