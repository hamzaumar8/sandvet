from django.contrib import admin
from .models import Property, Category, Testimony, Subscription

# Register your models here.
admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Testimony)
admin.site.register(Subscription)
