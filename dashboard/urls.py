from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', dashboardPage, name='dashboard'),
    path('properties/', propertyPage, name='property'),
    path('property/add/', PropertyAddPage, name='add-property'),

    path('cars/', CarPage, name='car'),
    path('car/add/', CarAddPage, name='add-car'),
    path('car/<int:id>/delete/', DeleteCar, name='delete-car'),
    path('car/<int:id>/edit/', CarEditPage, name='edit-car'),
    path('car/<int:id>/view/', ViewCar, name='view-car'),
    path('car/image/<int:id>/delete/', DeleteCarImage, name='delete-car-image'),
    path('car/<int:id>/featured/', FeaturedCar, name='featured-car'),

    path('brands/', BrandPage, name='brands'),
    path('brand/add/', BrandAddPage, name='add-brand'),
    path('brand/<int:id>/featured/', FeaturedBrand, name='featured-brand'),
    path('brand/<int:id>/view/', ViewBrand, name='view-brand'),
    path('brand/<int:id>/delete/', DeleteBrand, name='delete-brand'),
    path('brand/<int:id>eEdit/', BrandEditPage, name='edit-brand'),
    
    path('car/types/', TypePage, name='types'),
    path('car/type/add/', TypeAddPage, name='add-type'),
    path('car/type/<int:id>/edit/', TypeEditPage, name='edit-type'),
    path('car/type/<int:id>/delete/', DeleteType, name='delete-type'),

    # Ajax URLS
    path("dashboard/property/add/land/", ajaxPropertyLandAdd, name="add-land-property"),
]