from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', dashboardPage, name='dashboard'),
    path('properties/', propertyPage, name='property'),
    path('property/add/', PropertAddPage, name='add-property'),
]