from colorfield.fields import ColorField
from datetime import datetime, date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from django.shortcuts import reverse
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from core.models import Region, Locality, REGIONS_LIST
# Create your models here.

def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')

def year_choices():
    return [(r,r) for r in range(1984, date.today().year+1)]

def current_year():
    return date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    


CARE_PURPOSE_TYPE = [
    ('sale', 'Sale'),
    ('hire', 'Hire'),
]

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

CAR_GEARBOX = [
    ('automatic', 'Automatic'),
    ('manual', 'Manual'),
]

CAR_FUEL_TYPE = [
    ('petrol', 'Petrol'),
    ('diesel', 'Diesel'),
    ('gas', 'Gas'),
]


class Type(models.Model):
    name = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique_with='created_at__month', slugify=custom_slugify )
    
    def __str__(self):
        return self.name

    
    

class Brand(models.Model):
    name = models.CharField(unique=True, max_length=200)
    featured = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='brands/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique_with='created_at__month', slugify=custom_slugify )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url
    
    def get_absolute_url(self):
        return reverse("cars:brand", kwargs={
            'slug': self.slug
        })


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
    
    purpose = models.CharField(max_length=4, choices=CARE_PURPOSE_TYPE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='carbrands')
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True, related_name='carlocality')
    car_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name='cartypes')
    int_color = ColorField(default="#FFFFFF", null=True, blank=True)
    ext_color = ColorField(default="#FFFFFF", null=True, blank=True)
    mileage = models.CharField(max_length=200, null=True, blank=True)
    fuel_type = models.CharField(max_length=6, choices=CAR_FUEL_TYPE, null=True, blank=True)
    gearbox = models.CharField(max_length=10, choices=CAR_GEARBOX, null=True, blank=True)
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



class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='carimages')
    images = models.ImageField(null=True, blank=True, upload_to="cars")

    def __str__(self):
        return self.car.title

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url





class SparePart(models.Model):
    title = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='spareparts/')
    description = models.TextField(null=True, blank=False)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with='created_at__month',slugify=custom_slugify )
    region = models.CharField(max_length=20, choices=REGIONS_LIST, null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True, related_name='sparelocality')
    condition = models.CharField(max_length=4, choices=CAR_STATE, null=True)

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
        return reverse("cars:spare-part-detail", kwargs={
            'slug': self.slug
        })




class SparePartImage(models.Model):
    sparepart = models.ForeignKey(SparePart, on_delete=models.CASCADE, null=True, blank=True, related_name="sparepartimages")
    images = models.ImageField(null=True, blank=True, upload_to="cars/spareparts")

    def __str__(self):
        return self.sparepart.title

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url






class School(models.Model):
    title = models.CharField(max_length=200,null=True)
    region = models.CharField(max_length=20, choices=REGIONS_LIST, null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True, related_name='schoollocality')
    image = models.ImageField(upload_to='school/')
    description = models.TextField(null=True, blank=False)
    location = models.CharField(max_length=20, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    featured = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with='created_at__month',slugify=custom_slugify )

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
        return reverse("cars:school-detail", kwargs={
            'slug': self.slug
        })


    
class SchoolImage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name="schoolimage")
    images = models.ImageField(null=True, blank=True, upload_to="cars/school")

    def __str__(self):
        return self.sparepart.title

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url