# -*- coding: UTF-8 -*-

from django.http import HttpResponse

def my_home_page(request):
    return HttpResponse("Home Page!!")