from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_user, name="add_user"),
    url(r'^edit/(?P<id>\d+)$', views.edit_user, name="edit_user"),
    url(r'^show/(?P<id>\d+)$', views.show_user, name="show_user"),
    url(r'^create/(?P<user_id>\d+)/(?P<creator_id>\d+)$', views.create_message, name="create_message"),
    url(r'^create_comment/(?P<user_id>\d+)/(?P<message_id>\d+)$', views.create_comment, name="create_comment"),

]