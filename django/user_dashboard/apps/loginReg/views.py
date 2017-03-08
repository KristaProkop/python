from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'loginReg/index.html', )

def display_login(request):
    return render(request, 'loginReg/login.html')

def display_registration(request):
    return render(request, 'loginReg/register.html')

def logoff(request):
    request.session.clear()
    return redirect(reverse('loginReg:index'))

def add_user(request):
    return render(request, 'loginReg/add_user.html')