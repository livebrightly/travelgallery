from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Map(models.Model):
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    # user foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location



class ImageInfo(models.Model):
    name = models.CharField(max_length=200, default="new image")
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'images_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    image = models.ForeignKey(ImageInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for images_id: {self.image_id} @{self.url}"
