from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from core.models import  Locality, REGIONS_LIST
# Create your models here.

def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')


# Create your models here.
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
    address = models.CharField(max_length=200, null=True, blank=True)
    bed = models.PositiveIntegerField(default=1, null=True, blank=True)
    bath = models.PositiveIntegerField(default=1, null=True, blank=True)
    garage = models.PositiveIntegerField(default=0, null=True, blank=True)
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
    owned_by = models.ForeignKey("RealEstate", on_delete=models.CASCADE, null=True, blank=True, related_name="realestates")

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
        return reverse("property:property", kwargs={
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
        return self.created_at


    def get_land_details(self):
        return LandProperty.objects.get(property=self)






class RealEstate(models.Model):
    title = models.CharField(max_length=200,null=True, unique=True)
    region = models.CharField(choices=REGIONS_LIST, max_length=20, null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
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

    def get_absolute_url(self):
        return reverse("property:property", kwargs={
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
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    linkedIn = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.realestate.title



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

   