from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('mainmenu.urls')),
]
