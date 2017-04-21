"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app.views import index, delete, login, base, add, user,app

urlpatterns = [

    # url(r'^index/(\d*)/(\d*)', index),
    # url(r'^index/(\d*)/(\d*)', index),

    url(r'^index/$', index),
    url(r'^del/(?P<name>\w*)/$', delete),
    url(r'^base/login/$', login),
    url(r'^base/user/$', user),
    url(r'^base/$', base, name="base"),
    url(r'^add/$', add, name='add'),
    url(r'^$', app, name='app'),
    # url(r'^index/(?P<name>\d*)/$', index, {'id': 111}), 
]
