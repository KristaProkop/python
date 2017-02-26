from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def confirm(request, id):
    context = {
        'course': Course.objects.get(id=id),
    }
    return render(request, 'courses/confirm.html', context)

def delete(request, id):
    print request.POST['delete']
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
