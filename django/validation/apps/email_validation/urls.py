from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate$', views.create),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]