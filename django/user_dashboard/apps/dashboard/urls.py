from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_user, name="add_user"),
    url(r'^edit$', views.edit_user, name="edit_user"),
    url(r'^show$', views.show_user, name="show_user"),
]