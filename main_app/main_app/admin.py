from django.contrib import admin
# import your models here
from .models import ImageInfo, Photo

# Register your models here
# admin.site.register(Map)
admin.site.register(ImageInfo)
admin.site.register(Photo)
