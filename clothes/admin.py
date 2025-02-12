from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ClothesModel)
admin.site.register(models.Tag)