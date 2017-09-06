# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


# get detailed info about request
def debug_request(request):
    print(request)
    print(type(request))
    print(dir(request))
    for attr in (dir(request)):
        print(attr)
        print(getattr(request, attr))


# Create your views here.
def index(request):
    # debug_request(request)
    return HttpResponse('<em>Hello World!</em>')
