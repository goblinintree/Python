# -*- coding: UTF-8 -*-

from django.http import HttpResponse

def found_404(request):
    respone_text = "您好，你访问的页面未找到！！"
    return HttpResponse(respone_text)
