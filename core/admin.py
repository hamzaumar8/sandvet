from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'sandvet admin'
admin.site.site_title = 'sandvet admin area'
admin.site.index_title = 'Welcome to the sandvet admin area'

admin.site.register(Region)
admin.site.register(Locality)
admin.site.register(Booking)