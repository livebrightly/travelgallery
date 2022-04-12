from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from django.views.generic.edit import CreateView
# from django.views.generic.edit import ListView, CreateView, UpdateView, DeleteView

from .models import Image


def home(request):
    return HttpResponse('This is the gallery')


def about(request):
    return render(request, 'gallery/about.html')


def gallery(request):
    return HttpResponse('This is the gallery')

# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def gallery_index(request):
    images = Image.objects.all()
    return render(request, 'gallery/index.html', {'images': images})


class ImageCreate(CreateView):
    model = Image
    fields = fields = ['url', 'description']
    success_url = '/gallery/'
