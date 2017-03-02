from django.shortcuts import render, redirect
from .models import Course, Description
from django.core.urlresolvers import reverse

def index(request):
    context = {
        'courses': Course.objects.all(),
        'descriptions': Description.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    course = Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course=course)
    return redirect(reverse('courses:index'))


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
    return redirect(reverse('courses:index'))

def add_user(request):
    context = {
        'courses': Course.objects.all(),
        #'users': Course.objects.all()
    }
    return render(request, 'courses/course_selector.html', context)

def merge_user(request):
    user_id = request.POST['user_id']
    course_id = request.POST['course_id']
    print "user id is ", user_id
    print "coures id is", course_id
    user, course = Course.courseManager.merge( course_id)
    print user, course
    return redirect(reverse('courses:add_user'))



