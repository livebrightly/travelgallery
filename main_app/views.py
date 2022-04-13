from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
    fields = ['name', 'url', 'description']
    success_url = '/'


class ImageUpdate(UpdateView):
    model = Image
    # Let's disallow the renaming of a image by excluding the name field!
    fields = ['name', 'url', 'description']
    success_url = '/travel/gallery/'


def details(request, images_id):
    image = Image.objects.get(id=images_id)
    return render(request, 'gallery/details.html', {
        'image': image})


class ImageDelete(DeleteView):
    model = Image
    success_url = '/travel/gallery/'
