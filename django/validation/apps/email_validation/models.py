from __future__ import unicode_literals
import re
from django.db import models


class UserManager(models.Model):
    def register(self, email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        if (len(email) < 1) or not (EMAIL_REGEX.match(email)):
            test = False
            message = "Email is not valid!"
        else:
            user = User.objects.create(email=email)
            test = True
            message = "Successfully added " + user.email + " to the database!"
        return (test, message)

    def delete(self, id):
        User.objects.get(id=id).delete()
        message = "Email address deleted"
        return message

class User(models.Model):
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
