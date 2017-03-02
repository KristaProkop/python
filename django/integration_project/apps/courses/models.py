from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# Create your models here.
class CourseManager(models.Model):
    def merge(self, user_id, course_id):
        user = User.objects.get(id=user_id)
        print user
        course = Course.objects.get(id=course_id)
        response = Course.user_creator.add(user)
        print response
        return True


class Course(models.Model):
    name = models.CharField(max_length=255)
    user_creator = models.ManyToManyField(User, null=True, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courseManager = CourseManager()



class Description(models.Model):
    course = models.ForeignKey(Course)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
