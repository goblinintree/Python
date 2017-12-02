# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
import time
import re

def found_404(request):
    respone_text = "您好，你访问的页面未找到！！"
    return HttpResponse(respone_text)


def hello(request):
    return HttpResponse("Hello world！ This is my first trial. [Poll的笔记]")

def hello_name(request, name):
    if re.match(r"(\w+)",name):
        respone_text = "Hello %s" % name
    else:
        respone_text = "输入用户名不合法！！"
    return HttpResponse(respone_text)

def my_home_page(request):
    return HttpResponse("Home Page!!")



def visit_html(request,html_path):
    # respone_text = "您好，你访问的页面未找到2！！"
    # return HttpResponse(respone_text)
    return render_to_response("index.html")


def current_time(request):
    return HttpResponse("Current time is: "+time.strftime('%Y-%m-%d %H:%M:%S'))

