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
    path('brand/<int:id>/edit/', BrandEditPage, name='edit-brand'),
    
    path('car/types/', TypePage, name='types'),
    path('car/type/add/', TypeAddPage, name='add-type'),
    path('car/type/<int:id>/edit/', TypeEditPage, name='edit-type'),
    path('car/type/<int:id>/delete/', DeleteType, name='delete-type'),

    # SPARE PARTS
    path('car/spare-parts/', SparePartPage, name='spare-parts'),
    path('car/spare-part/add/', SparePartAddPage, name='add-spare-part'),
    path('car/spare-part/<int:id>/Edit/', SparePartEditPage, name='edit-spare-part'),
    path('car/spare-part/<int:id>/view/', ViewSparePart, name='view-spare-part'),
    path('car/spare-part/<int:id>/featured/', FeaturedSparePart, name='featured-spare-part'),
    path('car/spare-part/<int:id>/delete/', DeleteSparePart, name='delete-spare-part'),
    path('car/spare-part/image/<int:id>/delete/', DeleteSparePartImage, name='delete-sparepart-image'),
    
    # DRIVING SCHOOL
    path('car/driving-schools/', SchoolPage, name='schools'),
    path('car/driving-school/add/', SchoolAddPage, name='add-school'),
    path('car/driving-school/<int:id>/Edit/', SchoolEditPage, name='edit-school'),
    path('car/driving-school/<int:id>/view/', ViewSchool, name='view-school'),
    path('car/driving-school/<int:id>/featured/', FeaturedSchool, name='featured-school'),
    path('car/driving-school/<int:id>/delete/', DeleteSchool, name='delete-school'),
    path('car/driving-school/image/<int:id>/delete/', DeleteSchoolImage, name='delete-school-image'),

    # Ajax URLS
    path("dashboard/property/add/land/", ajaxPropertyLandAdd, name="add-land-property"),
]