"""
from django.conf.urls import *
#from django.contrib import admin
from . import views
from django.contrib import admin
from django.conf import settings

urlspatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
