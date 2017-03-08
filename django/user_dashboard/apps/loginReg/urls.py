from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^signin$', views.display_login, name="display_login"),
    url(r'^register$', views.display_registration, name="display_registration"),
    url(r'^logoff$', views.logoff, name="logoff"),

]