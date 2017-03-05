from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    if "id" not in request.session:
        return render(request, 'login/index.html')
    else: 
        return redirect(reverse('books:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

def create(request):
    first_name=str(request.POST['first_name'])
    last_name=str(request.POST['last_name'])
    email=str(request.POST['email'])
    password1=str(request.POST['password1'])
    password2=str(request.POST['password2'])
    valid, response = User.userManager.validate(first_name, last_name, email, password1, password2)
    if valid:
        context = {
            'event': 'registered',
            'first_name': response
        }
        messages.success(request, "Successfully registered. Please login.")
        return redirect(reverse('login:index'))
    elif not valid: 
        messages.error(request, response)
    else:
        messages.error(request, "Something went wrong. Try again later.")
    return redirect(reverse('books:index'))
    

def login(request):
    email = str(request.POST['email'])
    password = str(request.POST['password'])
    valid, response = User.userManager.login(email, password)
    if valid:
        request.session['id'] = response.id
        request.session['name'] = response.first_name
        return redirect(reverse('books:index'))
    if not valid:
        messages.error(request, response)
        return redirect(reverse('login:index'))

