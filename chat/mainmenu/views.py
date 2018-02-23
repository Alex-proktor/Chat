from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context


def index(request):
    username = "Bob"

    return render(request, 'chat.html', {'user_name': username})

