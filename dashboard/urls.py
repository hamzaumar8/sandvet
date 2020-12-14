from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', dashboardPage, name='dashboard'),
    path('properties/', propertyPage, name='property'),
    path('property/add/', PropertyAddPage, name='add-property'),

    path('cars/', CarPage, name='car'),
    path('car/add/', CarAddPage, name='add-car'),

    # Ajax URLS
    path("dashboard/property/add/land/", ajaxPropertyLandAdd, name="add-land-property"),
]