from django.contrib import admin
from django.urls import include, path
from . import views

# basic string HTTP response
urlpatterns = [
    path('', views.default_map, name="default"),
]


# NOTE from map api docs
# from django.conf.urls import url                                                                                                                              
# from . import views

# urlpatterns = [ 
#     url(r'', views.default_map, name="default"),
# ]