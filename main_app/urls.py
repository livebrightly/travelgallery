from django.contrib import admin
from django.urls import include, path
from . import views


# basic string HTTP response
urlpatterns = [
    path('', views.test, name='test'),
]

