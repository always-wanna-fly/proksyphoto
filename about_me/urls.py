from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from about_me import views

urlpatterns = [
    url(r'^about_me/$', views.about_me, name='about_me'),
]