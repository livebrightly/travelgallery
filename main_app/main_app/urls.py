from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery_index, name='index'),
    path('gallery/<int:images_id>/', views.details, name='details'),
    path('images/create/', views.ImageInfoCreate.as_view(), name='images_create'),
    path('images/<int:pk>/update/',
         views.ImageInfoUpdate.as_view(), name='images_update'),
    path('images/<int:pk>/delete/',
         views.ImageInfoDelete.as_view(), name='images_delete'),
    path('images/<int:images_id>/add_photo/',
         views.add_photo, name='add_photo'),
]
