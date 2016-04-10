from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'say$', 'deafgrandpa.views.say', name='say'),
    url(r'^$', 'deafgrandpa.views.index', name='index'),
]