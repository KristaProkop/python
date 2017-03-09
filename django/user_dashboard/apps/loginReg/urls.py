from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^signin$', views.display_login, name="display_login"),
    url(r'^register$', views.display_registration, name="display_registration"),
    url(r'^logoff$', views.logoff, name="logoff"),
    url(r'^validate$', views.validate, name="validate"),
    url(r'^login$', views.login, name="login"),
    url(r'^update_description/(?P<id>\d+)$', views.update_description, name="update_description"),
    url(r'^update_information/(?P<id>\d+)$', views.update_information, name="update_information"),
    url(r'^update_password/(?P<id>\d+)$', views.update_password, name="update_password"),
    url(r'^new_user$', views.new_user, name="new_user"),
    url(r'^delete/(?P<id>\d+)$', views.delete_user, name="delete_user"),
]