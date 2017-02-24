from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length= 30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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