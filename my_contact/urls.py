from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from my_contact import views

urlpatterns = [
    url(r'^my_contact/$', views.my_contact, name='my_contact'),

]