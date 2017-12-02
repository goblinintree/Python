"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib import admin


from mysite.views.view_hello import *
from mysite.views.view_time import *
from mysite.views.view_home import *
from mysite.views.view_404 import *


urlpatterns = [
    url(r'^$', my_home_page),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'/static/favicon.ico',permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^hello/(\w+)/$', hello_name),
    url(r'^now/$', current_time),
    url(r'^', found_404),
]
