from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from tasks.forms import TaskForm
from tasks.models import Tasks


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

def loginUser(req):
    if req.method == "POST":
        f = AuthenticationForm(data = req.POST)
        if f.is_valid():
            u = f.cleaned_data.get('username')
            p = f.cleaned_data.get('password')
            user = authenticate(username = u, password = p)
            if user is not None:
                login(req, user)
                return redirect('home')
        else:
            f = AuthenticationForm(data = req.POST)
            return render(req, "login.html", {'form':f})
    f = AuthenticationForm()
    return render(req, "login.html", {'form':f})

def contact(req):
    return render(req, "contact.html")

@login_required(login_url="login")
def neohome(req):
    if req.user.is_authenticated:
        user = req.user
        form = TaskForm()
        alltasks = Tasks.objects.filter(user = user).order_by('-status', 'due_date')
        return render(req, "neohome.html", {'form': form, 'tasks':alltasks})

@login_required(login_url="login")
def createTask(req):
    if req.user.is_authenticated:
        user = req.user
        form = TaskForm(req.POST)
        task = form.save(commit = False)
        task.user = user
        form.save()
        return redirect("neohome")

@login_required(login_url="login")
def logoutUser(req):
    logout(req)
    return redirect("home")

@login_required(login_url="login")
def deleteTask(req, id):
    Tasks.objects.get(pk = id).delete()
    return redirect('neohome')

@login_required(login_url="login")
def changeStatus(req, id):
    task = Tasks.objects.get(pk = id)
    # print(task.status)
    if task.status == 'p':
        task.status = 'c'
    else:
        task.status = 'p'
    task.save()
    # print(task.status)
    return redirect('neohome')
    