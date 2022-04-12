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

  # Add this method
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'map_id': self.id})


class Image(models.Model):
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # map = models.ForeignKey(Map, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'images_id': self.id})

    # def __str__(self):
    #     return f"Photo for map_id: {self.map_id} @{self.url}"
