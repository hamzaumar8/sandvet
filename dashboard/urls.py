from django.urls import path
from .views import core, prop, cars

app_name = 'dashboard'

urlpatterns = [
    path("accounts/auth/", core.auth, name="auth"),

    path('', core.dashboardPage, name='dashboard'),
    path('locality/', core.LocalityPage, name='locality'),
    path('locality/add/', core.LocalityAddPage, name='locality-add'),
    path('locality/<int:id>/edit/', core.LocalityEditPage, name='edit-locality'),
    path('locality/<int:id>/delete/', core.DeleteLocality, name='delete-locality'),

    # Bookings
    path('bookings/', core.BookingsPage, name='bookings'),
    path('booking/<int:id>/view/', core.ViewBooking, name='view-booking'),
    path('booking/<int:id>/delete/', core.DeleteBooking, name='delete-booking'),

    path('bookings/cars/', core.CarBookingsPage, name='car-bookings'),
    path('bookings/spareparts/', core.SparePartBookingsPage, name='sparepart-bookings'),
    path('bookings/driving-school/', core.SchoolBookingsPage, name='school-bookings'),
    path('bookings/properties/', core.PropertyBookingsPage, name='properties-bookings'),
    path('bookings/hotels/', core.HotelBookingsPage, name='hotels-bookings'),
    path('bookings/hotel-rooms/', core.HotelRoomBookingsPage, name='hotelrooms-bookings'),
    path('bookings/real-estates/', core.RealEstateBookingsPage, name='realestates-bookings'),

    # Propery
    path('properties/', prop.propertyPage, name='property'),
    path('property/add/', prop.PropertyAddPage, name='add-property'),
    path('property/<int:id>/edit/', prop.PropertyEditPage, name='edit-property'),
    path('property/<int:id>/view/', prop.ViewProperty, name='view-property'),
    path('property/<int:id>/delete/', prop.DeleteProperty, name='delete-property'),
    path('property/image/<int:id>/delete/', prop.DeletePropertyImage, name='delete-property-image'),

    # Property Category
    path('property/categories/', prop.CategoryPage, name='categories'),
    path('property/category/add/', prop.CategoryAddPage, name='add-category'),
    path('property/category/<int:id>/edit/', prop.CategoryEditPage, name='edit-category'),
    path('property/category/<int:id>/delete/', prop.DeleteCategory, name='delete-category'),

    # Real Estate
    path('real-estates/', prop.RealEstatePage, name='realestates'),
    path('real-estate/add/', prop.RealEstateAddPage, name='add-realestate'),
    path('real-estate/<int:id>/view/', prop.ViewRealEstate, name='view-realestate'),
    path('real-estate/<int:id>/edit/', prop.RealEstateEditPage, name='edit-realestate'),
    path('real-estate/<int:id>/delete/', prop.DeleteRealEstate, name='delete-realestate'),
    path('real-estate/<int:id>/featured/', prop.FeaturedRealEstate, name='featured-realestate'),
    path('real-estate/image/<int:id>/delete/', prop.DeleteRealEstateImage, name='delete-realestate-image'),

    # Hotels
    path('hotels/', prop.HotelsPage, name='hotels'),
    path('hotel/add/', prop.HotelAddPage, name='add-hotel'),
    path('hotel/<int:id>/view/', prop.ViewHotel, name='view-hotel'),
    path('hotel/<int:id>/featured/', prop.FeaturedHotel, name='featured-hotel'),
    path('hotel/<int:id>/edit/', prop.HotelEditPage, name='edit-hotel'),
    path('hotel/<int:id>/delete/', prop.DeleteHotel, name='delete-hotel'),
    path('hotel/image/<int:id>/delete/', prop.DeleteHotelImage, name='delete-hotel-image'),

    # Hotels Room
    path('hotel-rooms/', prop.HotelRoomsPage, name='hotel-rooms'),
    path('hotel-room/add/', prop.HotelRoomAddPage, name='add-hotel-room'),
    path('hotel-room/<int:id>/view/', prop.ViewHotelRoom, name='view-hotel-room'),
    path('hotel-room/<int:id>/edit/', prop.HotelRoomEditPage, name='edit-hotel-room'),
    path('hotel-room/<int:id>/featured/', prop.FeaturedHotelRoom, name='featured-hotel-room'),
    path('hotel-room/<int:id>/delete/', prop.DeleteHotelRoom, name='delete-hotel-room'),
    path('hotel-room/image/<int:id>/delete/', prop.DeleteHotelRoomImage, name='delete-hotel-room-image'),

    # Cars
    path('cars/', cars.CarPage, name='car'),
    path('car/add/', cars.CarAddPage, name='add-car'),
    path('car/<int:id>/delete/', cars.DeleteCar, name='delete-car'),
    path('car/<int:id>/edit/', cars.CarEditPage, name='edit-car'),
    path('car/<int:id>/view/', cars.ViewCar, name='view-car'),
    path('car/image/<int:id>/delete/', cars.DeleteCarImage, name='delete-car-image'),
    path('car/<int:id>/featured/', cars.FeaturedCar, name='featured-car'),

    path('brands/', cars.BrandPage, name='brands'),
    path('brand/add/', cars.BrandAddPage, name='add-brand'),
    path('brand/<int:id>/featured/', cars.FeaturedBrand, name='featured-brand'),
    path('brand/<int:id>/view/', cars.ViewBrand, name='view-brand'),
    path('brand/<int:id>/delete/', cars.DeleteBrand, name='delete-brand'),
    path('brand/<int:id>/edit/', cars.BrandEditPage, name='edit-brand'),
    
    path('car/types/', cars.TypePage, name='types'),
    path('car/type/add/', cars.TypeAddPage, name='add-type'),
    path('car/type/<int:id>/edit/', cars.TypeEditPage, name='edit-type'),
    path('car/type/<int:id>/delete/', cars.DeleteType, name='delete-type'),

    # SPARE PARTS
    path('car/spare-parts/', cars.SparePartPage, name='spare-parts'),
    path('car/spare-part/add/', cars.SparePartAddPage, name='add-spare-part'),
    path('car/spare-part/<int:id>/Edit/', cars.SparePartEditPage, name='edit-spare-part'),
    path('car/spare-part/<int:id>/view/', cars.ViewSparePart, name='view-spare-part'),
    path('car/spare-part/<int:id>/featured/', cars.FeaturedSparePart, name='featured-spare-part'),
    path('car/spare-part/<int:id>/delete/', cars.DeleteSparePart, name='delete-spare-part'),
    path('car/spare-part/image/<int:id>/delete/', cars.DeleteSparePartImage, name='delete-sparepart-image'),
    
    # DRIVING SCHOOL
    path('car/driving-schools/', cars.SchoolPage, name='schools'),
    path('car/driving-school/add/', cars.SchoolAddPage, name='add-school'),
    path('car/driving-school/<int:id>/Edit/', cars.SchoolEditPage, name='edit-school'),
    path('car/driving-school/<int:id>/view/', cars.ViewSchool, name='view-school'),
    path('car/driving-school/<int:id>/featured/', cars.FeaturedSchool, name='featured-school'),
    path('car/driving-school/<int:id>/delete/', cars.DeleteSchool, name='delete-school'),
    path('car/driving-school/image/<int:id>/delete/', cars.DeleteSchoolImage, name='delete-school-image'),

    # Ajax URLS
    path("dashboard/property/add/land/", prop.ajaxPropertyLandAdd, name="add-land-property"),
    path("dashboard/property/add/house/", prop.ajaxPropertyHouseAdd, name="add-house-property"),
    path("dashboard/logout/", core.authLogout, name="logout"),

]