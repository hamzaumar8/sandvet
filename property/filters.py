import django_filters

from .models import *

class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location_address = django_filters.CharFilter(field_name='location_address', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Property
        fields = [
            'title',
            'location_address', 
            'category', 
            'locality',
            'region',
        ]


class RealEstateFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location_address = django_filters.CharFilter(field_name='location_address', lookup_expr='icontains')
    class Meta:
        model = RealEstate
        fields = [
            'title',
            'location_address', 
            'locality',
            'region',
        ]

class PropertyCategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location_address = django_filters.CharFilter(field_name='location_address', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Property
        fields = [
            # 'property__title',
            # 'property__locality',
            # 'property__region',
            'title',
            'location_address',
            'locality',
            'region',
        ]


class HomePropertFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Property
        fields = [
            'title', 
            'category'
        ]




class HotelFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location_address = django_filters.CharFilter(field_name='location_address', lookup_expr='icontains')
    class Meta:
        model = Hotel
        fields = [
            'title',
            'location_address', 
            'locality',
            'region',
            'free_parking',
            'free_wiFi',
            'pool',
            'free_breakfast',
            'fitness_center',
            'free_airport_transportation',
            'conference_facilities',
            'bar_or_lounge',

        ]

class HotelRoomFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = HotelRoom
        fields = [
            'title',
            'housekeeping',
            'refrigerator',
            'flatscreen_tv',
            'kitchenette',
            'room_service',
            'air_conditioning',
        ]