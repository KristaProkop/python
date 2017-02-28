from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

class UserManager(models.Model):
    def validate(self, first_name, last_name, email, password1, password2):
        try: 
            User.objects.get(email=email) 
            response = "User already exists. Please log in instead."
        except: 
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            if len(first_name) < 2 or len(last_name) <2 :
                response = ("First and last name must be 2 or more characters.")
            elif any(filter(str.isdigit, first_name)) or any(filter(str.isdigit, last_name)):
                response = ("Names cannot contain numbers. Please try again.")
            elif password1 != password2:
                response = ("Passwords must match")
            elif len(password1) < 8:
                response = ("Password must be 8 or more characters")
            elif not EMAIL_REGEX.match(email):
                response = ("Invalid Email Address!")
            else:
                hashed = bcrypt.hashpw(password1, bcrypt.gensalt())
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
                response = first_name
                return True, response
        return False, response

    def login(self, email, password):
        try: 
            user = User.objects.get(email=email)
            userPwBytes = password.encode('utf-8')
            hashedPwBytes = user.password.encode('utf-8')
            if hashedPwBytes == (bcrypt.hashpw(userPwBytes, hashedPwBytes)):
                response = user.first_name
                return True, response
            else:
                response = "Email and password don't match."
                return False, response
        except:
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