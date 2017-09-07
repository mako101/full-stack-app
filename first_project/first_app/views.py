# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


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
    context = {
        'foo': 'America Fuck yea!!!',
        'bar': 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/190px-Flag_of_the_United_States.svg.png'
    }
    return render(request, 'first_app/index.html', context)
