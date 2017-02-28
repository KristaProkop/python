from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def create(request):
    first_name=str(request.POST['first_name'])
    last_name=str(request.POST['last_name'])
    email=str(request.POST['email'])
    password1=str(request.POST['password1'])
    password2=str(request.POST['password2'])
    valid, response = User.userManager.validate(first_name, last_name, email, password1, password2)
    if valid:
        print "valid info"
        context = {
            'event': 'registered',
            'first_name': first_name,
            'users': User.objects.all(),
        }
        return render(request, 'login/success.html', context)
    if not valid: 
        messages.error(request, response)
        return redirect('/')

def login(request):
    email = str(request.POST['email'])
    password = str(request.POST['password'])
    valid, response = User.userManager.login(email, password)
    if valid:
        context = {
            'event': "logged in",
            'first_name': response,
            'users': User.objects.all(),
        }
        return render(request, 'login/success.html', context)
    if not valid:
        messages.error(request, response)
        return redirect('/')

def success(request):
    print 'success'