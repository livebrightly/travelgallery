from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path
from . import views


# basic string HTTP response
urlpatterns = [
    path('', views.default_map, name="default"),
    path('maps/', views.maps_index, name='index'),
    path('about/', views.about, name="about"),
    path('/<int:map_id>/add_photo/', views.add_photo, name='add_photo')
]


# NOTE from map api docs
# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'', views.default_map, name="default"),
# ]
