from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from core.models import Region, Locality
# Create your models here.


PROPERTY_PURPOSE_TYPE = [
    ('sale', 'sale'),
    ('rent', 'rent'),
]

class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_category_url(self):
        return reverse("core:category", kwargs={
            'category': self.title
        })

    def get_for_sale_category_url(self):
        return reverse("property:for-sale-cate", kwargs={
            'category': self.title
        })

    def get_for_rent_category_url(self):
        return reverse("property:for-rent-cate", kwargs={
            'category': self.title
        })











class CarProperty(models.Model):
    asset = models.ForeignKey("Property",  on_delete=models.CASCADE, related_name='carproperty')

    # #######
    color = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title




class LandProperty(models.Model):
    asset = models.ForeignKey("Property",  on_delete=models.CASCADE, related_name='landproperty')
    # 
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name='landproperty')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
    # #######
    address = models.CharField(max_length=200, null=True, blank=True)
    dimension = models.CharField(max_length=200, null=True, blank=True)
    bed = models.PositiveIntegerField(default=1, null=True, blank=True)
    bath = models.PositiveIntegerField(default=1, null=True, blank=True)
    garage = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title











class Property(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    purpose = models.CharField(max_length=4, choices=PROPERTY_PURPOSE_TYPE, default='sale')
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

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