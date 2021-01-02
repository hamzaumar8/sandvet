from django.contrib import admin
from .models import Property, Category, Testimony, Subscription, LandProperty, RealEstate, SocialHandle, HouseProperty, Hotel, HotelRoom, HotelImage, HotelRoomImage

# Register your models here.
admin.site.register(Property)
admin.site.register(LandProperty)
admin.site.register(Category)
admin.site.register(Testimony)
admin.site.register(Subscription)
admin.site.register(RealEstate)
admin.site.register(SocialHandle)
admin.site.register(HouseProperty)
admin.site.register(Hotel)
admin.site.register(HotelRoom)
admin.site.register(HotelImage)
admin.site.register(HotelRoomImage)
