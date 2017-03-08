from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import User, UserManager

class MessageManager(models.Manager):
    def create_message(request, postData, id):
        return True

class CommentManager(models.Manager):
    def create_comment(request, postData, id):
        return True


class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = MessageManager()
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()

    def __str__(self):
        return self.title

