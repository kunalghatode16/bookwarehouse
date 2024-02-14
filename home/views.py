from django.shortcuts import render,redirect
# Create your views here.
from home.models import User

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        email=request.POST.get('remail')
        password=request.POST.get('rpassword')
        u = User(email=email, password=password)
        u.save()
        return redirect("/login/")
    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")
