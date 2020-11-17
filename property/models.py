from django.db import models
from django.shortcuts import reverse
from core.models import Region
# Create your models here.

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


class Property(models.Model):
    SALE = 'sale'
    RENT = 'rent'
    PROPERTY_PURPOSE_TYPE = [
        (SALE, 'sale'),
        (RENT, 'rent'),
    ]
    
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name='properties')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    purpose = models.CharField(max_length=4, choices=PROPERTY_PURPOSE_TYPE, default=SALE)
    # #######
    address = models.CharField(max_length=200, null=True, blank=True)
    dimension = models.CharField(max_length=200, null=True, blank=True)
    bed = models.PositiveIntegerField(default=1, null=True, blank=True)
    bath = models.PositiveIntegerField(default=1, null=True, blank=True)
    garage = models.PositiveIntegerField(default=0, null=True, blank=True)
    # #######
    image = models.ImageField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    

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



