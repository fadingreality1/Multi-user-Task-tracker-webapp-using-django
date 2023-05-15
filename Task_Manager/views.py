from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

def home(req):
    return render(req, "home.html")

def signup(req):
    if req.method == "POST":
        f = UserCreationForm(req.POST)
        if f.is_valid():
            # return HttpResponse("sahi h bhai")
            user = f.save()
            if user is not None:
                redirect('home')
        else:
            return render(req, "signup.html", {'form':f})
    f = UserCreationForm()
    return render(req, "signup.html", {'form':f})

def login(req):
    return render(req, "login.html")

def contact(req):
    return render(req, "contact.html")