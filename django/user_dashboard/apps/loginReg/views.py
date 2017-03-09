from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'loginReg/index.html', )

def logoff(request):
    request.session.clear()
    return redirect(reverse('loginReg:index'))

def display_login(request):
    return render(request, 'loginReg/login.html')

def display_registration(request):
    return render(request, 'loginReg/register.html')

def validate(request):
    valid, response = User.objects.validate(request.POST)
    if valid:
        return redirect(reverse('dashboard:index'))
    elif not valid: 
        messages.error(request, response)
        return redirect(reverse('loginReg:display_registration'))

def login(request):
    valid, response = User.objects.login(request.POST)
    if valid:
        request.session['id'] = response.id
        return redirect(reverse('dashboard:index'))
    if not valid:
        messages.error(request, response)
        return redirect(reverse('loginReg:display_registration'))

def update_description(request, id):
    description = request.POST['description']
    user = User.objects.update_description(id, description)
    return redirect(reverse('dashboard:index')) 

def update_information(request, id):
    user = User.objects.update_information(id, request.POST)
    return redirect(reverse('dashboard:index'))

def update_password(request, id):
    user = User.objects.update_password(id, request.POST)
    return redirect(reverse('dashboard:index')) 
    
def new_user(request):
    valid, response = User.objects.validate(request.POST)
    if valid:
        messages.success(request, response)
        return redirect(reverse('dashboard:index'))
    if not valid:
        messages.error(request, response)
        return redirect(reverse('dashboard:add_user'))

def delete_user(request, id):
    User.objects.filter(id=id).delete()
    return redirect(reverse('dashboard:index'))

