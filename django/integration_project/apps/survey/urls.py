from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^back', views.home, name="back"),
    url(r'^process', views.process, name="process"),
    url(r'^result', views.create, name="create"),
]