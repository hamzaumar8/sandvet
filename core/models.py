from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    capital = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
   
class Locality(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_locality_url(self):
        return reverse("core:locality", kwargs={
            'locality': self.name
        })

