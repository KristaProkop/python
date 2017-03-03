from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# Create your models here.
class SecretManager(models.Model):
    def create_secret(self, user_id, message):
        user = User.objects.get(id=user_id)
        secret = Secret.objects.create(posted_by=user, message=message)
        return True

    def delete_secret(self, secret_id):        # # user = User.objects.get(id=request.session['id'])
        # print user
        #add logic to test if session[id] is equal to secret posted_by id
        Secret.objects.filter(id=secret_id).delete()
        return True

class LikeManager(models.Model):
    def create_like(self, user_id, message_id):
        user = User.objects.get(id=user_id)
        print "user object:", user
        secret = Secret.objects.get(id=message_id)
        print "secret object:", secret
        Like.objects.create(secret=secret, liker=user)
        return True


class Secret(models.Model):
    message = models.TextField(max_length=1000)
    posted_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    SecretManager = SecretManager()


class Like(models.Model):
    secret = models.ForeignKey(Secret)
    liker = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    LikeManager = LikeManager()
