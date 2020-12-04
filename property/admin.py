from django.contrib import admin
from .models import Property, Category, Testimony, Subscription, LandProperty

# Register your models here.
admin.site.register(Property)
admin.site.register(LandProperty)
admin.site.register(Category)
admin.site.register(Testimony)
admin.site.register(Subscription)
