from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages

def index(request):
    context = {
        'users': User.objects.all(),
    }   
    return render(request, 'email_validation/index.html', context)

def create(request):
    valid, response = User.userManager.register(email=request.POST['email'])
    if valid:
        messages.success(request, response)
    else:
        messages.error(request, response)
    return redirect('/')

def delete(request, id):
    response = User.userManager.delete(id=id)
    messages.success(request, response)
    return redirect('/')