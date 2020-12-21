from django.contrib import admin
from .models import Car, Brand, CarImage, Type, SparePart
# Register your models here.

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(Type)
admin.site.register(SparePart)