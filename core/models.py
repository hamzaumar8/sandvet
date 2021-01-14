from django.db import models
from django.shortcuts import reverse
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')

REGIONS_LIST = (
    ('ashanti', 'Ashanti'),
    ('ahafo', 'Ahafo'),
    ('brong-ahafo', 'Brong Ahafo'),
    ('bono-east', 'Bono East '),
    ('central', 'Central'),
    ('eastern', 'Eastern'),
    ('greater-accra', 'Greater Accra'),
    ('northern', 'Northern'),
    ('savannah', 'Savannah'), 
    ('north-east', 'North East'), 
    ('upper-east', 'Upper East'),
    ('upper-west', 'Upper West'),
    ('volta', 'Volta'),
    ('oti', 'Oti Region'),
    ('werstern', 'Western'),
    ('werstern-north', 'Western North'),
)

class Region(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    capital = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_region_url(self):
        return reverse("core:region", kwargs={
            'region': self.name
        })
    
   
class Locality(models.Model):
    region = models.CharField(choices=REGIONS_LIST, max_length=20, null=True)
    name = models.CharField(max_length=200, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name',unique_with='created_at__month',slugify=custom_slugify)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_locality_url(self):
        return reverse("core:locality", kwargs={
            'locality': self.slug
        })






class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number =phone_number = PhoneNumberField()
    subject = models.CharField(max_length=200,null=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number =phone_number = PhoneNumberField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


