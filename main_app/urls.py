from django.contrib import admin
from django.urls import include, path
from . import views


# basic string HTTP response
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery_index, name='index'),
    path('gallery/<int:images_id>/', views.details, name='details'),
    path('images/create/', views.ImageCreate.as_view(), name='images_create'),
    path('images/<int:pk>/update/',
         views.ImageUpdate.as_view(), name='images_update'),
    path('images/<int:pk>/delete/',
         views.ImageDelete.as_view(), name='images_delete'),
]
