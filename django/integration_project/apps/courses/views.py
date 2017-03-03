from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description
from django.core.urlresolvers import reverse
from ..login.models import User
from django.contrib import messages
from django.db.models import Count

def index(request):
    context = {
        'courses': Course.objects.all(),
        'descriptions': Description.objects.all(),
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
    
def users_courses(request):
    if request.method == 'POST':
        course_id = int(request.POST['course'])
        user_id = int(request.POST['user'])
        user = User.objects.get(id=user_id)
        course = Course.objects.get(id=course_id)
        course.user_creator.add(user)
         
        message = "Successfully added ", user.first_name, " to ", course.name
        print message
        messages.success(request, message)
        return redirect(reverse('courses:users_courses'))
    else:
        context = {
            'courses': Course.objects.annotate(num_users=Count('user_creator')).order_by('name'),
            # 'courses': Course.objects.all(),
            'users': User.objects.all().order_by('first_name', 'last_name'),
        }
        return render(request, 'courses/course_selector.html', context)

    



