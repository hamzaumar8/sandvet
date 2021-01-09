from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from core.models import  Locality, REGIONS_LIST, Booking
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')


def get_dated(created_at):
    time = datetime.now()
    if created_at.day == time.day:
        return str(time.hour - created_at.hour) + " hours ago"
    else:
        if created_at.month == time.month:
            return str(time.day - created_at.day) + " days ago"
        else:
            if created_at.year == time.year:
                return str(time.month - created_at.month) + " months ago"
            else:
                return str(time.year - created_at.year) + " year(s) ago"
    return created_at

# Create your models here.
STAR_RATING = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

PRICE_NEGORIABLE = (
    ('yes', 'Yes'),
    ('no', 'No'),
)



PROPERTY_PURPOSE_TYPE = [
    ('sale', 'sale'),
    ('rent', 'rent'),
]

class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with='created_at__month',slugify=custom_slugify )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_category_url(self):
        return reverse("core:category", kwargs={
            'slug': self.slug
        })

    def get_for_sale_category_url(self):
        return reverse("property:for-sale-cate", kwargs={
            'slug': self.slug
        })

    def get_for_rent_category_url(self):
        return reverse("property:for-rent-cate", kwargs={
            'slug': self.slug
        })





class LandProperty(models.Model):
    property = models.OneToOneField("Property",  on_delete=models.CASCADE, related_name='landproperty', null=True)
    dimension = models.CharField(max_length=200, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.property.title




class HouseProperty(models.Model):
    property = models.OneToOneField("Property",  on_delete=models.CASCADE, related_name='houseproperty', null=True)
    #
    bed = models.PositiveIntegerField(default=1, null=True, blank=True)
    bath = models.PositiveIntegerField(default=1, null=True, blank=True)
    garage = models.PositiveIntegerField(default=0, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    amenities = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.property.title







class Property(models.Model):
    title = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    price_negotiable = models.CharField(max_length=3, choices=PRICE_NEGORIABLE, default='no')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=4, choices=PROPERTY_PURPOSE_TYPE, default='sale')
    region = models.CharField(choices=REGIONS_LIST, max_length=20, null=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)
    location_address = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='property/')
    description = models.TextField(null=True, blank=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(
                populate_from='title', 
                unique_with='created_at__month',
                slugify=custom_slugify
            )
    owned_by = models.ForeignKey("RealEstate", on_delete=models.CASCADE, null=True, blank=True, related_name="realestate")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("property:property-detail", kwargs={
            'slug': self.slug
        })

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
                else:
                    return str(time.year - self.created_at.year) + " year(s) ago"
        return self.created_at


    def get_land_details(self):
        return LandProperty.objects.get(property=self)


class PropertyImage(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True, related_name='propertyimages')
    images = models.ImageField(null=True, blank=True, upload_to="property/imgs/")

    def __str__(self):
        return self.property.title

    @property
    def imageURL(self):
        try:
            url =self.images.url 
        except:
            url = ''
        return url




class RealEstate(models.Model):
    title = models.CharField(max_length=200,null=True, unique=True)
    region = models.CharField(choices=REGIONS_LIST, max_length=20, null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
    location_address = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='realeastate/logo', null=True)
    image = models.ImageField(upload_to='realeastate/')
    description = models.TextField(null=True, blank=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(
                populate_from='title', 
                unique_with='created_at__month',
                slugify=custom_slugify
            )

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url
    
    @property
    def logoURL(self):
        try:
            url = self.logo.url 
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("property:realestate-detail", kwargs={
            'slug': self.slug
        })

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
                else:
                    return str(time.year - self.created_at.year) + " year(s) ago"
        return self.created_at


    def get_land_details(self):
        return LandProperty.objects.get(property=self)




class RealEstateImage(models.Model):
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, null=True, blank=True, related_name='realestateimages')
    images = models.ImageField(null=True, blank=True, upload_to="realestate/imgs/")

    def __str__(self):
        return self.realestate.title

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url



class SocialHandle(models.Model):
    realestate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, null=True, blank=True, related_name='socialhandle')
    facebook = models.URLField(max_length=200, null=True, blank=True)
    linkedIn = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.realestate.title



class Testimony(models.Model):  
    name = models.CharField(max_length=200, null=True)
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url

   


