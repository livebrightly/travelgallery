from .models import ImageInfo, Photo
import boto3
import uuid
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from multiprocessing import context


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'travelgallerybucket'


def home(request):
    return HttpResponse('This is the gallery')


def about(request):
    return render(request, 'gallery/about.html')


def gallery(request):
    return HttpResponse('This is the gallery')


def gallery_index(request):
    images = ImageInfo.objects.all()
    return render(request, 'gallery/index.html', {'images': images})


class ImageInfoCreate(CreateView):
    model = ImageInfo
    fields = ['name', 'url', 'description']
    success_url = '/'


class ImageInfoUpdate(UpdateView):
    model = ImageInfo
    # Let's disallow the renaming of a image by excluding the name field!
    fields = ['name', 'url', 'description']
    success_url = '/travel/gallery/'


def details(request, images_id):
    image = ImageInfo.objects.get(id=images_id)
    return render(request, 'gallery/details.html', {
        'image': image})


class ImageInfoDelete(DeleteView):
    model = ImageInfo
    success_url = '/travel/gallery/'


def add_photo(request, images_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            print(BUCKET)
            print(S3_BASE_URL)
            print(photo_file)
            print(key)
            print(images_id)
            # we can assign to image_id or image (if you have a image object)
            photo = Photo(url=url, images_id=images_id)
            photo.save()         
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', images_id=images_id)
