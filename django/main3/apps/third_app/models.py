from __future__ import unicode_literals
from django.db import models
  # Create your models here.

class UserManager(models.Manager):
    def login(self, email, password):
        print "Running a login function!"
        print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
        return "I will be a future login method"

    def register(self, **kwargs):
        print ("Register a user here")
        print ("If successful, maybe return {'theuser':user} where user is a user object?")
        print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
        pass

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting
      # the old hidden objects key with a new one with extra properties!!!
    userManager = UserManager()
      # *************************


# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     blog = models.TextField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class Comment(models.Model):
#     blog = models.ForeignKey(Blog)
#     comment = models.TextField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class User(models.Model):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     password = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# from django.db import models

# class People(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length= 30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class User(models.Model):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     password = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True) 

# class Post(models.model):
#     title = models.CharField(max_length=45)
#     message = models.TextField(max_length=1000)
#     user_id = models.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True) 