class Subscription(models.Model):
    PROPERTY_PURPOSE_TYPE = [
        ('sale', 'for sale'),
        ('rent', 'for rent'),
    ]
    email = models.CharField(max_length=200, null=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    purpose = models.CharField(max_length=4, choices=PROPERTY_PURPOSE_TYPE, default='sale')
    bed = models.PositiveIntegerField(default=1)
    from_price = models.FloatField(null=True)
    to_price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.email

   

class HospitalityCategory(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with='created_at__month',slugify=custom_slugify )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    # def get_category_url(self):
    #     return reverse("core:category", kwargs={
    #         'slug': self.slug
    #     })

    # def get_for_sale_category_url(self):
    #     return reverse("property:for-sale-cate", kwargs={
    #         'slug': self.slug
    #     })

    # def get_for_rent_category_url(self):
    #     return reverse("property:for-rent-cate", kwargs={
    #         'slug': self.slug
    #     })


class Hotel(models.Model):
    title = models.CharField(max_length=200,null=True)
    location_address = models.CharField(max_length=200, null=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)
    region = models.CharField(choices=REGIONS_LIST, max_length=20, null=True)
    logo = models.ImageField(upload_to='hotels/logo', null=True)
    image = models.ImageField(upload_to='hotels/')
    description = models.TextField(null=True, blank=False)
    rate = models.CharField(choices=STAR_RATING, max_length=1, null=True, blank=True)
    free_parking = models.BooleanField(default=False)
    free_wiFi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    fitness_center = models.BooleanField(default=False)
    free_breakfast = models.BooleanField(default=False)
    free_airport_transportation = models.BooleanField(default=False)
    conference_facilities = models.BooleanField(default=False)
    bar_or_lounge = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(
                populate_from='title', 
                unique_with='created_at__month',
                slugify=custom_slugify
            )

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url

    @property
    def logoURL(self):
        try:
            url = self.logo.url 
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("property:hotel-detail", kwargs={
            'slug': self.slug
        })

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
                else:
                    return str(time.year - self.created_at.year) + " year(s) ago"
        return self.created_at


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True, related_name='hotelimages')
    images = models.ImageField(null=True, blank=True, upload_to="hotel/imgs/")

    def __str__(self):
        return self.hotel.title

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True, related_name='hotel')
    title = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='hotels/rooms/')
    description = models.TextField(null=True, blank=False)
    housekeeping = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    flatscreen_tv = models.BooleanField(default=False)
    kitchenette = models.BooleanField(default=False)
    room_service = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(
                populate_from='title', 
                unique_with='created_at__month',
                slugify=custom_slugify
            )

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url

    @property
    def logoURL(self):
        try:
            url = self.logo.url 
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("property:hotel-room-detail", kwargs={
            'slug': self.slug
        })

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
                else:
                    return str(time.year - self.created_at.year) + " year(s) ago"
        return self.created_at


    

class HotelRoomImage(models.Model):
    hotelroom = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, null=True, blank=True, related_name='hotelroomimages')
    images = models.ImageField(null=True, blank=True, upload_to="hotelroom/imgs/")

    def __str__(self):
        return self.hotelroom.title

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url






class PropertyBooking(models.Model):
    booking = models.OneToOneField(Booking,  on_delete=models.CASCADE, related_name='propertybooking', null=True)
    property = models.ForeignKey(Property,  on_delete=models.CASCADE, related_name='bookproperty', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.property.title




class RealEstateBooking(models.Model):
    booking = models.OneToOneField(Booking,  on_delete=models.CASCADE, related_name='realestatebooking', null=True)
    realestate = models.ForeignKey(RealEstate,  on_delete=models.CASCADE, related_name='bookrealestate', null=True)
    category = models.CharField(default="Real Estate", max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.realestate.title

class HotelBooking(models.Model):
    booking = models.OneToOneField(Booking,  on_delete=models.CASCADE, related_name='hotelbooking', null=True)
    hotel = models.ForeignKey(Hotel,  on_delete=models.CASCADE, related_name='bookhotel', null=True)
    category = models.CharField(default="Hotel", max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.hotel.title



class HotelRoomBooking(models.Model):
    booking = models.OneToOneField(Booking,  on_delete=models.CASCADE, related_name='hotelroombooking', null=True)
    hotelroom = models.ForeignKey(HotelRoom,  on_delete=models.CASCADE, related_name='bookhotelroom', null=True)
    category = models.CharField(default="Hotel Room", max_length=15)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hotelroom.title