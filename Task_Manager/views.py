from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(req):
    return render(req, "home.html")

def signup(req):
    if req.method == "POST":
        f = UserCreationForm(req.POST)
        if f.is_valid():
            user = f.save()
            if user is not None:
                return redirect('login')
        else:
            return render(req, "signup.html", {'form':f})
    f = UserCreationForm()
    return render(req, "signup.html", {'form':f})

def login(req):
    if req.method == "POST":
        pass
        
    f = AuthenticationForm()
    return render(req, "login.html", {'form':f})

def contact(req):
    return render(req, "contact.html")