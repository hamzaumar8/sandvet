from django.db import models
from django.shortcuts import reverse
# Create your models here.

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
    region = models.CharField(choices=REGIONS_LIST, max_length=20, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_locality_url(self):
        return reverse("core:locality", kwargs={
            'locality': self.name
        })

