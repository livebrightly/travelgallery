from django.contrib import admin
# import your models here
from .models import Map, Image

# Register your models here
admin.site.register(Map)
admin.site.register(Image)
