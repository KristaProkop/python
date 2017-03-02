from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.create,name="create"),
    url(r'^confirm/(?P<id>\d+)$', views.confirm,name="confirm"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^merge_user$', views.merge_user, name="merge_user")
]