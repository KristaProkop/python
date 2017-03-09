from django.shortcuts import render, redirect
from .models import Course, Description

def index(request):
    context = {
        'courses': Course.objects.all(),
        'descriptions': Description.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    course = Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course=course)
    return redirect('/')


def confirm(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
        'description': Description.objects.get(course=course)
    }
    return render(request, 'courses/confirm.html', context)

def delete(request, id):
    course = Course.objects.get(id=id)
    Description.objects.get(course=course).delete()
    course.delete()
    return redirect('/')
