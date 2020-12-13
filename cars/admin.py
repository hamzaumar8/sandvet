from django.contrib import admin
from .models import Car, Brand, CarImage
# Register your models here.

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(CarImage)