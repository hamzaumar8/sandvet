from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'sandvet admin'
admin.site.site_title = 'sandvet admin area'
admin.site.index_title = 'Welcome to the sandvet admin area'

# class WishListAdmin(admin.TabularInline):
#     model = WishList
# class ToursiteImageInline(admin.TabularInline):
#     model = ToursiteImage
#     extra = 1

# class ToursiteAdmin(admin.ModelAdmin):
#     inlines = [ ToursiteImageInline,]

# admin.site.register(TourSite, ToursiteAdmin)
# admin.site.register(Order)
# admin.site.register(OrderTourSite)
# admin.site.register(WishList)
# admin.site.register(Town)
admin.site.register(Region)
admin.site.register(Locality)
# admin.site.register(PaidTour)