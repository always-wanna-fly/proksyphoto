from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from gallery import views

urlpatterns = [
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery/(?P<gallery_id>\w+)/$', views.galleries, name='galleries'),
]