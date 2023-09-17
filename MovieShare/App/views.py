from django.shortcuts import render, redirect
from .models import Movie


# Create your views here.

def login(request):
    Object = Movie.objects.all()
    if request.method == 'POST':
        userName = request.POST.get('UserName')
        password = request.POST.get('Password')
        passCode = userName.upper() + password.upper()
        message = "APP1232"
        if passCode == message:
            print('LogIn successfully')
            return render(request, "home.html", {'data': Object})
        else:
            return render(request,"login.html",{'notification':'password incorrect pleas try again'})
    return render(request, "login.html")
