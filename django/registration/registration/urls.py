from django.conf.urls import url, include
from django.contrib import admin
from apps.form_registration.models import User

urlpatterns = [
    url(r'^', include('apps.form_registration.urls', namespace="registration")),
]
