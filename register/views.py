from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =  request.POST['last_name']
        username =   request.POST['username']
        email =      request.POST['email']
        password1 =  request.POST['password1']
        password2 =  request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.infor(request, 'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Does not match')
            return redirect('register')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
