from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Model):


    def validate(self, first_name, last_name, email, password1, password2):
        try: 
            User.objects.get(email=email) 
            response = "User already exists in database. Please log in instead."
        except: 
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password1) < 1 or len(password2) < 1:
                response = ("All fields are required. Please complete all fields and resubmit.")
            elif any(filter(str.isdigit, first_name)) or any(filter(str.isdigit, last_name)):
                response = ("Names cannot contain numbers. Please try again.")
            elif len(password1) < 9:
                response = ("Password must be 8 or more characters")
            elif password1 != password2:
                response = ("Passwords must match")
            elif not EMAIL_REGEX.match(email):
                response = ("Invalid Email Address!")
            else:
                hashed = bcrypt.hashpw(password1, bcrypt.gensalt())
                print "hashed pw is", hashed
                response = first_name
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
                return True, response
        return False, response

    def login(self, email, password):
        # try: 
        user = User.objects.get(email=email)
        print user
        print 'users password is', user.password
        print 'bcrypt result is', (bcrypt.hashpw(password, user.password))
        if user.password == (bcrypt.hashpw(password, user.password)):
            print user.password, user.email
            response = user.first_name
            return True, response
        else:
            response = "Email and password don't match."
            return False, response
        # except:
            response = ("Email not found.")
            return False, response


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()