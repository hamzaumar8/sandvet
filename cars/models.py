from datetime import datetime, date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from django.shortcuts import reverse
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from property.models import REGIONS_LIST
from core.models import Region, Locality
# Create your models here.

def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')


def year_choices():
    return [(r,r) for r in range(1984, date.today().year+1)]

def current_year():
    return date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    



CAR_STATE = [
    ('new', 'New'),
    ('used', 'Used'),
]

CAR_DRIVE_TYPE = [
    ('left', 'Left'),
    ('right', 'Right'),
]
CAR_AIR_CON = [
    ('no', 'No'),
    ('yes', 'Yes'),
]

CAR_FUEL_TYPE = [
    ('petrol', 'petrol'),
    ('diesel', 'Diesel'),
    ('gas', 'Gas'),
]

class Brand(models.Model):
    name = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique_with='created_at__month', slugify=custom_slugify )

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='cars/')
    description = models.TextField(null=True, blank=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with='created_at__month',slugify=custom_slugify )
    region = models.CharField(max_length=20, choices=REGIONS_LIST, null=True, blank=True)
    # #######
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='carbrands')
    int_color = models.CharField(max_length=200, null=True, blank=True)
    ext_color = models.CharField(max_length=200, null=True, blank=True)
    mileage = models.CharField(max_length=200, null=True, blank=True)
    body_type = models.CharField(max_length=200, null=True, blank=True)
    fuel_type = models.CharField(max_length=6, choices=CAR_FUEL_TYPE, null=True, blank=True)
    drive_type = models.CharField(max_length=5, choices=CAR_DRIVE_TYPE, null=True, blank=True)
    car_state = models.CharField(max_length=4, choices=CAR_STATE, null=True)
    engine = models.CharField(max_length=200, null=True, blank=True)
    air_con = models.CharField(max_length=3, choices=CAR_AIR_CON, null=True, blank=True)
    year = models.IntegerField(_('year'), validators=[MinValueValidator(1984), max_value_current_year])

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
        return reverse("cars:car-detail", kwargs={
            'slug': self.slug
        })



class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='carimages')
    image = models.ImageField(null=True, blank=True, upload_to="cars")

    def __str__(self):
        return self.car.title

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url