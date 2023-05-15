from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate



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
        f = AuthenticationForm(data = req.POST)
        if f.is_valid():
            u = f.cleaned_data.get('username')
            p = f.cleaned_data.get('password')
            user = authenticate(username = u, password = p)
            print(user)
            return HttpResponse("login ho gya")
        else:
            f = AuthenticationForm(data = req.POST)
            return render(req, "login.html", {'form':f})
    f = AuthenticationForm()
    return render(req, "login.html", {'form':f})

def contact(req):
    return render(req, "contact.html")