from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User

def index(request):
    return render(request, 'form_registration/index.html')

def register(request):
    valid, response = User.objects.validate_info(request.POST)
    if valid:
        valid, response = User.objects.validate_password(request.POST)
        if valid:
            valid, response = User.objects.register(request.POST)
            if valid:
                valid, response = User.objects.login(request.POST)
                if valid:
                    return redirect(reverse('form_registration:success'))
                if not valid:
                    messages.error(request, response)
            if not valid:
                messages.error(request, response)
        if not valid:
            messages.error(request, response)
    if not valid:
        messages.error(request, response)
    return redirect(reverse('form_registration:index'))

def login(request):
    valid, response = User.objects.login(request.POST)
    if valid:
        return redirect(reverse('form_registration:success'))
    else:
        messages.error(request, response)
        return redirect(reverse('form_registration:index'))

def success(request):
    return render(request, 'form_registration/success.html')

