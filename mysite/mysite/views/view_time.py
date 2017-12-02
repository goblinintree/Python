# -*- coding: UTF-8 -*-
from django.http import HttpResponse
import time

def current_time(request):
    return HttpResponse("Current time is: "+time.strftime('%Y-%m-%d %H:%M:%S'))