from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from loginsys import views
# from chat.loginsys import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
]
