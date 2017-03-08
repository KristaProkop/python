from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.loginReg.urls', namespace="loginReg")),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace="dashboard")),
    url(r'^users/', include('apps.dashboard.urls', namespace="users")),
]
