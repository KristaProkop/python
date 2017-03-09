from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
from .forms import RegisterForm, LoginForm

def index(request):
    registerform = RegisterForm()
    loginform = LoginForm()
    context = { 
        "regForm": registerform,
        'logForm': loginform, 
        }
    return render(request, 'form_registration/index.html', context)

def register(request):
    if request.method == "POST":
        bound_form = RegisterForm(request.POST)
        print bound_form.is_valid() 
        print bound_form.errors 
        valid_info, response = User.objects.validate_info(request.POST)
        if valid_info:
            valid_password, response = User.objects.validate_password(request.POST)
            if valid_password:
                valid_registration, response = User.objects.register(request.POST)
                if valid_registration:
                    valid_login, response = User.objects.login(request.POST)
                    if valid_login:
                        request.session['id'] = response.id
                        request.session['first_name'] = response.first_name
                        messages.success(request, "Successfully registered")
                        return redirect(reverse('registration:success'))
        else:
            messages.error(request, response)
    return redirect(reverse('registration:index'))

def login(request):
    if request.method == "POST":
        valid, response = User.objects.login(request.POST)
        if valid:
            request.session['id'] = response.id
            request.session['first_name'] = response.first_name
            messages.success(request, "Successfully logged in")
            return redirect(reverse('registration:success'))
        else:
            messages.error(request, response)
    return redirect(reverse('registration:index'))

def success(request):
    return render(request, 'form_registration/success.html')

