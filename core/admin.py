from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.Car)
admin.site.register(models.Rating)