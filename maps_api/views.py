from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'travelgallerybucket'


# Create your views here.


def default_map(request):
    my_map_token = os.environ['mapbox_access_token']
    return render(request, 'default.html', {'my_map_token': my_map_token})


def aboutMapBox(request):
    return render(request, 'aboutMapBox.html')


def maps_index(request):
    return render(request, 'maps/index.html')


def add_photo(request, map_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            image = ImageInfo(url=url, map_id=map_id)
            image.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', map_id=map_id)
