from django.shortcuts import render
from django.contrib import auth


def index(request):
    username = "Bob"

    return render(request, 'chat.html', {'username': auth.get_user(request).username})
