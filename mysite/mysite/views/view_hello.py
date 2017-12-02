# -*- coding: UTF-8 -*-

from django.http import HttpResponse
import re

def hello(request):
    return HttpResponse("Hello world！ This is my first trial. [Poll的笔记]")

def hello_name(request, name):
    if re.match(r"(\w+)",name):
        respone_text = "Hello %s" % name
    else:
        respone_text = "输入用户名不合法！！"
    return HttpResponse(respone_text)